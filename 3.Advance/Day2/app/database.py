from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password123@localhost/fastapi'

# engine is responsible for connecting SQLALCHEMY with the sql database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# To talk to database we use session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()