# Make schema seprate from the code
- Let's put the schema in a different file, create a new files as `schemas.py`, cut the `Post` class from `main.py` and paste it in `schemas.py` 
- After doing that import schemas inside the main.py with
`from . import schemas`
- Now where we are using Post, we have to replace it with `schemas.Post`, which is in create_post and update_post path operation function.

# Create New Models
- create 2 new models, 1 for create post and 1 for update post.

Then schemas.py would like this:
```
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

class CreatePost(BaseModel):
    title: str
    content: str
    published: bool = True

class UpdatePost(BaseModel):
    title: str
    content: str
    published: bool = True
```

#### But why we did this, where we need this?
Well there may be case where you only want user to update the published but not the title and content so when you have a different model for it you can just change that model and it will work like this:
```
class UpdatePost(BaseModel):
    published: bool = True
```
