Ordering matters, like /posts/latest path operation is placed under the /posts then /posts will always be used as /posts/latest is covered in /posts.

Another solution could be change the URL e.g /posts/r/latest

# Handling unknown id cases
let's execute this /posts/3 (post with id 3 does not exist), API will respond with:
"post_detail": null

This is a bad UX so we will change this, handle exceptions for doing that we can change our code to:
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f'Post with id: {id} not found!'}
    return {"post_detail": post}

- Response is used in our above path operation function which will give us access to response status code and we will use exceptions here like:
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f'Post with id: {id} not found!'}
    return {"post_detail": post}

- status is used to access the response codes so we don't have to harcode the numbers there.

but instead of raising our custom exception we can use HTTPExceptions like we have in 3-main----.py file.

In 4-change-status-code---.py file we changed the status code return to 201 for CREATED which is recommeneded for creation case.
like this:
@app.post("/posts", status_code=status.HTTP_201_CREATED)

