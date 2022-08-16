from unicodedata import category
from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource

from model import Issues, db
class Issue(Resource):
    def post(self):
        data = request.get_json(force=True)
        name = data['name']
        descriprion = data['descriprion']
        category = data['category']
        priority = data['priority']
        assignee = data['assignee']
        due_date = data['due_date']
        assigned_date = data['assigned_date']
        solved_date = data['solved_date']
        created_at= data['created_at']
        updated_at = data['updated_at']
        issue = Issues(name=name, descriprion=descriprion, category=category, priority=priority, assignee=assignee, due_date=due_date,
            assigned_date=assigned_date, solved_date=solved_date, created_at=created_at, updated_at=updated_at)
        db.session.add(issue)
        db.session.commit()
        return jsonify({"message":"success","code":200})
    def get(self):
        data = Issues.query.all()
        issues = []
        for d in data:
            issues.append({
                     "id":d.id,
                    "name" :d.name,
                    "descriprion" :d.descriprion,
                    "category" :d.category,
                    "priority": d.priority,
                    "assignee" : d.assignee,
                    "due_date": d.due_date,
                    "assigned_date" : d.assigned_date,
                    "solved_date" : d.solved_date,
                    "created_at":  d.created_at,
                    "updated_at" : d.updated_at,
            })
            return jsonify(issues)
class IssuesList(Resource):
    def get(self, id):
        return "get issue"
    def put(self, id):
        return "update issue"
    def delete(self,id):
        return "delete issue"