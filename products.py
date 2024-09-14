import sqlite3

def create_products_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL CHECK(price >= 0),
            stock INTEGER NOT NULL CHECK(stock >= 0)
        )
    ''')
    conn.commit()

def add_product(conn, name, description, price, stock):
    if not name or price < 0 or stock < 0:
        raise ValueError("Entrada inválida. Verifique os dados fornecidos.")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, description, price, stock)
        VALUES (?, ?, ?, ?)
    ''', (name, description, price, stock))
    conn.commit()
    print(f"Produto {name} adicionado com sucesso!")

def edit_product(conn, product_id, name, description, price, stock):
    if not name or price < 0 or stock < 0:
        raise ValueError("Entrada inválida. Verifique os dados fornecidos.")
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products
        SET name = ?, description = ?, price = ?, stock = ?
        WHERE id = ?
    ''', (name, description, price, stock, product_id))
    conn.commit()
    print(f"Produto {name} atualizado com sucesso!")

def remove_product(conn, product_id):
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM products WHERE id = ?
    ''', (product_id,))
    conn.commit()
    print(f"Produto {product_id} removido com sucesso!")

def list_products(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, description, price, stock FROM products')
    products = cursor.fetchall()
    return products

def view_product_by_id(conn, product_id):
    if product_id <= 0:
        raise ValueError("ID do produto inválido.")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product_data = cursor.fetchone()
    return product_data
