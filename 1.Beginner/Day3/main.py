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
@app.get("/")
def root():
    return {"message": "welcome to my API"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}


# post request
@app.post("/posts")
def create_posts(post: Post):
    print(post.rating)
    # printing and converting pydantic model to dict
    print(post.dict())
    return {"data": post}
