from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from models.model import Users, Issues, Comments, db
import time
from auth.auth import generate_jwt_token, admin_login_required, user_login_required, login_required
from resources.users import User
import bcrypt
class Login(Resource):
    def post(self):
        data = request.get_json(force=True)
        email = data['email']
        password = data['password']
        user = Users.query.filter_by(email = email).limit(1).all()
        if not user:
            abort(401)
        user_data = {}
        for x in user:
            if x.password !=password:
                abort(401)
            user_data.update({
                    "name": x.full_name,
                     "role": x.role
            })
        token = generate_jwt_token(user_data)
        return jsonify({
            "token": token
        })