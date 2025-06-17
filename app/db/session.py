# app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # ister PostgreSQL yaparsın sonra

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # sqlite için
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
