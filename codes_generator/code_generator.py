import random
import sqlite3
import time


def generate(num_of_codes):
    symbols = ['2', '3', '4', '6', '7', '8', '9', 'A', 'B', 'C', 'E', 'F', 'G', 'H',
               'J', 'K', 'L', 'M', 'N', 'P', 'R', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return (random.sample(symbols, 9) for _ in range(num_of_codes))


def add_to_db(codes):
    conn = sqlite3.connect('chio_codes.sqlite')
    cur = conn.cursor()
    time_now = time.strftime('%Y-%m-%d %H:%M:%S')

    cur.executescript('''
        CREATE TABLE IF NOT EXISTS Codes (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            code   TEXT UNIQUE,
            generation_id INTEGER,
            usage_id INTEGER
        );
        
        CREATE TABLE IF NOT EXISTS Generation (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            datetime TEXT UNIQUE
        );
        
        CREATE TABLE IF NOT EXISTS Usage (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            datetime TEXT,
            pdf_file_name TEXT
        )    
        ''')

    cur.execute('''INSERT OR IGNORE INTO Generation (datetime)
        VALUES (?)''', (time_now, ))
    cur.execute('SELECT id FROM Generation WHERE datetime = ? ', (time_now, ))
    generation_id = cur.fetchone()[0]

    for code in codes:
        cur.execute('''INSERT OR IGNORE INTO Codes (code, generation_id)
            VALUES (?, ?)''', (''.join(code), generation_id))

    conn.commit()


if __name__ == '__main__':
    codes_iter = generate(5000000)
    add_to_db(codes_iter)
