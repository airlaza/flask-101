# wsgi.py
from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world"

@app.route('/api/v1/produits')
def list_products():
    PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    }
    return jsonify(PRODUCTS)