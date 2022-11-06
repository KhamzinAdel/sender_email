from app import app, db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    generation_code = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<users> {self.id}'



