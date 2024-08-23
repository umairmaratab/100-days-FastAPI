In the Day1, basic path creation is covered.
Path operation:
All code for a specific path is called path operation.
Function used inside a path operation is called path operation function.

In this directory 2 GET methods were created:
Both prints some random text.

After that Postman is setup which is used for API Testing.
GET VS POST
IN GET request, you send request to API server and it sends some data back.
In POST request, you send some data to API server and API server also sends data back.

2 Main methods were created:
--> @app.get("/posts") to get posts
--> @app.post("/createposts") to create posts
In post method we send data in the body of the request, we can use Postman to do that by sending
data as json or any other format.
e.g
{
    "title": "Linux",
    "Description": "Linux is open source"
}
How are we going to extract the data we sent using path operation
In path operation function you can do:
def create_posts(payload: dict = Body(...)) # payload is just a variable name
This Body(...) is built into FastAPI, and it take all fields from body and convert it to dict
