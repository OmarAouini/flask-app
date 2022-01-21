from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from home.routes import home_blueprint
from authentication.routes import authentication_blueprint

#db
db = SQLAlchemy()

app = Flask(__name__)
# Setup Flask-SQLAlchemy
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)
# Register blueprints
app.register_blueprint(home_blueprint)
app.register_blueprint(authentication_blueprint)