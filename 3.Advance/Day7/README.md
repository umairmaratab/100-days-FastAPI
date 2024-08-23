# Inheritance Use
### Using Inheritance instead of creating new models as same
- Let's update the schemas.py and change it to:
```
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

```

Now change main.py file accordingly i.e change this `schemas.Post` to this `schemas.PostCreate`.

- Also remove /sqlalchemy test route.
