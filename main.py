import sqlite3

# Conectar ao banco de dados (ele será criado se não existir)
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Criar tabela de usuários
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password_hash TEXT NOT NULL
)
''')

# Criar tabela de produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    price REAL NOT NULL
)
''')

conn.commit()
conn.close()
