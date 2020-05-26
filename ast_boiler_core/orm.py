from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_orm(app):
    db.init_app(app)
    return app
