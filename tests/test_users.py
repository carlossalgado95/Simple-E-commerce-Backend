import unittest
import sys
import os
import sqlite3

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from users import create_user_table, register_user, login_user, list_users

class TestUsers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        create_user_table()

    def setUp(self):
        register_user('testuser', 'password123') # Register a user for testing

    def test_login_user(self):
        user_id = login_user('testuser', 'password123') # Log in
        
        # Connect to the database to check the user ID
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE username = ?', ('testuser',))
        expected_user_id = cursor.fetchone()[0]
        conn.close()

        # Check if the returned user ID is the expected one
        self.assertEqual(user_id, expected_user_id)

if __name__ == '__main__':
    unittest.main()
