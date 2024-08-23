# Creating Posts
Now we will edit app.post, path operation.
### Posts can be created like this:
* Method 1
```
# post request
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post): 
    cur.execute(f"INSERT INTO posts (title, content, published) VALUES({post.title}, {post.content}, {post.published})")
    new_post = cur.fetchone()

    # we have to commit otherwise changes won't be saved to our database
    # conn.commit() # commit is used with our connection variable
    return {"data": new_post}
```

#### Problems with Method 1
- This is vulnerable to SQL injection attack, someone can inject sql command with that method

* Method 2
```
# post request
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post): 
    cur.execute("""INSERT INTO posts(title, content, published) WITH VALUES (%s, %s, %s)""", (post.title, post.content, post.published)) # %s indicates that it will be a variable
    new_post = cur.fetchone()

    # we have to commit otherwise changes won't be saved to our database
    # conn.commit() # commit is used with our connection variable
    return {"data": new_post}
```

#### How Method 2 solved our problem
- Using %s (each value is considered as a variable) we are actually senatizing the input so this way someone cannot pass the sql command.