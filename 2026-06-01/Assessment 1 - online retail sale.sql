CREATE DATABASE retail_capstone_db;
USE retail_capstone_db;

CREATE TABLE customers
(
customer_id INT PRIMARY KEY,
customer_name VARCHAR(100),
city VARCHAR(50),
state VARCHAR(50),
gender VARCHAR(10),
membership_type VARCHAR(30)
);

CREATE TABLE products
(
product_id INT PRIMARY KEY,
product_name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10,2)
); 

CREATE TABLE orders
(
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE,
order_status VARCHAR(30)
); 


CREATE TABLE order_items
(
item_id INT PRIMARY KEY,
order_id INT,
product_id INT,
quantity INT
); 

CREATE TABLE payments
(
payment_id INT PRIMARY KEY,
order_id INT,

payment_mode VARCHAR(30),
payment_status VARCHAR(30),
amount DECIMAL(10,2)
); 

CREATE TABLE deliveries
(
delivery_id INT PRIMARY KEY,
order_id INT,
delivery_partner VARCHAR(50),
delivery_status VARCHAR(30),
delivery_city VARCHAR(50)
); 

INSERT INTO customers VALUES
(1, 'Aarav Sharma', 'Mumbai', 'Maharashtra', 'Male', 'Gold'),
(2, 'Priya Nair', 'Chennai', 'Tamil Nadu', 'Female', 'Silver'),
(3, 'Rahul Verma', 'Delhi', 'Delhi', 'Male', 'Platinum'),
(4, 'Sneha Reddy', 'Hyderabad', 'Telangana', 'Female', 'Gold'),
(5, 'Vikram Singh', 'Jaipur', 'Rajasthan', 'Male', 'Silver'),
(6, 'Ananya Das', 'Kolkata', 'West Bengal', 'Female', 'Platinum'),
(7, 'Karan Patel', 'Ahmedabad', 'Gujarat', 'Male', 'Gold'),
(8, 'Meera Iyer', 'Bengaluru', 'Karnataka', 'Female', 'Silver'),
(9, 'Arjun Kumar', 'Lucknow', 'Uttar Pradesh', 'Male', 'Gold'),
(10, 'Divya Menon', 'Kochi', 'Kerala', 'Female', 'Platinum'); 

select * from customers; 

INSERT INTO products VALUES
(1, 'Laptop', 'Electronics', 55000.00),
(2, 'Smartphone', 'Electronics', 25000.00),
(3, 'Headphones', 'Electronics', 2000.00),
(4, 'Office Chair', 'Furniture', 7500.00),
(5, 'Study Table', 'Furniture', 12000.00),
(6, 'Refrigerator', 'Appliances', 35000.00),
(7, 'Washing Machine', 'Appliances', 28000.00),
(8, 'Microwave Oven', 'Appliances', 10000.00),
(9, 'Backpack', 'Accessories', 1500.00),
(10, 'Water Bottle', 'Accessories', 500.00); 

select * from products; 

INSERT INTO orders VALUES
(101, 1, '2026-01-05', 'Delivered'),
(102, 2, '2026-01-08', 'Shipped'),
(103, 3, '2026-01-10', 'Delivered'),
(104, 4, '2026-01-12', 'Pending'),
(105, 5, '2026-01-15', 'Cancelled'),
(106, 6, '2026-01-18', 'Delivered'),
(107, 7, '2026-01-20', 'Shipped'),
(108, 8, '2026-01-22', 'Delivered'),
(109, 9, '2026-01-25', 'Pending'),
(110, 10, '2026-01-28', 'Delivered'),
(111, 1, '2026-02-01', 'Shipped'),
(112, 3, '2026-02-03', 'Delivered'),
(113, 5, '2026-02-05', 'Pending'),
(114, 7, '2026-02-07', 'Delivered'),
(115, 9, '2026-02-10', 'Cancelled'); 

select * from orders; 

INSERT INTO order_items VALUES
(1, 101, 1, 1),
(2, 101, 3, 2),
(3, 102, 2, 1),
(4, 103, 4, 1),
(5, 103, 9, 3),
(6, 104, 5, 1),
(7, 105, 10, 5),
(8, 106, 6, 1),
(9, 107, 7, 1),
(10, 108, 8, 2),
(11, 109, 3, 1),
(12, 110, 1, 1),
(13, 111, 2, 2),
(14, 111, 9, 1),
(15, 112, 4, 1),
(16, 113, 5, 2),
(17, 114, 6, 1),
(18, 114, 10, 4),
(19, 115, 7, 1),
(20, 115, 8, 1); 

select * from order_items ; 
INSERT INTO payments VALUES
(1, 101, 'Credit Card', 'Paid', 59000.00),
(2, 102, 'UPI', 'Paid', 25000.00),
(3, 103, 'Debit Card', 'Paid', 16500.00),
(4, 104, 'Net Banking', 'Pending', 12000.00),
(5, 105, 'UPI', 'Failed', 2500.00),
(6, 106, 'Credit Card', 'Paid', 35000.00),
(7, 107, 'Debit Card', 'Paid', 28000.00),
(8, 108, 'UPI', 'Paid', 20000.00),
(9, 109, 'Cash on Delivery', 'Pending', 2000.00),
(10, 110, 'Credit Card', 'Paid', 55000.00),
(11, 111, 'UPI', 'Paid', 51500.00),
(12, 112, 'Debit Card', 'Paid', 7500.00),
(13, 113, 'Net Banking', 'Pending', 24000.00),
(14, 114, 'Credit Card', 'Paid', 37000.00),
(15, 115, 'UPI', 'Failed', 38000.00);

select * from payments; 

INSERT INTO deliveries VALUES
(1, 101, 'BlueDart', 'Delivered', 'Mumbai'),
(2, 102, 'Delhivery', 'In Transit', 'Chennai'),
(3, 103, 'Ecom Express', 'Delivered', 'Delhi'),
(4, 104, 'DTDC', 'Pending', 'Hyderabad'),
(5, 105, 'BlueDart', 'Cancelled', 'Jaipur'),
(6, 106, 'Delhivery', 'Delivered', 'Kolkata'),
(7, 107, 'Ecom Express', 'Out for Delivery', 'Ahmedabad'),
(8, 108, 'DTDC', 'Delivered', 'Bengaluru'),
(9, 109, 'BlueDart', 'Pending', 'Lucknow'),
(10, 110, 'Delhivery', 'Delivered', 'Kochi'),
(11, 111, 'Ecom Express', 'In Transit', 'Mumbai'),
(12, 112, 'DTDC', 'Delivered', 'Delhi'),
(13, 113, 'BlueDart', 'Pending', 'Jaipur'),
(14, 114, 'Delhivery', 'Delivered', 'Ahmedabad'),
(15, 115, 'Ecom Express', 'Cancelled', 'Lucknow'); 

select * from payments; 
ALTER TABLE orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id)
REFERENCES customers(customer_id); 
select * from orders; 

ALTER TABLE order_items
ADD CONSTRAINT fk_orderitems_product
FOREIGN KEY (product_id)
REFERENCES products(product_id); 


ALTER TABLE payments
ADD CONSTRAINT fk_payments_order
FOREIGN KEY (order_id)
REFERENCES orders(order_id); 

ALTER TABLE deliveries
ADD CONSTRAINT fk_deliveries_order
FOREIGN KEY (order_id)
REFERENCES orders(order_id); 

select * from customers; 
select customer_name, city, membership_type from customers; 
select * from products order by price desc; 
select customer_name from customers where city = 'Hyderabad' ; 
select * from customers where city = 'Hyderabad' ; 
select * from customers where membership_type = 'gold'; 
select * from products where price between 500 and 700; 
select * from products where category = 'Electronics' and 'fashion' ; 
SELECT *
FROM orders
WHERE order_date > '2026-01-01'; 
select * from payments ; 
select * from payments where payment_mode = 'UPI'; 
select * from deliveries ;  
select * from deliveries where delivery_status = 'Pending' ; 

select count(*) from customers; 
select count(*) from orders ; 
select count(*) from products ; 
select sum(amount) as total_revenue from payments where payment_status = 'Paid'; 
select avg(amount) from payments; 
select max(amount) from payments; 
select min(amount) from payments; 
select count(*) from customers order by city ; 
select count(*) from products order by category; 
select count(*) from orders order by order_status; 
SELECT c.customer_name,
       o.order_id,
       o.order_date
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id; 
select order_id, product_name , quantity, price from products P join orders o where P.product_id = o.order_id; 
SELECT c.customer_name,
       p.product_name,
       oi.quantity,
       o.order_date
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id; 

select *  from orders; 
select * from payments; 
select * from deliveries; 
select o.order_id , d.delivery_partner, d.delivery_status from orders o join deliveries d on o.order_id = d.order_id ; 
SELECT
    c.customer_name,
    c.city,
    o.order_id,
    o.order_date,
    p.product_name,
    p.category,
    oi.quantity,
    p.price,
    pay.payment_status,
    d.delivery_status
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id
JOIN payments pay
    ON o.order_id = pay.order_id
JOIN deliveries d
    ON o.order_id = d.order_id; 
select * from customers; 
SELECT c.city,
       SUM(p.amount) AS total_revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN payments p
    ON o.order_id = p.order_id
WHERE p.payment_status = 'Paid'
GROUP BY c.city; 
SELECT c.customer_id,
       c.customer_name,
       SUM(p.amount) AS total_revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN payments p
    ON o.order_id = p.order_id
WHERE p.payment_status = 'Paid'
GROUP BY c.customer_id, c.customer_name;  

SELECT p.product_id,
       p.product_name,
       SUM(oi.quantity) AS total_quantity_sold
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name; 

SELECT p.category,
       SUM(oi.quantity * p.price) AS revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.category; 

SELECT c.customer_id,
       c.customer_name,
       COUNT(o.order_id) AS number_of_orders
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name; 

SELECT c.customer_id,
       c.customer_name,
       COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(o.order_id) > 1; 

SELECT p.category,
       SUM(oi.quantity * p.price) AS revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.category
HAVING SUM(oi.quantity * p.price) > 10000; 

SELECT city,
       COUNT(customer_id) AS total_customers
FROM customers
GROUP BY city
HAVING COUNT(customer_id) > 2; 

SELECT p.product_id,
       p.product_name,
       SUM(oi.quantity) AS total_quantity_sold
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
HAVING SUM(oi.quantity) > 3; 

SELECT *
FROM customers
WHERE customer_id IN
(
    SELECT customer_id
    FROM orders
); 

select * from orders; 
SELECT *
FROM customers
WHERE customer_id NOT IN
(
    SELECT customer_id
    FROM orders
); 

SELECT *
FROM products
WHERE product_id NOT IN
(
    SELECT product_id
    FROM order_items
); 

SELECT order_id,
       payment_mode,
       payment_status,
       amount
FROM payments
WHERE amount >
(
    SELECT AVG(amount)
    FROM payments
); 

SELECT c.customer_id,
       c.customer_name,
       p.amount
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN payments p
    ON o.order_id = p.order_id
WHERE p.amount =
(
    SELECT MAX(amount)
    FROM payments
); 

SELECT *
FROM products
WHERE price >
(
    SELECT AVG(price)
    FROM products
); 

SELECT DISTINCT c.customer_id,
                c.customer_name
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id
WHERE p.category = 'Electronics'; 

SELECT *
FROM orders
WHERE order_id IN
(
    SELECT order_id
    FROM payments
    WHERE payment_status = 'Paid'
); 

SELECT *
FROM orders
WHERE order_id IN
(
    SELECT order_id
    FROM deliveries
    WHERE delivery_status <> 'Delivered'
);  

SELECT c.customer_id,
       c.customer_name,
       SUM(p.amount) AS total_spending
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN payments p
    ON o.order_id = p.order_id
WHERE p.payment_status = 'Paid'
GROUP BY c.customer_id, c.customer_name
HAVING SUM(p.amount) >
(
    SELECT AVG(customer_total)
    FROM
    (
        SELECT SUM(p2.amount) AS customer_total
        FROM orders o2
        JOIN payments p2
            ON o2.order_id = p2.order_id
        WHERE p2.payment_status = 'Paid'
        GROUP BY o2.customer_id
    ) AS avg_spending
); 

SELECT *
FROM orders o
WHERE NOT EXISTS
(
    SELECT 1
    FROM payments p
    WHERE p.order_id = o.order_id
); 

SELECT *
FROM orders
WHERE order_id NOT IN
(
    SELECT order_id
    FROM payments
); 
select * from payments;
select * from payments where amount is null or amount = 0; 
SELECT o.order_id,
       o.order_status,
       p.payment_status
FROM orders o
JOIN payments p
    ON o.order_id = p.order_id
WHERE o.order_status = 'Cancelled'
  AND p.payment_status = 'Paid'; 
  
  SELECT o.order_id,
       d.delivery_status,
       p.payment_status
FROM orders o
JOIN deliveries d
    ON o.order_id = d.order_id
JOIN payments p
    ON o.order_id = p.order_id
WHERE d.delivery_status = 'Delivered'
  AND p.payment_status = 'Failed'; 
  
SELECT *
FROM order_items oi
WHERE NOT EXISTS
(
    SELECT 1
    FROM products p
    WHERE p.product_id = oi.product_id
); 

SELECT *
FROM orders o
WHERE NOT EXISTS
(
    SELECT 1
    FROM customers c
    WHERE c.customer_id = o.customer_id
);