from flask import Flask

from app.webhook.routes import webhook

from flask_pymongo import PyMongo
mongo = PyMongo()

# Creating our flask app
def create_app():

    app = Flask(__name__,template_folder="templates")
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/webhookdata'
    mongo.init_app(app)

    # registering all the blueprints
    app.register_blueprint(webhook)
    
    return app
