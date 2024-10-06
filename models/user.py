from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(150), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        hasher = PasswordHasher()
        self.password = hasher.hash(password)

    def check_password(self, password):
        hasher = PasswordHasher()
        try:
            return hasher.verify(self.password, password)
        except Exception:
            return False

    def __repr__(self):
        return f'<User {self.username}>'
