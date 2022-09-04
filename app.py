
from flask import Flask, request, Response, jsonify, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from models.model import  db
from flask_restful import Resource, Api
from flask_cors import CORS

from resources.comments import Comment, CommentList 
from resources.issues import Issue, IssuesList
from resources.users import User, UserList
from resources.login import Login
app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db.init_app(app)  
api = Api(app)
CORS(app)

migrate = Migrate(app, db)
# Registration and all Retrival
api.add_resource(User, '/users/')
api.add_resource(Issue, '/issues/')
api.add_resource(Comment, '/comments/')

#Update and Delete on a single entity 
api.add_resource(UserList, '/users/<int:id>')
api.add_resource(IssuesList, '/issues/<int:id>')
api.add_resource(CommentList, '/comments/<int:id>')

## Login endpoint
api.add_resource(Login, '/login')


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"message":"page not found","error":404})
@app.route('/',methods=['GET','POST'])
def index():
    return "ok" 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.debug = True