from random import randrange
from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
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

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def root():
    return {"message": "welcome to my API"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}


# post request
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
    # printing and converting pydantic model to dict
    my_posts.append(post_dict)
    return {"data": post_dict}

# what if a post with certain id does not exist, we will change Response to handle that case
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id: {id} not found!')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f'Post with id: {id} not found!'}
    return {"post_detail": post}

# delete post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, response: Response):
    # deleting post
    # find the index in the array that has required ID
    # my_post.pop(index)
    
    index = find_index_post(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Could not delete, as post with id: {id} not found!')
    my_posts.pop(index)
    # when something is deleted you don't send data back that's what fastapi says
    return Response(status_code=status.HTTP_204_NO_CONTENT)
