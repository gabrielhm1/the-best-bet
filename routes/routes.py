from app import app
from flask import render_template
from datetime import datetime,date
from models import match


@app.route('/')
def index():
    date_today = date.today()
    matchs_data = []
    matchs = match.Match.query.filter( date_today >= match.Match.match_date).all()
    for this_match in matchs:
        matchs_data.append(match.get_all_data(this_match))

    return render_template("index.html",content=matchs_data)

@app.route('/odds/<int:match_id>')
def odd(match_id):
    response = match.Match.query.filter_by(id=match_id)
    content = {
        "match": match.get_all_data(response[0])
    }

    return render_template("odd.html", content = content)

@app.route('/match', methods=['POST'])
def add_match():
    return match.insert_match()
