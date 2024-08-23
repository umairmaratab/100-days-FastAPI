# Refining /post
we are doing this to get values:
`new_post = models.Post(title = post.title, content=post.content, published=post.published)`

what if we have 100 of this type of fields, this would be very tedious work so let's solve this problem using 
(**post.dict())
- post.dict() will convert the body to dictionary.
- ** will make it work like title=post.title, content = post.content -------------------!


# Handling specific Queries
Now we will handle querying specific posts i.e @app.get(/posts/{id})

```
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
    return {"post_detail": post}

```
we have used `.first()` because anytime we know we have just one match we will use `first()` so search should stop at that point.

