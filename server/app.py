#!/usr/bin/env python3

from flask import request, session
from flask_restful import Resource

from config import app, db, api
from models import User, UserSchema


# Clears all session data used by the application.
# Useful for testing and resetting authentication state.
class ClearSession(Resource):

    def delete(self):

        session['page_views'] = None
        session['user_id'] = None

        return {}, 204


# Creates a new user account.
# Hashes the password, saves the user to the database,
# logs the user in, and returns the user as JSON.
class Signup(Resource):

    def post(self):
        data = request.get_json()

        user = User(
            username=data['username']
        )

        user.password_hash = data['password']

        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id

        return UserSchema().dump(user), 201


# Authenticates an existing user.
# Verifies the username and password, stores the user's
# id in the session, and returns the user as JSON.
class Login(Resource):

    def post(self):
        data = request.get_json()

        user = User.query.filter_by(
            username=data['username']
        ).first()

        if user and user.authenticate(data['password']):
            session['user_id'] = user.id
            return UserSchema().dump(user), 200

        return {}, 401


# Checks whether a user is currently authenticated.
# Returns the user object if a valid session exists,
# otherwise returns an empty response.
class CheckSession(Resource):

    def get(self):
        user = User.query.filter_by(
            id=session.get('user_id')
        ).first()

        if user:
            return UserSchema().dump(user), 200

        return {}, 204


# Logs a user out by removing their session information.
# Returns a 204 status code after logout.
class Logout(Resource):

    def delete(self):
        session['user_id'] = None
        return {}, 204


api.add_resource(ClearSession, '/clear', endpoint='clear')
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Logout, '/logout')


if __name__ == '__main__':
    app.run(port=5555, debug=True)