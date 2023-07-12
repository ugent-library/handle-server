create table if not exists handles (
  handle text not null,
  idx integer not null,
  type text,
  data bytea,
  ttl_type smallint,
  ttl integer,
  timestamp integer,
  refs bytea,
  admin_read boolean,
  admin_write boolean,
  pub_read boolean,
  pub_write boolean,
  PRIMARY KEY(handle, idx)
);
alter table handles owner to handle;
