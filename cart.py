import sqlite3

# Função para criar a tabela de carrinhos (se não existir)
def create_cart_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    ''')
    conn.commit()

# Função para visualizar o carrinho de um usuário
def view_cart(user_id, conn):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT products.name, cart.quantity, products.price
        FROM cart
        JOIN products ON cart.product_id = products.id
        WHERE cart.user_id = ?
    ''', (user_id,))
    items = cursor.fetchall()
    return items

# Função para adicionar um produto ao carrinho
def add_to_cart(conn, user_id, product_id, quantity):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO cart (user_id, product_id, quantity)
        VALUES (?, ?, ?)
    ''', (user_id, product_id, quantity))
    conn.commit()
    print(f"Produto {product_id} adicionado ao carrinho do usuário {user_id}.")

def remove_from_cart(conn, cart_id):
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM cart WHERE id = ?
    ''', (cart_id,))
    conn.commit()
    print(f"Produto com ID {cart_id} removido do carrinho.")
