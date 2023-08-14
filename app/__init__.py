from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if not test_config:

        #app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("RENDER_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        #app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("RENDER_DATABASE_URI")

    from app.models.milk import Milk
    
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.milk_routes import milks_bp
    app.register_blueprint(milks_bp)

    return app
