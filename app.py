from flask import Flask,render_template
# from datetime import date
from datetime import datetime,date
from models.tables import db
from models.tables import Match

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/postgres'
db.init_app(app)


@app.route('/')
def index():
    date_today = date.today()

    matchs = Match.query.filter( date_today <= Match.match_date).all()

    return render_template("index.html",matchs=matchs)

@app.route('/odds/<int:Number>')
def odd(Number):
    print(Number)
    content = {
        "id" : Number
    }
    return render_template("odd.html", content = content)

if __name__ == "__main__":
    app.run(debug=True)
