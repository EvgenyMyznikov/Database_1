-- 1.количество исполнителей в каждом жанре;
SELECT genre_id, COUNT(artist_id) FROM genreartist
GROUP BY genre_id;

-- 2.количество треков, вошедших в альбомы 2019-2020 годов;
SELECT COUNT(id) FROM track
WHERE albumid IN(
	SELECT id FROM album
	WHERE release_year BETWEEN '2019-01-01' AND '2020-12-31');

-- 3.средняя продолжительность треков по каждому альбому;
SELECT albumid, AVG(duration) FROM track
GROUP BY albumid;

-- 4.все исполнители, которые не выпустили альбомы в 2020 году;
SELECT DISTINCT a.name FROM artist AS a
LEFT JOIN albumartist AS aa ON a.id = aa.id
LEFT JOIN album AS am ON aa.id = am.id
WHERE release_year < '2020-01-01';

-- 5.названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
SELECT DISTINCT c.name FROM collection AS c
LEFT JOIN artist AS a ON c.id = a.id
WHERE a.id = 3;

-- 6.название альбомов, в которых присутствуют исполнители более 1 жанра;
SELECT DISTINCT a.name FROM album AS a
LEFT JOIN albumartist AS aa ON a.id = aa.id
LEFT JOIN genreartist AS ga ON aa.id = ga.artist_id
GROUP BY a.name
HAVING COUNT(ga.artist_id) > 1;

-- 7.наименование треков, которые не входят в сборники;
SELECT t.name FROM track AS t
WHERE id NOT IN(
    SELECT ct.track_id FROM collectiontrack AS ct
	LEFT JOIN collection AS c ON ct.id = c.id
    GROUP BY ct.track_id);

-- 8.исполнителя(-ей), написавшего самый короткий по продолжительности трек;
SELECT a.name FROM artist AS a
WHERE id IN(
    SELECT aa.artist_id FROM albumartist AS aa
    LEFT JOIN track AS t ON aa.id = t.albumid
        WHERE duration IN(
            SELECT MIN(duration) FROM track));

-- 9.название альбомов, содержащих наименьшее количество треков.
SELECT DISTINCT a.name FROM album AS a
INNER JOIN track AS t ON a.id = t.albumid
WHERE albumid IN(
	SELECT COUNT(albumid) FROM track
	GROUP BY albumid
	ORDER BY albumid
	LIMIT 1);

