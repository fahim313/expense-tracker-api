from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker,declarative_base

# sqlite db
DATABASE_URL = "sqlite:///./expense_tracker.db"

# create database engine 
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# create a local database session 
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
# Base class for SQLAlchemy models
Base = declarative_base()
