# Working with sqlalchemy
- Inside app directory create a new file as database.py
paste this code insid database.py
```
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

```

- After that we have to define our tables. we can define the tables as Python Models.
- Create a new file as models.py

### Creating a model
paste this code inside models.py
```
from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class Post(Base):
    __tablename__  = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)

```

 - Then add this line inside the main.py file:
```
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```
After doing that inside your path operation functions, add this parameter:
`db:Sesssion = Depends(get_db)`

--> Add dependencies in the main file where required.

Install `psycopg2` if needed with:
`pip install psycopg2`

To do's:
- Delete the posts table from DB
- Run the uvicorn server
- Check the db again, you will see the posts table created again because of this line `models.Base.metadata.create_all(bind=engine)` we have in our main.py file.
