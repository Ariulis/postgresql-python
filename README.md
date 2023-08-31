### PostgreSQL with Python

env/.env file:
  - DB_NAME
  - DB_USER
  - DB_PASSWORD
  - DB_HOST

To run app:

```
docker-compose --env-file env/.env up --build
```
To get into the container 'db' (postgresql):

```
docker-compose exec db --username=<username> --dbname=<db name>
```

Tasks:
1. Add data to 'customer' table
2. Show all fields of 'customer' table
3. Show 'name' field of 'customer' table
4. Add data to 'product' table
5. Add data to 'product_photo' table
6. Show 'name' field of 'product' table and 'url' field of 'product_photo' table
7. Create photo for unexist product
8. Delete entry of 'product_photo' table
9. Update 'url' field in the 'product_photo' table
10. Create an order for one entry of 'customer' table
11. Add products to 'cart_product' table
12. Show customers with their orders sum:
  - name, cart_id, product_id, price
  - name, price
  - coalesce()
  - sorted by orders_sum
  - customers, which have orders_sum greater then 0
13. Avoiding problems with encoding in PostgreSQL
14. Select one entry but the second one
