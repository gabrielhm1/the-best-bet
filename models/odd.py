from app import db


class Odd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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