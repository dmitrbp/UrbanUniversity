import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        );
        '''
    )
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        );
        '''
    )
    connection.commit()

def get_all_products():
    products_list = [i for i in cursor.execute('SELECT * FROM Products;').fetchall()]
    connection.commit()
    return products_list

def fill_products():
    values = [
        ("Продукт 1", "Описание 1", "100"),
        ("Продукт 2", "Описание 2", "200"),
        ("Продукт 3", "Описание 3", "300"),
        ("Продукт 4", "Описание 4", "400")
    ]
    if cursor.execute('SELECT COUNT(*) FROM Products').fetchone()[0] == 0:
        for row in values:
            cursor.execute('INSERT INTO Products(title, description, price) VALUES(?, ?, ?)', row)
    connection.commit()

def add_user(username, email, age):
    cursor.execute('''
        INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)''',
        (username, email, age, 1000)
    )
    connection.commit()

def is_included(username):
    return bool(
        cursor.execute(
        'SELECT COUNT(*) FROM Users WHERE username = ?', (username, )
        ).fetchone()[0]
    )
