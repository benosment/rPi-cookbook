drop table if exists recipes;
create table recipes (
  id integer primary key autoincrement,
  title text not null,
  ingredients text not null,
  preperation_time text not null,
  directions text not null,
  num_portions text not null,
  category text not null,
  src text not null,
  date_created text not null,
  date_updated text not null
);