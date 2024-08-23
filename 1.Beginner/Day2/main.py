from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message": "welcome to my API"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}


# post request
# @app.post("/createposts")
# def create_posts(post: Post):
#     print(post.rating)
#     # printing and converting pydantic model to dict
#     print(post.dict())
#     return {"data": post}

# Best practice is to always use plurals in the url pattern and use a 
# single word to describe it like posts (It's plural and a single word too)

@app.post("/posts")
def create_posts(post: Post):
    print(post.rating)
    # printing and converting pydantic model to dict
    print(post.dict())
    return {"data": post}
