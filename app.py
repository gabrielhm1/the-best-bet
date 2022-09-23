from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template("index.html")

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host_team = db.Column(db.String(200), nullable=False)
    away_team = db.Column(db.String(200), nullable=False)
    match_date = db.Column(db.DateTime, nullable=False)
    
    
    odd = db.relationship("Odd",backref="match")

class Odd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(2000))
    host_win = db.Column(db.Integer)
    away_win = db.Column(db.Integer)
    match_draw = db.Column(db.Integer)

    match_id = db.Column(db.Integer, db.ForeignKey("match.id"))


@app.route('/odds/<int:Number>')
def odd(Number):
    print(Number)
    content = {
        "id" : Number
    }
    return render_template("odd.html", content = content)

if __name__ == "__main__":
    app.run(debug=True)
