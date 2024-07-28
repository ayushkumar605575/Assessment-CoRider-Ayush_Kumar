# Flask Application
A Flask-based backend application


## Setup Instructions
1. Install the required libraries by running the command `pip install -r requirements.txt`.
2. Install mongodb database.
2. Run `docker-compose up --build` file to setup a network in docker and run the server.
4. Use `Postman` to send requests to the server


## Endpoints
1. GET `/users` -> Get all users
2. POST `/users` -> Add new users
3. GET `/users/<id>` -> Get specific user by id
4. PUT `/users/<id>` -> Update user by id
5. DELETE `/users/<id>` -> Delete user by id