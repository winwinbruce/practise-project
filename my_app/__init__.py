from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
# app.config['MONGODB_SETTINGS'] = {"db": "mydb",}
app.config.from_pyfile('src/config/flask_config.py')
db = MongoEngine(app)


from my_app.src.api.ml_mnist import ml
from my_app.src.api.db_operations import db_operations


app.register_blueprint(db_operations)
app.register_blueprint(ml)