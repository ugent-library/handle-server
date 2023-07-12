create table if not exists nas(na text not null, primary key(na));
alter table nas owner to handle;
insert into nas (na) values ('0.NA/1854');
