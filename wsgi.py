# wsgi.py
from flask import Flask, jsonify, abort
app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Le Wagon'},
    }
@app.route('/')
def hello():
    return "Hello world", 200

@app.route('/api/v1/produits', methods = ['GET'])
def read_many_products():    
    return jsonify(PRODUCTS), 200

@app.route('/api/v1/produits/<int:id>', methods = ['GET'])
def read_one_product(id):
    product = PRODUCTS.get(id)
    if product is None:
        abort(404)
    else:
        return jsonify(product), 200
