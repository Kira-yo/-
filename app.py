from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("Startpage.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/enter")
def enter():
    return render_template("enter.html")


@app.route("/Mainpage")
def Mainpage():
    return render_template("Mainpage.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/information")
def information():
    return render_template("information.html")

@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

