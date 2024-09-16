import unittest
import sqlite3
import sys
import os

# Add the root directory to the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cart import create_cart_table, add_to_cart, view_cart, remove_from_cart
from products import create_products_table, add_product

class TestCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect(':memory:')  # Use in-memory database for tests
        create_cart_table(cls.conn)
        create_products_table(cls.conn)
        add_product(cls.conn, 'Test Product', 'Test Description', 100.0, 10)
    
    def setUp(self):
        self.conn.execute('DELETE FROM cart') # Clear the cart before each test
        self.conn.commit()

    def test_add_to_cart(self):
        add_to_cart(self.conn, 1, 1, 2)  # Add the product to the cart
        items = view_cart(1, self.conn)
        self.assertIn(('Test Product', 2, 100.0), items)

    def test_remove_from_cart(self):
        self.conn.execute('INSERT INTO cart (user_id, product_id, quantity) VALUES (1, 1, 2)') # Add a product to the cart
        self.conn.commit()
        
        items_before = view_cart(1, self.conn) # Check if item is present before removal
        self.assertIn(('Test Product', 2, 100.0), items_before)
        cart_id = self.conn.execute('SELECT id FROM cart WHERE user_id = 1 AND product_id = 1').fetchone()[0]
        
        remove_from_cart(self.conn, cart_id) # Remove product from cart
        items_after = view_cart(1, self.conn) # Check if the item was removed
        self.assertNotIn(('Test Product', 2, 100.0), items_after)

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

if __name__ == '__main__':
    unittest.main()
