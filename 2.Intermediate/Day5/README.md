# Deleting posts
```
# delete post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, response: Response):
    cur.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cur.fetchone()
    conn.commit()

    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Could not delete, as post with id: {id} not found!')

    # when something is deleted you don't send data back that's what fastapi says
    return Response(status_code=status.HTTP_204_NO_CONTENT)

```

# Updating Post
```
def update_post(id:int, post:Post):
    cur.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
                (post.title, post.content, post.published, str(id)))
    updated_post = cur.fetchone()
    conn.commit()

    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Could not update, as post with id: {id} not found!')
    
    return {"data": updated_post}
```