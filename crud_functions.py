import sqlite3


def initiate_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')

    # cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    #                ('Упорин', 'Описание', '100'))
    # cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    #                ('Ниибётин', 'Описание', '200'))
    # cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    #                ('Похерон', 'Описание', '300'))
    # cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    #                ('Хулинам', 'Описание', '400'))

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result

