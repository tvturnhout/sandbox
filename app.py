from flask import Flask, render_template

import safygiphy

app = Flask(__name__)
 
@app.route("/")
def index():
    return "Index"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/members")
def members():
    return "Members"

@app.route("/hello/<string:name>")
def getMember(name):
    g = safygiphy.Giphy()
    r = g.random(tag=name)
    return render_template('test.html', name=name, url_gif=r["data"]["id"])
 
if __name__ == "__main__":
    app.run()