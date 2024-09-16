import sqlite3
import hashlib

# Function to create the users table (if it doesn't exist)
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

# Function to check if the user already exists
def user_exists(username):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()

    return user is not None

# Function to register a new user
def register_user(username, password):
    if user_exists(username):
        print(f"Erro: O nome de usuário {username} já está em uso.")
        return

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Password hashing to ensure security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''', (username, hashed_password))

    conn.commit()
    conn.close()

    print(f"Usuário {username} registrado com sucesso!")

# Function to perform user login
def login_user(username, password):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Hash of the password to compare with the stored value
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute('''
        SELECT id FROM users WHERE username = ? AND password = ?
    ''', (username, hashed_password))

    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"Login bem-sucedido! Bem-vindo, {username}.")
        return user[0]  # Returns the user ID
    else:
        print("Falha no login: Usuário ou senha incorretos.")
        return None  # Login failed

# Function to list all users
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
