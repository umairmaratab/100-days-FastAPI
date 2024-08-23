# Structuring project
Create new directory with name app
Make app a python package by creating a __init__.py file inside the directory.

# Using Database
- Database is a collection of organized data that can be easily accessed and managed.
- we din't work or interact with databases directly.
- Instead we make use of a software referred to as a Database Management System (DBMS).

## NOw after learning the basics of SQL
Now we will interact with our database from our application for which we require a driver, which you can install with `pip install psycopg[binary]`

## Connect with DB
### Method 1
```
while True:
# Connect to DB
    try:
        # Connect to an existing database
        with psycopg.connect(host = 'localhost', dbname='fastapi', user='postgres',
                                    password='password123') as conn:
            # Open a cursor to perform database operations
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM posts")
        break
    except Exception as error:
        print("Connecting to database failed")
        print(f"Error:", error)
        time.sleep(2)
```

### Method 2
while True:
### Connect to DB
```
    try:
        # Connect to an existing database
        conn = psycopg.connect(host = 'localhost', dbname='fastapi', user='postgres',
                                    password='password123')
            # Open a cursor to perform database operations
            # with conn.cursor() as cur:
            #     cur.execute("SELECT * FROM posts")
        cur = conn.cursor()
        break
    except Exception as error:
        print("Connecting to database failed")
        print(f"Error:", error)
        time.sleep(2)
```
If you forget the password of postgres, you can reset it via following commands:
`sudo -i -u postgres`
`psql`
`ALTER USER username WITH PASSWORD 'newpassword';`
`\q`
if needed `sudo systemctl reload postgresql`

- If you note our way of connecting with db is very bad and dangerous, we are actually passing username and password in our code (Never do this).

But we will keep this simple for now and keep this as it is.
