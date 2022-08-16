from unicodedata import name
from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from model import Users, Issues, Comments, db
class User(Resource):
    def post(self):
        data = request.get_json(force=True)
        full_name = data['full_name']
        nik_name = data['nik_name']
        email = data['email']
        address = data['address']
        position = data['position']
        role = data['role']
        user_name = data['user_name']
        password = data['password']
        last_login = data['last_login']
        created_at = data['created_at']
        updated_at = data['updated_at']
        user = Users(full_name=full_name, nik_name=nik_name, email=email, address=address, position=position, role=role,
        user_name=user_name, password=password, last_login=last_login, created_at=created_at, updated_at=updated_at)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message":"success","code":200})
    def get(self):
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
    def get(self, id):
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
    def put(self, id):
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
        user.last_login = data['last_login']
        user.created_at = data['created_at']
        user.updated_at = data['updated_at']
        db.session.commit()
        return jsonify({"message":"success","code":200})
    def delete(self, id):
        Users.query.filter_by(id=id).delete()
        return jsonify({"message":"success","code":200})