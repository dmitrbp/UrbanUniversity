import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER
)''')
# cursor.execute('CREATE INDEX IF NOT EXISTS idx_age ON Users(age)')

values = [
    ("User1", "example1@gmail.com", "10", "1000"),
    ("User2", "example2@gmail.com", "20", "1000"),
    ("User3", "example3@gmail.com", "30", "1000"),
    ("User4", "example4@gmail.com", "40", "1000"),
    ("User5", "example5@gmail.com", "50", "1000"),
    ("User6", "example6@gmail.com", "60", "1000"),
    ("User7", "example7@gmail.com", "70", "1000"),
    ("User8", "example8@gmail.com", "80", "1000"),
    ("User9", "example9@gmail.com", "90", "1000"),
    ("User10", "example10@gmail.com", "100", "1000")
]
for row in values:
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)', row)

for i in range(1, len(values) + 1):
    if (i - 1) % 2 == 0:
        cursor.execute('UPDATE Users SET balance = 500 WHERE id = ?', (i,))

for i in range(1, len(values) + 1):
    if (i - 1) % 3 == 0:
        cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

cursor.execute("SELECT * FROM Users WHERE age <> 60")
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')
print(users)

cursor.close()
connection.commit()
connection.close()
