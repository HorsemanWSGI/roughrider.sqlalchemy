import os
from setuptools import setup, find_packages


version = "0.1"

install_requires = [
    'sqlalchemy',
]

test_requires = [
    'pytest',
]


setup(
    name='roughrider.sqlalchemy',
    version=version,
    author='Souheil CHELFOUH',
    author_email='trollfot@gmail.com',
    url='',
    download_url='http://pypi.python.org/pypi/roughrider.sqlalchemy',
    description='WSGI SQLAlchemy Helper',
    long_description=(open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read()),
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python:: 3 :: Only',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['roughrider',],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'test': test_requires,
    },
)
