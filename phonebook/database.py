from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCEMY_DATABASE_URL = 'sqlite:///./phonebook.db'

engin = create_engine(SQLALCEMY_DATABASE_URL, connect_args={
    "check_same_thread": False
})
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engin)

Base = declarative_base()
