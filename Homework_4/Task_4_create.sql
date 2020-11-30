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
    Release_year date       not null
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
    Release_year date         not null
);

create table if not exists GenreArtist
(
    Id        serial primary key,
    Genre_id  integer not null references Genre (id),
    Artist_id integer not null references Artist (id)
);

create table if not exists AlbumArtist
(
    Id        serial primary key,
    Album_id  integer references Album (id),
    Artist_id integer references Artist (id)
);

create table if not exists CollectionTrack
(
    Id            serial primary key,
    Collection_id integer references Collection (id),
    Track_id      integer references Track (id)
);


