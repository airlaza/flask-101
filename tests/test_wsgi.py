# test_wsgi.py
from flask_testing import TestCase
from wsgi import app

class ApplicationTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app
    
    def test_hello(self):
        response = self.client.get('/')
        body = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Hello" in body)

    def test_read_many_products(self):
        response = self.client.get('/api/v1/produits')
        products = response.json
        self.assertIsInstance(products, dict)
        self.assertGreater(len(products), 2)

    def test_read_one_product(self):
        response = self.client.get('/api/v1/produits/1')
        product = response.json
        self.assertIsInstance(product, dict)
        self.assertGreater(len(product), 1)

    def test_delete_one_product(self):
        response = self.client.get('/api/v1/produits/1')
        response_all = self.client.get('/api/v1/produits')
        product = response.json
        self.assertIsInstance(response_all.json, dict)
        self.assertEqual(len(response_all.json), 2)