from typing import Type, Optional, Mapping, NamedTuple, Callable
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm.query import Query
from sqlalchemy.orm import sessionmaker, scoped_session


class SQLAlchemyEngine(NamedTuple):
    name: str
    engine: Engine
    factory: sessionmaker

    @classmethod
    def from_url(cls, name: str,
                 url: str,
                 convert_unicode: bool = True,
                 twophase: Optional[bool] = True,
                 query_cls: Type[Query] = Query):
        engine = create_engine(url, convert_unicode=convert_unicode)
        return cls(
            name=name,
            engine=engine,
            factory=sessionmaker(
                bind=engine,
                twophase=twophase,
                query_cls=query_cls
            )
        )

    @contextmanager
    def session(self):
        session = scoped_session(self.factory)
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.flush()
            session.close()

    def sqlalchemy_middleware(environ_key: Optional[str] = None):
        def app_wrapper(app: Callable):
            def caller(environ: dict, start_response: Callable):
                with self.session() as session:
                    if environ_key is not None:
                        environ[environ_key] = session
                    try:
                        response = app(environ, start_response)
                    finally:
                        if environ_key is not None:
                            del environ[environ_key]
                    return response
            return caller
        return app_wrapper