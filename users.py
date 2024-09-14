import sqlite3
import hashlib

# Função para criar a tabela de usuários (se não existir)
def create_user_table():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Função para verificar se o usuário já existe
def user_exists(username):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()

    return user is not None

# Função para registrar um novo usuário
def register_user(username, password):
    if user_exists(username):
        print(f"Erro: O nome de usuário {username} já está em uso.")
        return

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Hash da senha para garantir a segurança
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''', (username, hashed_password))

    conn.commit()
    conn.close()

    print(f"Usuário {username} registrado com sucesso!")

# Função para realizar login do usuário
def login_user(username, password):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Hash da senha para comparar com o valor armazenado
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute('''
        SELECT id FROM users WHERE username = ? AND password = ?
    ''', (username, hashed_password))

    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"Login bem-sucedido! Bem-vindo, {username}.")
        return user[0]  # Retorna o ID do usuário
    else:
        print("Falha no login: Usuário ou senha incorretos.")
        return None  # Falha no login

# Função para listar todos os usuários
def list_users():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    cursor.execute('SELECT id, username FROM users')
    users = cursor.fetchall()

    conn.close()

    if users:
        print("Usuários cadastrados:")
        for user in users:
            print(f"ID: {user[0]}, Nome de usuário: {user[1]}")
    else:
        print("Nenhum usuário encontrado.")
    
    return users
