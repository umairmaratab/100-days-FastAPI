Issues with the Day 1 setup:
--> Hard to get all the values from the body
--> The client can send whatever data they want.
--> The data isn't getting validated

Solution:
we will enforce user for a schema that we expect, we can do that
using pydantic Models.
e.g
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None