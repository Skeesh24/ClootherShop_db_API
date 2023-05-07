from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from utils.configuration import SQLALCHEMY_DATABASE_URL
from sqlalchemy.orm import sessionmaker


# ====== export ====== #
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()
base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# ==================== #


metadata.create_all(bind=engine)
