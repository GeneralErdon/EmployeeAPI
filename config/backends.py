from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv
import os

from utils.utils import BASE_DIR

load_dotenv(BASE_DIR / ".env")

DB_ENGINE:str = os.environ.get("DB_ENGINE", "sqlite")

if DB_ENGINE == "sqlite":
    SQLALCHEMY_DATABASE_URL = "sqlite:///empleados.db"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    
if DB_ENGINE == "postgresql":
    SQLALCHEMY_DATABASE_URL = "postgresql://{user}:{password}@{host}/{db_name}"\
        .format(
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            host=os.environ.get("DB_HOST"),
            db_name=os.environ.get("DB_NAME")
            )
    engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()