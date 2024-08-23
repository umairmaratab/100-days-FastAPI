from random import randrange
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title":
                                                                                    "favorite series", "content": "RandomData", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
def root():
    return {"message": "welcome to my API"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}


# post request
@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
 
    my_posts.append(post_dict)
    return {"data": post_dict}


# # Request to get a particular post
# @app.get("/posts/{id}")
# def get_post(id):
#     print(id)
#     return {"post": f"Here is the post {id}"}


# Request to get a particular post using function
# Add function below the pydantic model
# @app.get("/posts/{id}")
# def get_post(id):
#     post = find_post(int(id))
#     return {"post_details": post}


# Request to get a particular post using function
# Add function below the pydantic model
# @app.get("/posts/{id}")
# def get_post(id):
#     post = find_post(int(id))
#     return {"post_details": post}


# Request to get a particular post
@app.get("/posts/{id}")
def get_post(id: int): # using int, the passed paramter will automatically be converted to int
    post = find_post(id)
    return {"post": f"Here is the post {id}"}
