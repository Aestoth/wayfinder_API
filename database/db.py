import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import sessionmaker


load_dotenv()

DB_TYPE = os.getenv('DB_TYPE')
DBHOST = os.environ['DBHOST']
DBPORT = os.environ['DBPORT']
DATABASE = os.environ['DATABASE']
DBUSER = os.environ['DBUSER']
DBPASSWORD = os.environ['DBPASSWORD']

SQLALCHEMY_DATABASE_URI = f"postgresql://{DBUSER}:{DBPASSWORD}@{DBHOST}:{DBPORT}/{DATABASE}"
engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_size=20, echo=True)


Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base() 
