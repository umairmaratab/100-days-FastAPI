CRUD 
CREATE --> POST
READ   --> GET
UPDATE --> PUT/PATCH
DELETE --> DELETE

/home/mr-robot/Pictures/Screenshots/Screenshot from 2024-08-05 13-18-53.png

--> Standard convention for API's is to use plural.
like using /posts instead of /post.

# Storing the Data
we can store data in a DB but that will be covered in later sections of the course.
For now we will use a list/array of dictionaries to store our posts.
Example:
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title":
                                                                                    "favorite series", "content": "RandomData", "id": 2}]
                                                        