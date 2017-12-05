"SELECT ALL"
SELECT * FROM celebs;
"CREATE TABLE"
CREATE TABLE celebs(id INTEGER, name TEXT, age INTEGER);
"INSERT VALUE"
INSERT INTO celebs (id, name, age) VALUES (1, 'Justin Bieber', 21);
SELECT * FROM celebs;

INSERT INTO celebs (id, name, age) VALUES (2, 'Beyonce Knowles', 33);
INSERT INTO celebs (id, name, age) VALUES (3, 'Jeremy Lin', 26);
INSERT INTO celebs (id, name, age) VALUES (4, 'Taylor Swift', 26);
SELECT name FROM celebs;

"ADD COLUMN"
ALTER TABLE celebs ADD COLUMN twitter_handle TEXT;
SELECT * FROM celebs;
"UPDATE SET DELETE"
UPDATE celebs
SET twitter_handle = '@taylorswift13'
WHERE id = 4;

DELETE FROM celebs WHERE twitter_handle IS NULL;
SELECT * FROM celebs;
