# Edit our Path Operations to use ORM
let's start with /posts
```
@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # cur.execute("""SELECT * FROM posts""")
    # posts = cur.fetchall()
    # print(posts)
    posts = db.query(models.Post).all()
    return {"data": posts}
```

--> Let's now work on create post i.e @app.post("/posts ------------")
```
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db: Session = Depends(get_db)): 
    # cur.execute("""INSERT INTO posts(title, content, published) VALUES (%s, %s, %s) RETURNING * """, 
    #             (post.title, post.content, post.published)) # %s indicates that it will be a variable

    # new_post = cur.fetchone()

    # # we have to commit otherwise changes won't be saved to our database
    # conn.commit() # commit is used with our connection variable
    new_post = models.Post(title = post.title, content=post.content, published=post.published)
    db.add(new_post) # Adding post
    db.commit()
    db.refresh(new_post)
    
    return {"data": new_post}
```