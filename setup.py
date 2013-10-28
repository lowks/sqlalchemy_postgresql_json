""" sqlalchemy-postgresql-json
	Adds JSON support to SQLAlchemy, with magic helpers to keep things mutable
"""

from setuptools import setup, find_packages
from git_version import get_git_version

setup(
    name='sqlalchemy_postgresql_json',
    version=get_git_version(),
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['psycopg2', 'sqlalchemy'])
