from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from models.model import Users, Issues, Comments, db
import time
import bcrypt
from auth.auth import admin_login_required, user_login_required, login_required
class User(Resource):
    @admin_login_required
    def post(self, payload):
        data = request.get_json(force=True)
        full_name = data['full_name']
        nik_name = data['nik_name']
        email = data['email']
        address = data['address']
        position = data['position']
        role = data['role']
        user_name = data['user_name']
        password = data['password']
        #last_login = data['last_login']
        created_at = time.time() #data['created_at']
        updated_at = time.time()#data['updated_at']
        user = Users(full_name=full_name, nik_name=nik_name, email=email, address=address, position=position, role=role,
        user_name=user_name, password=password, created_at=created_at, updated_at=updated_at)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message":"user added","code":201})
    @admin_login_required
    def get(self, payload):
        data = Users.query.all()
        users = []
        for d in data:
            users.append({
                "id":d.id,
                "full_name" : d.full_name,
                "nik_name" :d.nik_name,
                "email" :d.email,
                "address" :d.address,
                "position" :d.position,
                "role" :d.role,
                "user_name" :d.user_name,
                "password" :d.password,
                "last_login" :d.last_login,
                "created_at" :d.created_at,
                "updated_at" :d.updated_at,
            })
        
        return jsonify(users)
    def put(self):
        return "put test"
    def delete(self):
        return "delete test"
class UserList(Resource):
    @login_required
    def get(self, id, payload):
        d = Users.query.get(id)
        user = []
        user.append({
                 "id":d.id,
                "full_name" : d.full_name,
                "nik_name" :d.nik_name,
                "email" :d.email,
                "address" :d.address,
                "position" :d.position,
                "role" :d.role,
                "user_name" :d.user_name,
                "password" :d.password,
                "last_login" :d.last_login,
                "created_at" :d.created_at,
                "updated_at" :d.updated_at,
            })
        return jsonify(user)
    @admin_login_required
    def put(self, id, payload):
        data = request.get_json(force=True)
        user = Users.query.get(id)
        user.full_name = data['full_name']
        user.nik_name = data['nik_name']
        user.email = data['email']
        user.address = data['address']
        user.position = data['position']
        user.role = data['role']
        user.user_name = data['user_name']
        user.password = data['password']
        #user.last_login = data['last_login']
        user.created_at = time.time()#data['created_at']
        user.updated_at = time.time()#data['updated_at']
        db.session.commit()
        return jsonify({"message":"user updated","code":200})
    @admin_login_required
    def delete(self, id, payload):
        Users.query.filter_by(id=id).delete()
        return jsonify({"message":"User Deleted","code":200})