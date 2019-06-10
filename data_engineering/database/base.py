"""This code creates:

* a SQLAlchemy Engine that will interact with our dockerized PostgreSQL database,
* a SQLAlchemy ORM session factory bound to this engine,
* a base class for our classes definitions.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'docker'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = 5432
db_name = 'postgres'
DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/'

# create the postgres database engine
data_base = create_engine(f'{DATABASE_URI}{db_name}')

# make a session binding to the database in a global scope
Session = sessionmaker(data_base)

# Base class for all the models.
Base = declarative_base()
