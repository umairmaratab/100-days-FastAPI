Now to use that dictionary we can do:
@app.get("/posts")
def get_posts():
    return {"data": my_posts}

Now to create posts, we will append our post inside the array of
list we created.
See @app.post("/posts) path operation.
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
    # printing and converting pydantic model to dict
    my_posts.append(post_dict)
    return {"data": post_dict} # when we create a new post we will return that post

# GET particular post
@app.get("/posts/{id}")

# A method will be created to find the post and that method will return that particualr post.
and we will respond with the proper message.
# Make sure that both have same types when calling with id.
but we can validate it by defining id type in path operation function like this:
@app.get("/posts/{id}")
def get_post(id: int):


