# wsgi.py
from flask import Flask
from flask import jsonify
app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Le Wagon'},
    }

@app.route('/api/v1/produits')
def read_many_products():    
    return jsonify(PRODUCTS), 200