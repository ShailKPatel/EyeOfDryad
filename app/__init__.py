from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    csrf.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
