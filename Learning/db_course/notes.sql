CREATE TABLE Users(
	name VARCHAR(128),
	email VARCHAR(128)
)

CREATE TABLE 'Album' (
'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
'title' VARCHAR(128) NOT NULL UNIQUE,
'artist_id' INTEGER
)


INSERT INTO Users(name, email) VALUES('Bogdanka', 'bogdanka@asd.com')
DELETE FROM Users WHERE email='bogdanka@asd.com'
UPDATE Users SET name='Ivan' WHERE email='ivancho@as.as'
SELECT * FROM Users WHERE name='Fred'  -- ( * means all attributes [columns]. Can put the col name instead)
SELECT * FROM Users
SELECT name,email FROM Users ORDER BY email

INSERT INTO Artists(name) VALUES('Led Zepelin');
INSERT INTO Artists(name) VALUES('AC/DC');

INSERT INTO Genre(name) VALUES('Rock');
INSERT INTO Genre(name) VALUES('Metal');

INSERT INTO Album(title, artist_id) VALUES('Who Made Who', 2);
INSERT INTO Album(title, artist_id) VALUES('|V', 1)

INSERT INTO Track(title, rating, len, count, album_id, genre_id) VALUES('Black Dog', 5, 297, 0, 2, 1);
INSERT INTO Track(title, rating, len, count, album_id, genre_id) VALUES('Stairway', 5, 482, 0, 2, 1);
INSERT INTO Track(title, rating, len, count, album_id, genre_id) VALUES('About to Rock', 5, 313, 0, 1, 2);
INSERT INTO Track(title, rating, len, count, album_id, genre_id) VALUES('Who Made Who', 5, 207, 0, 1, 2);

select Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id
select Album.title, Artist.name from Album join Artist where Album.artist_id = Artist.id
select Track.title, Album.title, Genre.name, Artist.name from Track join Album, Genre, Artist
    where Track.album_id = Album.id and Track.genre_id = Genre.id and Album.artist_id = Artist.id
select Track.title, Album.title, Genre.name, Artist.name from Track join Album join Genre join Artist
    on Track.album_id = Album.id and Track.genre_id = Genre.id and Album.artist_id = Artist.id