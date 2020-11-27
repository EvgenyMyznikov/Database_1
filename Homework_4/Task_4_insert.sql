INSERT INTO public.genre ("name")
VALUES ('Folk music'),
       ('Electronic music'),
       ('Rock music'),
       ('Pop music'),
       ('Country music');
INSERT INTO public.artist ("name")
VALUES ('Arkona'),
       ('Armin van Buuren'),
       ('Metallica'),
       ('Wolfheart'),
       ('My Dying Bride'),
       ('Eivør Pálsdóttir'),
       ('Wovenhand'),
       ('Umbra et Imago');
INSERT INTO public.album ("name", "year")
VALUES ('Khram', '2018-01-19'),
       ('Therapy', '2018-04-20'),
       ('S&M2', '2020-08-28'),
       ('Wolves Of Karelia', '2020-04-10'),
       ('The Ghost of Orion', '2020-03-06'),
       ('Segl', '2020-09-18'),
       ('Star Treatment', '2016-09-09'),
       ('Die Unsterblichen - Das zweite Buch', '2017-12-01');
INSERT INTO public.track ("name", duration, albumid)
VALUES ('Mantra', '03:51:00', 1),
       ('Shtorm', '05:11:00', 1),
       ('Therapy', '03:06:00', 2),
       ('Confusion', '06:41:00', 3),
       ('Halo on Fire', '08:18:00', 3),
       ('Reaper', '04:59:00', 4),
       ('Hail of Steel', '05:42:00', 4),
       ('Your Broken Shore', '07:41:00', 5),
       ('Tired of Tears', '08:35:00', 5),
       ('Let It Come', '03:34:00', 6);
INSERT INTO public.track ("name", duration, albumid)
VALUES ('Manasegl', '02:17:00', 6),
       ('Sleep on I', '03:01:00', 6),
       ('Horizon on Fire', '05:59:00', 4),
       ('Swaying Reed', '05:59:00', 7),
       ('Come Brave', '04:01:00', 7),
       ('The Animals Blues', '08:42:00', 8),
       ('Schandfleck', '05:14:00', 8);
INSERT INTO public.collection ("name", "year")
VALUES ('Best of Arkona', '2018-07-17'),
       ('Balance', '2019-10-25'),
       ('S&M2', '2020-08-28'),
       ('Wolfheart 13-20', '2020-11-25'),
       ('The Ghost of Orion - Live', '2020-07-21'),
       ('Segl - Live', '2020-09-21'),
       ('Star Treatment - Live', '2018-08-27'),
       ('Die Unsterblichen - Das zweite Buch', '2018-07-25');
INSERT INTO public.genreartist (genre_id, artist_id)
VALUES (1, 1),
       (2, 2),
       (3, 3),
       (3, 4),
       (3, 5),
       (4, 6),
       (5, 7),
       (3, 8);
INSERT INTO public.albumartist (album_id, artist_id)
VALUES (1, 1),
       (2, 2),
       (3, 3),
       (4, 4),
       (5, 5),
       (6, 6),
       (7, 7),
       (8, 8);
INSERT INTO public.collectiontrack (collection_id, track_id)
VALUES (1, 1),
       (1, 2),
       (2, 3),
       (3, 4),
       (3, 5),
       (4, 6),
       (4, 7),
       (5, 8),
       (5, 9),
       (6, 10);
INSERT INTO public.collectiontrack (collection_id, track_id)
VALUES (6, 11),
       (6, 12),
       (4, 13),
       (7, 14),
       (7, 15),
       (8, 16),
       (8, 17);
