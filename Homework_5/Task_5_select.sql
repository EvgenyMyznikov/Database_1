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
SELECT name FROM artist
WHERE id IN(
    SELECT artist_id FROM albumartist
    WHERE album_id IN(
        SELECT id FROM album
        WHERE release_year < '2020-01-01'));

-- 5.названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
SELECT name FROM collection
WHERE id IN(
    SELECT track_id FROM collectiontrack
    WHERE track_id IN(
        SELECT id FROM track
        WHERE id IN(
            SELECT artist_id FROM albumartist
            WHERE artist_id IN(
                SELECT id FROM artist
                WHERE id = 3))));

-- 6.название альбомов, в которых присутствуют исполнители более 1 жанра;
SELECT name FROM album
WHERE id IN(
    SELECT artist_id FROM albumartist
    WHERE artist_id IN(
        SELECT artist_id FROM genreartist
        GROUP BY artist_id
        HAVING COUNT(genre_id) > 1));

-- 7.наименование треков, которые не входят в сборники;
SELECT name FROM track
WHERE id NOT IN(
    SELECT track_id FROM collectiontrack
    GROUP BY track_id);

-- 8.исполнителя(-ей), написавшего самый короткий по продолжительности трек;
SELECT name FROM artist
WHERE id in(
    SELECT artist_id FROM albumartist
    WHERE album_id = (
        SELECT albumid FROM track
        WHERE duration IN(
            SELECT MIN(duration) FROM track)));

-- 9.название альбомов, содержащих наименьшее количество треков.
SELECT name FROM album
WHERE id in(
    SELECT COUNT(albumid) FROM track
    GROUP BY albumid
    ORDER BY albumid DESC
    LIMIT 1);

