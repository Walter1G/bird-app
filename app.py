from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
import psycopg2 


from models import db, Bird

import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wal:189DlOofPYdItjngGiTheguvCKCM50xR@dpg-cmj9cv21hbls738hus70-a.ohio-postgres.render.com/bird_app_kwpf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.json.compact = False

migrate = Migrate(app, db)

api =  Api(app)

class Birds(Resource):
    def get(self):
        birds = [bird.to_dict() for bird in Bird.query.all()]
        return make_response(jsonify(birds), 200)
    
api.add_resource(Birds, '/birds')


