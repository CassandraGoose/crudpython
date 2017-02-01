from app import db
from sqlalchemy.dialects.postgresql import JSON


class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('title', db.String())
    genre = db.Column('genre', db.String())

    def __init__(self, title, genre):
        self.title = title
        self.genre = genre


    def __repr__(self):
        return '<id {}>'.format(self.id)
