# Flask Password Protection Lab

## Overview

This project demonstrates user authentication and password protection using Flask, SQLAlchemy, Flask-Bcrypt, and Flask sessions.

The application allows users to:

* Create accounts with secure password hashing
* Log in using a username and password
* Maintain authentication state with sessions
* Log out and clear session data
* Verify active user sessions

## Technologies Used

* Python
* Flask
* Flask-RESTful
* Flask-SQLAlchemy
* Flask-Bcrypt
* Flask-Migrate
* Marshmallow
* SQLite

## Features

### User Signup

Creates a new user account and securely hashes the user's password before storing it in the database.

### User Login

Authenticates a user by comparing the submitted password against the stored password hash.

### Session Authentication

Stores the authenticated user's ID in the Flask session and allows session validation through the `/check_session` endpoint.

### User Logout

Removes the authenticated user's session information and logs the user out.

## Password Security

Passwords are never stored in plain text.

The application uses Flask-Bcrypt to:

* Generate password hashes during signup
* Verify passwords during login
* Prevent direct access to stored password hashes

## API Routes

| Method | Route          | Description            |
| ------ | -------------- | ---------------------- |
| POST   | /signup        | Create a new user      |
| POST   | /login         | Authenticate a user    |
| GET    | /check_session | Verify current session |
| DELETE | /logout        | Log out current user   |
| DELETE | /clear         | Clear session data     |

## Testing

Run the test suite with:

```bash
pipenv run python -m pytest
```

All provided tests pass successfully.

