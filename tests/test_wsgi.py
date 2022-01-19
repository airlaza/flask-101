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