import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.object import Object, ObjectList
from resources.parent import Parent, ParentList

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# for Heroku
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'IAcceptTheRisk'
api = Api(app)


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Parent, '/parent/<string:name>')
api.add_resource(ParentList, '/parents')
api.add_resource(Object, '/object/<string:name>')
api.add_resource(ObjectList, '/objects')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__': # doing this as we want to run the app only when someone runs it and not on import of app.py from another module
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
