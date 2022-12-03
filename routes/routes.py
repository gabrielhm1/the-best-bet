from app import app
from flask import render_template
from datetime import datetime,date
from models import match,odd
from flask import request,jsonify


@app.route('/')
def index():
    date_today = date.today()
    item = match.Match.query.filter_by(host_team="Atletico").filter_by(away_team="Cruzeiro").first()
    matchs_data = []
    matchs = match.Match.query.filter( date_today >= match.Match.match_date).all()
    for this_match in matchs:
        matchs_data.append(match.get_all_data(this_match))

    return render_template("index.html",content=matchs_data)

@app.route('/odds/<int:match_id>')
def odd_page(match_id):
    response = match.Match.query.filter_by(id=match_id)
    content = {
        "match": match.get_all_data(response[0])
    }

    return render_template("odd.html", content = content)

@app.route('/match', methods=['POST'])
def add_match():
    try:
        host = request.json['host_team']
        away = request.json['away_team']
        item = match.Match.query.filter_by(host_team=host).filter_by(away_team=away).first()
        if item is None:
            return match.insert_match()
        else:
            return odd.insert_odd(item.id)
    except Exception as e:
        return jsonify({'Message': 'General error!'}), 500


