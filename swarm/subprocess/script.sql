USE djangoTest;
DROP TABLE IF EXISTS music;
CREATE TABLE music(id INT AUTO_INCREMENT PRIMARY KEY,singer TEXT, song TEXT, genre TEXT);
INSERT INTO music (singer, song, genre) VALUES('Mike', "talking to the moon", "romantic");
INSERT INTO music (singer, song, genre) VALUES('Jorge', "i swear", "romantic");
INSERT INTO music (singer, song, genre) VALUES('Paul', "paradise", "rock");
