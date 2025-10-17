from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

@app.route('/about')
def about():
    return render_template("shablon.html")

if __name__ == "__main__":
    app.run(debug=True)