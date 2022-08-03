import os
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("/index.html")

@app.route("/next")
def next():
     return 'This could be the next page!!'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)
