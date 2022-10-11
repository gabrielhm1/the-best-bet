import re
from flask import Flask,render_template
# from datetime import date
from datetime import datetime,date

from sqlalchemy import null
from models.tables import db
from models.tables import Match,Odd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)
def compare_odds(match_id):
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
    odds = Odd.query.filter_by(match_id = match_id)
    for odd in odds:
        if odd.host_win > best_odd["host_win"]["odd"]:
            best_odd["host_win"]["odd"] = odd.host_win
            best_odd["host_win"]["company"] = odd.company
        if odd.away_win > best_odd["host_win"]["odd"]:
            best_odd["away_win"]["odd"] = odd.away_win
            best_odd["away_win"]["company"] = odd.company
        if odd.match_draw > best_odd["draw"]["odd"]:
            best_odd["draw"]["odd"] = odd.match_draw
            best_odd["draw"]["company"] = odd.company
    # print(best_odd)
    return best_odd

def get_best_odd(match_id=null,matchs=null):
    if matchs == null:
        best_odd = compare_odds(match_id)
        return best_odd
    elif match_id == null:
        matchs_info = []
        for match in matchs:
            best_odd = compare_odds(match.id)
            match_dict = vars(match)
            matchs_info.append(dict(match_dict, **best_odd))
        return matchs_info


@app.route('/')
def index():
    date_today = date.today()
    matchs = Match.query.filter( date_today >= Match.match_date).all()
    matchs_info  = get_best_odd(matchs=matchs)
    print(matchs_info)
    return render_template("index.html",content=matchs_info)

@app.route('/odds/<int:match_id>')
def odd(match_id):
    odds = Odd.query.filter_by(match_id = match_id)
    match = Match.query.filter_by(id=match_id)

    content = {
        "best_odd": get_best_odd(match_id=match_id),
        "odds": odds,
        "match":match  
    }

    return render_template("odd.html", content = content)

if __name__ == "__main__":
    app.run(debug=True)
