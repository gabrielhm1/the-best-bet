from models.match import Match
from models.odd import Odd
from app import db,app
from datetime import datetime
match =[]
odds = []

with app.app_context():
    db.create_all()
    db.session.add_all(match)
    db.session.add_all(odds)
    db.session.commit()