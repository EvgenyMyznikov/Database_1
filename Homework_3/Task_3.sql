create table if not exists Genre
(
    Id   serial primary key,
    Name varchar(40) not null unique
);

create table if not exists Artist
(
    Id   serial primary key,
    Name varchar(100) not null
);

create table if not exists Album
(
    Id   serial primary key,
    Name varchar(100) not null,
    Year date         not null
);

create table if not exists Track
(
    Id       serial primary key,
    Name     varchar(100) not null unique,
    Duration time         not null,
    AlbumId  integer references Album (Id)
);

create table if not exists Collection
(
    Id   serial primary key,
    Name varchar(100) not null,
    Year date         not null
);

create table if not exists GenreArtist
(
    id        serial primary key,
    genre_id  integer not null references Genre (id),
    artist_id integer not null references Artist (id)
);

create table if not exists AlbumArtist
(
    id        serial primary key,
    album_id  integer references Album (id),
    artist_id integer references Artist (id)
);

create table if not exists CollectionTrack
(
    id            serial primary key,
    collection_id integer references Collection (id),
    track_id      integer references Track (id)
);


