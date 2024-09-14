import unittest
import sqlite3
import sys
import os

# Adicione o diretório raiz ao caminho de importação
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cart import create_cart_table, add_to_cart, view_cart, remove_from_cart
from products import create_products_table, add_product

class TestCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect(':memory:')  # Use in-memory database for tests
        
        # Cria as tabelas necessárias no banco de dados em memória
        create_cart_table(cls.conn)
        create_products_table(cls.conn)
        
        # Adiciona um produto para os testes
        add_product(cls.conn, 'Test Product', 'Test Description', 100.0, 10)
    
    def setUp(self):
        # Limpa o carrinho antes de cada teste
        self.conn.execute('DELETE FROM cart')
        self.conn.commit()

    def test_add_to_cart(self):
        add_to_cart(self.conn, 1, 1, 2)  # Adiciona o produto ao carrinho
        items = view_cart(1, self.conn)
        self.assertIn(('Test Product', 2, 100.0), items)

    def test_remove_from_cart(self):
        # Adiciona um produto ao carrinho
        self.conn.execute('INSERT INTO cart (user_id, product_id, quantity) VALUES (1, 1, 2)')
        self.conn.commit()
        
        # Verifica se o item está presente antes da remoção
        items_before = view_cart(1, self.conn)
        self.assertIn(('Test Product', 2, 100.0), items_before)
        
        # Obtém o ID do carrinho do produto
        cart_id = self.conn.execute('SELECT id FROM cart WHERE user_id = 1 AND product_id = 1').fetchone()[0]
        
        # Remove o produto do carrinho
        remove_from_cart(self.conn, cart_id)
        
        # Verifica se o item foi removido
        items_after = view_cart(1, self.conn)
        self.assertNotIn(('Test Product', 2, 100.0), items_after)

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

if __name__ == '__main__':
    unittest.main()
