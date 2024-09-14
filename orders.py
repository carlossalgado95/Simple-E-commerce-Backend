import sqlite3

def is_valid_user_id(user_id):
    """Verifica se o ID do usuário é válido."""
    return isinstance(user_id, int) and user_id > 0

def is_valid_order_id(order_id):
    """Verifica se o ID do pedido é válido."""
    return isinstance(order_id, int) and order_id > 0

def is_valid_total(total):
    """Verifica se o total é válido."""
    return isinstance(total, (int, float)) and total >= 0

def create_orders_table():
    conn = sqlite3.connect('test_db.sqlite3')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            total_price REAL,
            order_date TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()

def drop_orders_table():
    conn = sqlite3.connect('test_db.sqlite3')
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS orders')

    conn.commit()
    conn.close()

def place_order(user_id):
    if not is_valid_user_id(user_id):
        raise ValueError("Invalid user ID")

    conn = sqlite3.connect('test_db.sqlite3')
    cursor = conn.cursor()

    # Calcular o total do carrinho
    cursor.execute('''
        SELECT SUM(products.price * cart.quantity) AS total
        FROM cart
        JOIN products ON cart.product_id = products.id
        WHERE cart.user_id = ?
    ''', (user_id,))
    total = cursor.fetchone()[0]

    if total is None:
        total = 0.0

    if not is_valid_total(total):
        raise ValueError("Invalid total amount")

    # Criar o pedido
    cursor.execute('''
        INSERT INTO orders (user_id, total_price, order_date)
        VALUES (?, ?, DATE('now'))
    ''', (user_id, total))

    order_id = cursor.lastrowid

    # Limpar o carrinho após o pedido
    cursor.execute('''
        DELETE FROM cart WHERE user_id = ?
    ''', (user_id,))

    conn.commit()
    conn.close()

    print(f"Pedido #{order_id} criado com sucesso! Total: R${total:.2f}")

def view_order_details(order_id, user_id):
    if not is_valid_order_id(order_id):
        raise ValueError("Invalid order ID")
    if not is_valid_user_id(user_id):
        raise ValueError("Invalid user ID")

    conn = sqlite3.connect('test_db.sqlite3')
    cursor = conn.cursor()

    # Verificar se o pedido pertence ao usuário
    cursor.execute('''
        SELECT user_id FROM orders WHERE id = ?
    ''', (order_id,))
    order_user_id = cursor.fetchone()

    if order_user_id is None or order_user_id[0] != user_id:
        conn.close()
        raise PermissionError("You are not authorized to view this order")

    # Obter detalhes do pedido
    cursor.execute('''
        SELECT * FROM orders WHERE id = ?
    ''', (order_id,))
    order = cursor.fetchone()

    conn.close()

    if order:
        return {
            'order_id': order[0],
            'user_id': order[1],
            'total_price': order[2],
            'order_date': order[3]
        }
    else:
        return None
