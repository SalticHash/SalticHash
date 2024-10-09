# Imports from files
from lang import LANG
from config import CONFIG

# Flask Imports
from flask import Flask, redirect, render_template, request, url_for

# Configure application
app = Flask(__name__)

app.jinja_env.globals.update(lang = LANG)

# Routes
@app.route("/")
def index():
    return render_template("index.html", categories=CONFIG["projects"])

@app.route("/more")
def view():
    return render_template("more.html")

@app.route("/edu")
def edu():
    return render_template("edu.html")

@app.route('/socials')
def manual():
    return render_template("socials.html")

@app.errorhandler(404)
def page_not_found(_event):
    return error("Page not found, It's nowhere to be seen", 404)

def error(text, statuscode = 400):
    req = {"text": text, "statuscode": statuscode}
    return render_template("error.html", req=req)

if __name__ == "__main__":
    app.run(port=2727)
