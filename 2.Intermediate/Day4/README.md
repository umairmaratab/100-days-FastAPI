# Getting a specific post
```
@app.get("/posts/{id}")
def get_post(id: int):
    cur.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
    post = cur.fetchone()

```
This query will find the post for us and again we must use %s and convert the id into str (otherwise error will be raised.)
