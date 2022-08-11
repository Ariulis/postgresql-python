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

Tasks:
1. Add data to 'customer' table
2. Show all fields of 'customer' table
3. Show 'name' field of 'customer' table
4. Add data to 'product_photo' table
5. Show 'name' field of 'product' table and 'url' field of 'product_photo' table
6. Create photo for unexist product
7. Delete entry of 'product_photo' table
8. Update 'url' field in the 'product_photo' table
9. Create an order for one entry of 'customer' table
10. Add products to 'cart_product' table
11. Show customers with their orders sum:
  - name, cart_id, product_id, price
  - name, price
  - coalesce()
  - sorted by orders_sum
  - customers, which have orders_sum greater then 0
12. Avoiding problems with encoding in PostgreSQL
13. Select one entry but the second one