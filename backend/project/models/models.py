from app import db


class Clothes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    blob_path = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=True)
    cloth_type = db.Column(db.String, nullable=False)