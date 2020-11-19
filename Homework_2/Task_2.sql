create table if not exists Genre (
	Id serial primary key,
	Name varchar(40) not null unique
);

create table if not exists Artists (
	Id serial primary key,
	Name varchar(100) not null,
	GenreId integer references Genre(Id)
);

create table if not exists Albums (
	Id serial primary key,
	Name varchar(100) not null,
	Year integer not null,
	ArtistsId integer references Artists(Id)
);

create table if not exists Tracks (
	Id serial primary key,
	Name varchar(100) not null unique,
	Duration timestamp not null,
	AlbumsId integer references Albums(Id)
);


