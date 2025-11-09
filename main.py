from flask import Flask, render_template

app = Flask(__name__)

dzindza_menu = ['download', 'feedback', 'my websites']

@app.route('/')
def index():
    return "index"
print("hi")
@app.route('/about')
def about():
    return render_template("shablon.html", title='dzindza module', menu=dzindza_menu)


if __name__ == "__main__":
    app.run(debug=True)