from app import db
from .odd import Odd

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host_team = db.Column(db.String(200), nullable=False)
    away_team = db.Column(db.String(200), nullable=False)
    match_date = db.Column(db.Date, nullable=False)
    
    odd = db.relationship("Odd",backref="match")

    def to_json(self):
        return {
            "id": self.id,
            "host_team": self.host_team,
            "away_team": self.away_team,
            "match_date": self.match_date,
            "odd": [format_odd.to_json() for format_odd in self.odd ]
        }


def get_best_odd(match):
    best_odd = {
        "host_win": {
            "odd": 0
        },
        "away_win": {
            "odd": 0
        },
        "draw":{
            "odd": 0
        }
    }
    for odd in match.odd:
        if odd.host_win > best_odd["host_win"]["odd"]:
            best_odd["host_win"]["odd"] = odd.host_win
            best_odd["host_win"]["company"] = odd.company
        if odd.away_win > best_odd["host_win"]["odd"]:
            best_odd["away_win"]["odd"] = odd.away_win
            best_odd["away_win"]["company"] = odd.company
        if odd.match_draw > best_odd["draw"]["odd"]:
            best_odd["draw"]["odd"] = odd.match_draw
            best_odd["draw"]["company"] = odd.company
    return best_odd

def get_all_data(match):
    best_odd = get_best_odd(match)
    match_info = dict(match.to_json(), **best_odd)
    return match_info