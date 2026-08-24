from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv
import os 

load_dotenv()

# sqlite db
DATABASE_URL = os.getenv("DATABASE_URL")

# create database engine 
engine = create_engine(DATABASE_URL)

# create a local database session 
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
# Base class for SQLAlchemy models
Base = declarative_base()

# DB denpendency function 

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()