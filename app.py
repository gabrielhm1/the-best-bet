from flask import Flask
# from datetime import date
from datetime import datetime,date
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

import routes.routes
if __name__ == "__main__":
    app.run(debug=True)