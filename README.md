# Bug Tracker API Documentation
## Environemnt Setup & Setting up the Backend
### Python Installation 
If you Don't have installed Python yet, please go here and itstall it. 
https://docs.python.org/3/using/unix html#getting-and-installing-the-latest-version-of-python)

### Creating Virtual Environemnt 
  **Creating Virtual Environment on Linux** - 
  ```bash
python3 -m venv venv
```
  **Activating Virtual Environment on Linux** - 
  ```bash
source venv/bin/activate
```
 **Creating Virtual Environment on Windows** - 

### Installing Dependencies
  all required packages are found in requirements.txt. so, after switching to your vertual environemtn, run the following command to install all required packages 

  ```bash
  pip install -r requirements.txt
  ```
### Set up the Database
connect to your postgres database engine and run the following command to create the database.

```bash
createbd bug_tracker
```
### Importing demo data to the Database
If you want to have a demo data in the newly created DB, you can run the following command. The demo DB file located under this directory. 

```bash
psql bug_tracker < bug_tracker.psql
```
### Exporting Environment Variables 
In order to run this flask API, please run the following command to store your root app to environemnt variable 
```bash

export SECRET_KEY="testsecret"
export ALGORITHM="HS256"
export DB_HOST=localhost:5432
export DB_USER=postgres
export DB_PASSWORD=123456
export DB_NAME=bug_tracker
```
### Run the Server

To run the server, execute:

```bash
    flask run
```
or 
```bash
    python3 app.py
```
### API Description 
### Endponints accessed by GET Method 
  1.  /users
      - gets list of registered users
      - Request Arguments: None
      - Returns JSON data like the following format 
      ```json
              
             {
                "address": "Adis Ababa",
                "created_at": "unix timestamp will be here",
                "email": "test@gmail.com",
                "full_name": "Abe Kebe",
                "id": 1,
                "last_login": "unix timestamp will be here",
                "nik_name": "",
                "password": "dfgdSDFDGFGBgh57624235",
                "position": "",
                "role": "admin",
                "updated_at": "unix timestamp will be here",
                "user_name": "unix timestamp will be here"
         },
        {
        "address": "Adis Ababa",
            "created_at": "unix timestamp will be here",
            "email": "test2@gmail.com",
            "full_name": "Abe Kebe",
            "id": 2,
            "last_login": "unix timestamp will be here",
            "nik_name": "",
            "password": "dfgdSDFDGFGBgh57624235",
            "position": "",
            "role": "user",
            "updated_at": "unix timestamp will be here",
            "user_name": "unix timestamp will be here"
        }.............

  2. /get a user
      - gets a single user based on user id. 
          - Request Arguments: User ID
          - Returns JSON data like the following format 
          ```json
             {
                "address": "Adis Ababa",
                "created_at": "unix timestamp will be here",
                "email": "test@gmail.com",
                "full_name": "Abe Kebe",
                "id": 1,
                "last_login": "unix timestamp will be here",
                "nik_name": "",
                "password": "dfgdSDFDGFGBgh57624235",
                "position": "",
                "role": "admin",
                "updated_at": "unix timestamp will be here",
                "user_name": "unix timestamp will be here"
             },
  3. /issues/<int:issue_id>
  4. /issues
  5. /comments
  6. /comments/<int:comment_id>
### Endponints accessed by POST Method 
 ...

### Endponints accessed by PUT Method 
...

### Endponints accessed by DELETE Method 