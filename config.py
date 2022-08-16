import os
from flask import Flask

SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost:5432/bug_tracker'
SQLALCHEMY_TRACK_MODIFICATIONS = False