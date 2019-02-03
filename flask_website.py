"""
This is a small python/flask website created to exercise using html, css and python.
Web app created from practice in The Python Mega Course, from Ardit Sulce.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template("home.html")

@app.route('/about/')
def about ():
    return render_template("about.html")

if (__name__ == "__main__"):
    app.run(debug = True)
