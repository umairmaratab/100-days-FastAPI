from random import randrange
from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
import psycopg
import time
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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

@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # cur.execute("""SELECT * FROM posts""")
    # posts = cur.fetchall()
    # print(posts)
    posts = db.query(models.Post).all()
    return posts


# post request
@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)): 
    # cur.execute("""INSERT INTO posts(title, content, published) VALUES (%s, %s, %s) RETURNING * """, 
    #             (post.title, post.content, post.published)) # %s indicates that it will be a variable

    # new_post = cur.fetchone()

    # # we have to commit otherwise changes won't be saved to our database
    # conn.commit() # commit is used with our connection variable
    
    new_post = models.Post(**post.dict())
    db.add(new_post) # Add the post
    db.commit() # commit it to make/save changes in db
    db.refresh(new_post) # to return the post back like RETURNING * does

    return new_post

# what if a post with certain id does not exist, we will change Response to handle that case
@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    # cur.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
    # post = cur.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id: {id} not found!')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f'Post with id: {id} not found!'}
    return post

# delete post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db: Session = Depends(get_db)):
    # cur.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    # deleted_post = cur.fetchone()
    # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Could not delete, as post with id: {id} not found!')

    post.delete(synchronize_session=False)
    db.commit()
    # when something is deleted you don't send data back that's what fastapi says
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# update post by id
@app.put("/posts/{id}")
def update_post(id:int, updated_post:schemas.PostCreate, db:Session = Depends(get_db)):
    # cur.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
    #             (post.title, post.content, post.published, str(id)))
    # updated_post = cur.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Could not update, as post with id: {id} not found!')
    
    # post_query.update({'title': 'This is the updated title'}, synchronize_session=False)

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()
