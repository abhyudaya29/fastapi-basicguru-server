from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

from helpers.logger import logger
load_dotenv()

database_url=os.getenv('POSTGRES_URL')
print ('Database URL: %s' % database_url)

engine=create_engine(database_url)
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base()

def get_db():
    db=SessionLocal()
    logger.info("Connection establish with databse")
    try:
        yield db
    finally:
        db.close()