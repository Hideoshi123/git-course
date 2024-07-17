from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hideoshi Peralta"

@app.route('/sum/<int:numa>/<int:numb>')
def sum(a: int,b: int):
    return a + b