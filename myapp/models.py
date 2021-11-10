from myapp import db
from datetime import datetime

from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String (64), index = True, unique = True)
    city_rank = db.Column(db.Integer ())
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def __repr__ (self):
        return f'{self.city_name} with rank number {self.city_rank}'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column (db.DateTime, default=datetime.utcnow)
    user_id = db.Column (db.Integer, db.ForeignKey ('user.id'))

    def __repr__(self):
        return f'<Post {self.id}: {self.body}>'
