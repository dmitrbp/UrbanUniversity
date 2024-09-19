import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
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


