#imdb databank
use imdb;

SELECT 
    *
FROM
    movies m
        LEFT JOIN
    budget AS b ON b.movie = m.name AND m.year = b.year
WHERE
    b.movie IS NOT NULL;

SELECT 
    name, year, COUNT(*)
FROM
    movies
GROUP BY name , year
HAVING COUNT(*) > 1;

SELECT 
    COUNT(*)
FROM
    (SELECT 
        name, year, COUNT(*)
    FROM
        movies
    GROUP BY name , year
    HAVING COUNT(*) > 1) x;

#alter table names to use the same style guid 
ALTER TABLE imdb.genre
	CHANGE COLUMN `id` `name` INT(11) NOT NULL AUTO_INCREMENT , RENAME TO  `imdb`.`genres`;

#error 1452 - genres has director_id that do not exist in our directors table
DELETE FROM imdb.directors_genres WHERE director_id NOT IN (SELECT id FROM imdb.directors);


 describe imdb.directors;
 describe imdb.directors_genres;
 

#add foreign keys to existing tables
ALTER TABLE imdb.directors_genres
ADD FOREIGN key (director_id) REFERENCES imdb.directors(id);

SELECT 
    COUNT(*)
FROM
   imdb.movies;