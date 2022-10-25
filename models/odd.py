from app import db
from flask import request, jsonify

class Odd(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company = db.Column(db.String(2000))
    host_win = db.Column(db.Integer)
    away_win = db.Column(db.Integer)
    match_draw = db.Column(db.Integer)

    match_id = db.Column(db.Integer, db.ForeignKey("match.id"))

    def to_json(self):
        return {
            "id": self.id,
            "company": self.company,
            "host_win": self.host_win,
            "away_win": self.away_win,
            "match_draw": self.match_draw
        }
def insert_odd():
    odds_list = []
    odd = Odd()
    odd.company = request.json['company']
    odd.host_win = request.json['host_win']
    odd.away_win = request.json['away_win']
    odd.match_draw = request.json['match_draw']
    odd.match_id = request.json['match_id']
    
    try:
        db.session.add(odd)
        db.session.commit()
        return jsonify({'mensagem': 'Cadastro Realizado!'}), 201
    except:
        return jsonify({'mensagem': 'Erro no cadastro!'}), 500
