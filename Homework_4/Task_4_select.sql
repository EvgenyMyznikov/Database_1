SELECT name, year
FROM album
WHERE year = 2018;

SELECT name, duration
FROM track
WHERE duration = (SELECT MAX(duration) FROM track);

SELECT name
FROM track
WHERE duration >= '03:30';

SELECT name
FROM collection
WHERE year >= 2018
  AND year <= 2020;

SELECT name
FROM artist
WHERE name = (SELECT count(name) = 1 FROM artist);

SELECT name
FROM track
WHERE name LIKE '%мой%';

SELECT name
FROM track
WHERE name LIKE '%my%';

