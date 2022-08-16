from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from model import Comments, db
class Comment(Resource):
    def post(self):
        data = request.get_json(force=True)
        user_id = data['user_id']
        issue_id = data['issue_id']
        content = data['content']
        comment = Comments(user_id=user_id, issue_id=issue_id, content=content)
        db.session.add(comment)
        db.session.commit()
        return jsonify({"message":"success","code":200})
    def get(self):
        data = Comments.query.all()
        comments = []
        for d in data:
            comments.append({
                    "id" :d.id,
                    "user_id" :d.user_id,
                    "issue_id" :d.issue_id,
                    "content": d.content,
            })
            return jsonify(comments)
class CommentList(Resource):
    def get(self, id):
        return "get comment"
    def put(self, id):
        return "update comment"
    def delete(self, id):
        return "delete comment"