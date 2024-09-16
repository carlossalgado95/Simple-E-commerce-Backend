import unittest
import sqlite3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from products import create_products_table, add_product, edit_product, remove_product, list_products, view_product_by_id

class TestProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect(':memory:') # Create a connection to the in-memory database
        create_products_table(cls.conn)

    def setUp(self):
        # Clear the product table before each test
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM products')
        self.conn.commit()

    def test_add_product(self):
        # Add a product and check if it was added
        add_product(self.conn, 'Product 1', 'Description 1', 100.0, 10)
        products = list_products(self.conn)
        # Sets to check if product with auto-generated ID is present
        product_ids = [p[0] for p in products]
        self.assertTrue(any(
            p[1:] == ('Product 1', 'Description 1', 100.0, 10) for p in products
        ))

    def test_list_products(self):
        # Add a product and check if it appears in the list
        add_product(self.conn, 'Product 2', 'Description 2', 200.0, 20)
        products = list_products(self.conn)
        # Sets to check if product with auto-generated ID is present
        product_ids = [p[0] for p in products]
        self.assertTrue(any(
            p[1:] == ('Product 2', 'Description 2', 200.0, 20) for p in products
        ))

    def test_edit_product(self):
        # Add a product and edit its information
        add_product(self.conn, 'Product 3', 'Description 3', 300.0, 30)
        products = list_products(self.conn)
        # Get the ID of the added product
        product_id = next(p[0] for p in products if p[1:] == ('Product 3', 'Description 3', 300.0, 30))

        # Edit the product
        edit_product(self.conn, product_id, 'Product 3 Edited', 'Description 3 Edited', 350.0, 35)
        product = view_product_by_id(self.conn, product_id)
        self.assertEqual(product[1], 'Product 3 Edited')
        self.assertEqual(product[2], 'Description 3 Edited')
        self.assertEqual(product[3], 350.0)
        self.assertEqual(product[4], 35)

    def test_remove_product(self):
        # Add a product and remove it
        add_product(self.conn, 'Product 4', 'Description 4', 400.0, 40)
        products = list_products(self.conn)
        # Get the ID of the added product
        product_id = next(p[0] for p in products if p[1:] == ('Product 4', 'Description 4', 400.0, 40))

        # Remove the product'
        remove_product(self.conn, product_id)
        products = list_products(self.conn)
        self.assertNotIn(
            (product_id, 'Product 4', 'Description 4', 400.0, 40),
            products
        )

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

if __name__ == '__main__':
    unittest.main()
