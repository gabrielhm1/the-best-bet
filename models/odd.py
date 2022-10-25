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
def insert_odd(id_match):
    item = request.json['odds']
    check_exist = Odd.query.filter_by(company=item['company']).filter_by(match_id=id_match).first()
    odd = Odd() if check_exist is None else check_exist 
    odd.company = item['company']
    odd.host_win = item['host_win']
    odd.away_win = item['away_win']
    odd.match_draw = item['match_draw']
    odd.match_id = id_match
    
    try:
        if check_exist is None:
            db.session.add(odd)
            db.session.commit()
            return jsonify({'mensagem': f'Odd adicionada a partida {id_match}!'}), 201
        else:
            db.session.commit()
            return jsonify({'mensagem': f'Odd {odd.id} da partida {id_match} editada com sucesso!'}), 201

    except Exception as e:
        return jsonify({'mensagem': 'Erro no cadastro!'}), 500
