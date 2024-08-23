# Delete Specific Path Operation
```
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

```

# Updating Particular post
```
# update post by id
@app.put("/posts/{id}")
def update_post(id:int, updated_post:Post, db:Session = Depends(get_db)):
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

    return {"data": post_query.first()}

```

## we have two models
1. **Schema Models/Pydantic Models**
- define the structure of a request and response.
- This ensures that when a user wants to create a post, the request will only go 
though if it has a 'title' and 'content' in the body 
- It is for validations, it is for schema defination to make sure request is following a valid schema.

- Example:
```
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

```

- It is used in our path operation functions like here:
```
# post request
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db: Session = Depends(get_db)): 
```

2. **SQLALCHMEY MODEL**
- Responsible for defining the columns of our "posts" table within postgres
- is used to query, create, delete and update entries within the database.

- Example:
`new_post = models.Post(**post.dict())`
