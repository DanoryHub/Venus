from flask_sqlalchemy import SQLAlchemy

from os import environ
from app import app


def create_db_connection(app):
    POSTGRES_USER = environ.get("POSTGRES_USER")
    POSTGRES_PW = environ.get("POSTGRES_PASSWORD")
    POSTGRES_DB = environ.get("POSTGRES_DB")

    DB_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PW}@localhost:44312/{POSTGRES_DB}'

    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

    SQLAlchemy(app)


if __name__ == "__main__":
    create_db_connection(app)
    app.run()
