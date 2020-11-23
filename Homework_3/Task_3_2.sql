create table if not exists Employee (
    id serial primary key,
    name varchar(100) not null,
    department varchar(100) not null,
    chief_id integer not null references Employee(id)
);