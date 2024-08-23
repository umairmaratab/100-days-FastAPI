from random import randrange
from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
import psycopg
import time
from sqlalchemy.orm import Session
from . import models
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

while True:
# Connect to DB
    try:
        # Connect to an existing database
        conn = psycopg.connect(host = 'localhost', dbname='fastapi', user='postgres',
                                    password='password123')
            # Open a cursor to perform database operations
            # with conn.cursor() as cur:
            #     cur.execute("SELECT * FROM posts")
        cur = conn.cursor()
        break
    except Exception as error:
        print("Connecting to database failed")
        print(f"Error:", error)
        time.sleep(2)
    # conn = psycopg.connect(host = 'localhost', database='fastapi', user='postgres',
    #                         password='password123')
    
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title":
                                                                                    "favorite series", "content": "RandomData", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def root():
    return {"message": "welcome to my API"}

@app.get("/sqlalchmey")
def test_posts(db: Session = Depends (get_db)):
    return {"status": "success"}

@app.get("/posts")
def get_posts():
    cur.execute("""SELECT * FROM posts""")
    posts = cur.fetchall()
    # print(posts)
    return {"data": posts}


# post request
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post): 
    cur.execute("""INSERT INTO posts(title, content, published) VALUES (%s, %s, %s) RETURNING * """, 
                (post.title, post.content, post.published)) # %s indicates that it will be a variable

    new_post = cur.fetchone()

    # we have to commit otherwise changes won't be saved to our database
    conn.commit() # commit is used with our connection variable
    return {"data": new_post}

# what if a post with certain id does not exist, we will change Response to handle that case
@app.get("/posts/{id}")
def get_post(id: int):
    cur.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
    post = cur.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id: {id} not found!')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f'Post with id: {id} not found!'}
    return {"post_detail": post}

# delete post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, response: Response):
    cur.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cur.fetchone()
    conn.commit()

    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Could not delete, as post with id: {id} not found!')

    # when something is deleted you don't send data back that's what fastapi says
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# update post by id
@app.put("/posts/{id}")
def update_post(id:int, post:Post):
    cur.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
                (post.title, post.content, post.published, str(id)))
    updated_post = cur.fetchone()
    conn.commit()

    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Could not update, as post with id: {id} not found!')
    
    return {"data": updated_post}
