from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host_team = db.Column(db.String(200), nullable=False)
    away_team = db.Column(db.String(200), nullable=False)
    match_date = db.Column(db.Date, nullable=False)
    
    
    odd = db.relationship("Odd",backref="match")

class Odd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(2000))
    host_win = db.Column(db.Integer)
    away_win = db.Column(db.Integer)
    match_draw = db.Column(db.Integer)

    match_id = db.Column(db.Integer, db.ForeignKey("match.id"))