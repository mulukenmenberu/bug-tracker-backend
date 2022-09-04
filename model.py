
from email.policy import default
from venv import create
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, relationship
db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String)
    nik_name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    address = db.Column(db.String(120))
    position = db.Column(db.String(120))
    role = db.Column(db.String(120))
    user_name = db.Column(db.String(120))
    password = db.Column(db.String())
    last_login = db.Column(db.String(), nullable=True)
    created_at = db.Column(db.String())
    updated_at = db.Column(db.String())

class Issues(db.Model):
    __tablename__ = 'issues'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    descriprion = db.Column(db.String())
    category = db.Column(db.String(120))
    priority = db.Column(db.String(120), nullable=True)
    assignee = db.Column(db.String(120), nullable=True)
    due_date = db.Column(db.String(), nullable=True)
    assigned_date = db.Column(db.String(), nullable=True)
    solved_date = db.Column(db.String(), nullable=True)
    created_at= db.Column(db.String(), nullable=True)
    updated_at = db.Column(db.String(), nullable= True)


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    issue_id = db.Column(db.Integer, db.ForeignKey('issues.id'))
    content = db.Column(db.String(120), nullable=False)
    user_id_fk = relationship('Users', backref='parent_user', foreign_keys=[user_id], cascade="all,delete")
    issue_id_fk = relationship('Issues', backref='parent_issue', foreign_keys=[issue_id], cascade="all,delete")
