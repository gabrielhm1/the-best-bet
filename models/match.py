from datetime import datetime
from app import db
from .odd import Odd
from flask import request, jsonify


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
        if odd.away_win > best_odd["away_win"]["odd"]:
            best_odd["away_win"]["odd"] = odd.away_win
            best_odd["away_win"]["company"] = odd.company
        if odd.match_draw > best_odd["draw"]["odd"]:
            best_odd["draw"]["odd"] = odd.match_draw
            best_odd["draw"]["company"] = odd.company
    return best_odd

def get_all_data(match):
    best_odd = {"best_odd": get_best_odd(match)}
    match_info = dict(match.to_json(), **best_odd)
    return match_info

def insert_match():
    odds_list = []
    match = Match()
    odd = request.json['odds']
    match.host_team = request.json['host_team']
    match.away_team = request.json['away_team']
    match.match_date = datetime.now()
    odd_insert = Odd(
        company = odd['company'],
        host_win = odd['host_win'],
        away_win = odd['away_win'],
        match_draw = odd['match_draw']
    )
    match.odd = odds_list

    try:
        db.session.add(match)
        db.session.commit()
        return jsonify({'Message': 'Registered!'}), 201
    except:
        return jsonify({'Message': 'Failure!'}), 500

def update_match(match):
    odds_list = []

    try:
        match.host_team = request.json['host_team']
        match.away_team = request.json['away_team']
        # match.match_date = datetime.now()
        
        for odd in match.odd:
            odds_list.append(odd)
        for odd in request.json['odds']:
            odd_insert = Odd(
                company = odd['company'],
                host_win = odd['host_win'],
                away_win = odd['away_win'],
                match_draw = odd['match_draw']
            )
            odds_list.append(odd_insert)
        match.odd = odds_list
        db.session.commit()

        return jsonify({'Message': 'Match updated!'}), 201
    except:
        return jsonify({'Message': 'Failed to update data!'}), 500