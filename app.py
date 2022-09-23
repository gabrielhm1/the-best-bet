from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/odds/<int:Number>')
def odd(Number):
    print(Number)
    content = {
        "id" : Number
    }
    return render_template("odd.html", content = content)
if __name__ == "__main__":
    app.run(debug=True)
