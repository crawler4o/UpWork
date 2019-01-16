import xml.etree.ElementTree as ElTr
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

fname = 'Library.xml'


def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


stuff = ElTr.parse(fname)
all_tracks = stuff.findall('dict/dict/dict')
print('Dict count:', len(all_tracks))
for entry in all_tracks:
    if lookup(entry, 'Track ID') is None:
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None or genre is None:
        continue

    print(name, artist, album, genre, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', (artist, ))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', (genre, ))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, genre_id, len, rating, count) 
            VALUES ( ?, ?, ?, ?, ?, ? )''', (name, album_id, genre_id, length, rating, count))

    conn.commit()
