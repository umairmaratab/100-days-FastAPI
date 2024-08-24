# Sending Response Back
we can also define what a response should like so we are now going to create a pydantic model for the response so we can define how a response is going to look like.

So far what we were doing was to send the user data back after an operation but let's say we logged a user into the system we don't want to return the user his password back.

# Cleanings
Let's clean the data we have, let's delete the `data` from the return statements.
So from this `return {"data": posts}` to this `return posts`.

# Creating pydantic model for response
```

class Post(BaseModel):
    title: str
    content: str
    published: bool

```

This the model for response, it's different from the PostBase Model in a way that now it will only show these particular fields not the other fields like we have `id` and `created_at`.

# Edit app.post path operation accordingly
### Before:
```
@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
```

### After
```
@app.post("/posts", status_code=status.HTTP_201_CREATED)
```
Then send the request to verify the updated response.
