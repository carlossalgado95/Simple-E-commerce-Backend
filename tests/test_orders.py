import sys
import os
import unittest
import sqlite3

# Adicionar o diretório 'src' ao caminho de busca do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from orders import create_orders_table, drop_orders_table, place_order, view_order_details

class TestOrders(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configuração para o banco de dados de teste
        cls.test_db = 'test_db.sqlite3'
        if os.path.exists(cls.test_db):
            os.remove(cls.test_db)
        
        # Criar as tabelas necessárias
        create_orders_table()

        cls.conn = sqlite3.connect(cls.test_db)
        cls.cursor = cls.conn.cursor()

        # Criar tabelas adicionais necessárias para os testes
        cls.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE
            )
        ''')
        cls.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        cls.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cart (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(product_id) REFERENCES products(id)
            )
        ''')

        # Inserir dados de exemplo
        cls.cursor.execute('INSERT INTO users (username) VALUES ("Test User")')
        cls.cursor.execute('INSERT INTO users (username) VALUES ("Another User")')
        cls.cursor.execute('INSERT INTO products (name, price) VALUES ("Test Product", 10.0)')
        cls.cursor.execute('INSERT INTO products (name, price) VALUES ("Another Product", 15.0)')

        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        # Fechar a conexão e remover o banco de dados de teste
        cls.conn.close()
        if os.path.exists(cls.test_db):
            os.remove(cls.test_db)

    def test_place_order(self):
        # Inserir dados no carrinho
        self.cursor.execute('INSERT INTO cart (user_id, product_id, quantity) VALUES (1, 1, 2)')
        self.conn.commit()

        # Fazer o pedido
        place_order(1)

        # Verificar o pedido
        self.cursor.execute('SELECT * FROM orders')
        orders = self.cursor.fetchall()
        
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0][1], 1)  # user_id
        self.assertEqual(orders[0][2], 20.0)  # total_price

    def test_view_order_details(self):
        # Fazer um pedido
        place_order(1)
        
        # Testar a visualização dos detalhes do pedido
        order_details = view_order_details(1, 1)
        self.assertIsNotNone(order_details)
        self.assertIn('order_id', order_details)
        self.assertIn('user_id', order_details)
        self.assertIn('total_price', order_details)

    def test_invalid_user_id_place_order(self):
        # Testar a função place_order com um ID de usuário inválido
        with self.assertRaises(ValueError):
            place_order(-1)

    def test_invalid_order_id_view_order_details(self):
        # Testar a função view_order_details com um ID de pedido inválido
        with self.assertRaises(ValueError):
            view_order_details(-1, 1)

    def test_unauthorized_access_view_order_details(self):
        # Fazer um pedido com um usuário
        place_order(1)
        
        # Testar o acesso não autorizado
        with self.assertRaises(PermissionError):
            view_order_details(1, 2)  # Usuário diferente do que fez o pedido

if __name__ == '__main__':
    unittest.main()
