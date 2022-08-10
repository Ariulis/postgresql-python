create table if not exists customer(
  id serial primary key,
  name varchar(255),
  email varchar(255),
  phone varchar(50)
);

create table if not exists product(
  id serial primary key,
  title varchar(255),
  description text,
  price integer
);

create table if not exists product_photo(
  id serial primary key,
  url varchar(255),
  product_id integer references product(id)
);

create table if not exists cart(
  id serial primary key,
  customer_id integer references customer(id)
);

create table if not exists cart_product(
  cart_id integer references cart(id),
  product_id integer references product(id)
);