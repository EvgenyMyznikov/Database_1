SELECT name, release_year
FROM album
WHERE release_year IN('2018-01-01', '2018-12-31');

SELECT name, duration
FROM track
WHERE duration = (SELECT MAX(duration) FROM track);

SELECT name
FROM track
WHERE duration >= '03:30';

SELECT name
FROM collection
WHERE release_year IN('2018-01-01', '2020-12-31')

SELECT name
FROM artist 
WHERE name NOT LIKE '% %';

SELECT name
FROM track
WHERE name LIKE '%мой%';

SELECT name
FROM track
WHERE name LIKE '%my%';

