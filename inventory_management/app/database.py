from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://db_postgresql_k4h6_user:yvSo36ZlE57JYk9NhFbG2kwzpfqj9F1S@dpg-crc0frbv2p9s73dl0akg-a.oregon-postgres.render.com/db_postgresql_k4h6" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
