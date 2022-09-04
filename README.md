# Bug Tracker Backend Documentation

### This is a bug tracker project with flask backend and React frontend 
## Project Description 

This is a bug tracker api which allows to track bugs or tasks and assigning them to the available personnel. this is python (Flask) backend for the bug tracker project. this project has the following list of functionalities 

- Admin
  - Register & Manage Users, Register & Manage Issues, Assign Issues to Users, Track progress, Manage comments added to issues e.t.c
- Users
  - View All issues, manage issues assigned to them, track isue progress, add comment on issues e.t.c
- Postman collection link:- https://www.getpostman.com/collections/eb09dcb58ba86c7b7e8c
## Environemnt Setup 
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
psql bug_tracker < bug_tracker.sql
```
- Alternatively, you can create at once all required tables using flask migrate, but you will not find any demo data
  - follow the following command to apply flask migrate
```bash
flask db init 
flask db migrate
flask db upgrade
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
      - Allowed Users: @Admin
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

  2. /get/<int:user_id>
     - Allowed Users: @Admin, @User
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
   - Allowed Users: @Admin, @User
   - gets a single Issue (Task)  based on task id. 
   - Request Arguments: Issue ID
   - Returns JSON data like the following format 
   ```json
             {
                "assigned_date": "1662124444.2369049",
                "assignee": "Muluken",
                "category": "Bug",
                "created_at": "1662124444.2369049",
                "descriprion": "test descriprion",
                "due_date": "1662124444.2369049",
                "id": 1,
                "name": "Javascript Bug on Landing Page",
                "priority": "high",
                "solved_date": "1662124444.236909",
                "updated_at": "1662124444.2369113"
             }
4. /issues
   - Allowed Users: @Admin, @User
   - gets list of all registered issues. 
   - Request Arguments: None
   - Returns JSON data like the following format 
   ```json
         {
                      "assigned_date": "1662124444.2369049",
                      "assignee": "Muluken",
                      "category": "Bug",
                      "created_at": "1662124444.2369049",
                      "descriprion": "test descriprion",
                      "due_date": "1662124444.2369049",
                      "id": 1,
                      "name": "Javascript Bug on Landing Page",
                      "priority": "high",
                      "solved_date": "1662124444.236909",
                      "updated_at": "1662124444.2369113"
                  },
                      {
                        "assigned_date": "1662124444.2369049",
                        "assignee": "test user",
                        "category": "Bug",
                        "created_at": "1662124444.2369049",
                        "descriprion": "test descriprion",
                        "due_date": "1662124444.2369049",
                        "id": 2,
                        "name": "Javascript Bug on Landing Page",
                        "priority": "Low",
                        "solved_date": "1662124444.236909",
                        "updated_at": "1662124444.2369113"
                  },
            
5. /comments
   - Allowed Users: @Admin, @User
   - gets list of comments (discussions) on all available tasks. 
   - Request Arguments: None
   - Returns JSON data like the following format 
   ```json
            {
                "content": "test comment",
                "id": 2,
                "issue_id": 1,
                "user_id": 1
            },
              {
                "content": "sample comment",
                "id": 1,
                "issue_id": 5,
                "user_id": 2
            }
              
6. /comments/<int:comment_id>
   - Allowed Users: @Admin, @User
   - gets a specific comment using coment ID 
   - Request Arguments: Comemnt ID
   - Returns JSON data like the following format 
   ```json
              {
                      "content": "test comment",
                      "id": 2,
                      "issue_id": 1,
                      "user_id": 1
                  }
### Endponints accessed by POST Method 
1. /users 
   - Allowed Users: @Admin
   - adds users to the DB
   - Request Arguments: 
   ```json
         {
            "full_name" : "Abe",
            "nik_name" : "kebe",
            "email" : "test@gmail.com",
            "address": "ET",
            "position": "Junior Developer",
            "role": "admin",
            "user_name": "abe",
            "password": "1234"
        }
   ```
    - Returns JSON data like the following format 
    ```json
           {
        "code": 201,
        "message": "user registered"
      }
    ```
2. /issues 
  - Allowed Users: @Admin
  - adds issues to the DB
  - Request Arguments: 
  ```json
          {
            "name": "test issue",
            "descriprion": "test",
            "category": "test category",
            "priority": "high",
            "due_date": "11-05-17"
       }
  ```

  - Returns JSON data like the following format 
  ```json
           {
        "code": 201,
        "message": "Issues registered"
      } 
  ```
3. /comments 
  - Allowed Users: @Admin
  - adds a comment on a specific issue
  - Request Arguments: 
  ```json
          {
          "content": "test comment",
          "issue_id": 1,
          "user_id": 1
       } 
  ```
  - Returns JSON data like the following format 
  ```json
           {
        "code": 201,
        "message": "comment added"
      }
  ```
4. /login 
  - Auth endpoint
  - Request Arguments: 
  ```json
          {
        "username":"test@gmail.com",
         "password":"1234"
       }
  ```
  - Returns JSON data like the following format 
  ```json
           {
          "userData": ["user name", "role"...],
          "token": "this is jwt token"
      }
  ```
### Endponints accessed by PUT Method 

1. /users/<int:user_id> 
  - Allowed Users: @Admin
  - updates user details using user ID
  - Request Arguments: 
  ```json
          {
        "full_name" : "Abe",
        "nik_name" : "kebe",
        "email" : "test@gmail.com",
        "address": "AA",
        "position": "Support",
        "role": "user",
        "user_name": "abe",
        "password": "123456"
       } 
  ```
  - Returns JSON data like the following format 
  ```json
           {
        "code": 200,
        "message": "user updated"
      }
  ```
2. /issues<int:issue_id> 
  - Allowed Users: @Admin
  - updates issue details using issue ID
  - Request Arguments: 
  ```json
          {
        "name": "issue test",
        "descriprion": "test descriprion",
        "category": "test category",
        "priority": "high",
        "due_date": "11-05-17",
        "assignee": "Mule"
       } 
  ```
  - Returns JSON data like the following format 
  ```json
           {
        "code": 200,
        "message": "issue updated"
      }
  ```
3. /comments<int:comment_id> 
  - Allowed Users: @Admin
  - updates issue details using comment ID
  - Request Arguments: 
  ```json
          {
        "content": "test comment",
        "issue_id": 1,
        "user_id": 1
       } 
  ```
  - Returns JSON data like the following format 
  ```json
           {
        "code": 200,
        "message": "comment updated"
      }
  ``` 
### Endponints accessed by DELETE Method 

1. /users<int:user_id> 
  - Allowed Users: @Admin
  - deletes users using user ID
  - Request Arguments: None
  - Returns JSON data like the following format 
  ```json
           {
        "code": 200,
        "message": "user deleted"
      }
  ```
2. /issues<int:issue_id> 
  - Allowed Users: @Admin
  - deletes issues using issue ID
  - Request Arguments: None
  - Returns JSON data like the following format 
  ```json
           {
        "code": 200,
        "message": "issue deleted"
      }
  ```
3. /comments<int:comment_id> 
  - Allowed Users: @Admin
  - deletes comments using commenr ID
  - Request Arguments: None
  - Returns JSON data like the following format 
  ```json
           {
        "code": 200,
        "message": "comment deleted"
      }
  ```