# ORM
- Object Relational Mapper is a layer of abstraction that sits between the database and us
- We can perform all DB operations through traditional python code. No more SQL!

Python code will be used and that will be converted into SQL by ORM.

### What can an ORM do:
Instead of manually defining tables in postgres, we can define our tables as python models

Queries can be made exclusively through python code. No SQL is necessary.

e.g
```
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean)
```
- To execute:
``` db.query(models.Post).filter(models.Post.id == id).first() ``` 

# SQLALCHEMY
- Sqlalchemy is one of the most popular python ORMs
- It is standalone libray and has no association with FastAPI. It can be used with any other python web frameworks or any python based application.


## SQLALCHEMY Setup
- Install sqlalchemy with `pip install sqlalchemy`
- To talk to any DB we need a driver so make sure psycopg is installed.


