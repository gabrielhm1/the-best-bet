from models import Match,Odd
from app import db
from datetime import datetime
match =[
        Match(id=1,host_team="Atletico",away_team="Cruzeiro",match_date=datetime.now()),
        Match(id=2,host_team="Palmeiras",away_team="São Paulo",match_date=datetime.now()),
        Match(id=3,host_team="Santos",away_team="Vasco",match_date=datetime.now())
        ]
odds = [
    Odd(id=1,company="Betano",host_win=2.20,away_win=3.2,match_draw=2.5,match_id=2),
    Odd(id=2,company="PixBet",host_win=3,away_win=4.2,match_draw=2.5,match_id=2),
    Odd(id=3,company="Betano",host_win=3,away_win=3.2,match_draw=2.5,match_id=1),
    Odd(id=4,company="PixBet",host_win=2.20,away_win=5.2,match_draw=2.5,match_id=1),
    Odd(id=5,company="Betano",host_win=6.20,away_win=3.5,match_draw=2.6,match_id=3),
    Odd(id=6,company="Betano",host_win=4.20,away_win=3.2,match_draw=2.5,match_id=3),
]

with app.app_context():
    db.create_all()
    db.session.add_all(match)
    db.session.add_all(odds)
    db.session.commit()