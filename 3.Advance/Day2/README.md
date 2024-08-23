# Cleaning up 
- Cut the get_db function code from main.py file and add it into our database.py file.
- Then import get_db in main.py, also we can remove that SessionLocal import statement

--> To verify things, delete the table once again and run the uvicorn server and check the db

- One thing also need to change is that this won't work: `publised = Column(Boolean, default=True)`, change this to `server_default='TRUE'`

if you save this and reload the server, nothing will change in the db but why?
- it is because sqlalchemy works this way, before creating the table it checks if a table already exists or not, if yes it won't create a new table or update it. that's what the documentation says.

- For now to get over this, we will go for a work around which is we delete the previous table and run the server again.

--> Now let's add the timestamp column for post creation time as created_at.
`
created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
`
Add this line in the Post class inside models.py

Now before start making queries inside our path operations let's edit our /sqlalchemy path operation we created recently just to test things.

```
@app.get("/sqlalchmey")
def test_posts(db: Session = Depends (get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}
```
This will return the posts we have in our db.

To check the workings that what ORM is doing let's make one change

```
@app.get("/sqlalchmey")
def test_posts(db: Session = Depends (get_db)):
    posts = db.query(models.Post)
    print(posts)
    return {"data": "Successfull"}
```

The above path operation function will return you an sql query which will be:

```
SELECT posts.id AS posts_id, posts.title AS posts_title, posts.content AS posts_content, posts.publised AS posts_publised, posts.created_at AS posts_created_at 
FROM posts
```