from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#db = SQLAlchemy(app)


@app.route('/', methods=["GET"])
def hello_endpoint():
    return "HELLO, WORLD!!!"
