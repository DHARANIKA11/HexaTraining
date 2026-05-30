use retail_db; 
CREATE TABLE books
(
book_id INT PRIMARY KEY,
book_title VARCHAR(100),
category VARCHAR(50),
author VARCHAR(50),
price DECIMAL(10,2),
stock INT,
published_year INT
);

INSERT INTO books VALUES
(1, 'Python Basics', 'Programming', 'Ravi Kumar', 550, 30, 2021),
(2, 'Advanced SQL', 'Database', 'Priya Sharma', 750, 15, 2020),
(3, 'Data Engineering Guide', 'Data', 'Amit Verma', 1200, 10, 2023),
(4, 'Machine Learning Start', 'AI', 'Neha Reddy', 950, 8, 2022),
(5, 'Excel for Business', 'Business', 'Kiran Rao', 400, 50, 2019),
(6, 'Power BI Reports', 'Data', 'Sneha Patel', 850, 12, 2021),
(7, 'Java Fundamentals', 'Programming', 'Arjun Mehta', 600, 20, 2018),
(8, 'Cloud Basics', 'Cloud', 'Rahul Nair', 700, 18, 2022),
(9, 'SQL Interview Prep', 'Database', 'Farhan Ali', 500, 25, 2024),
(10, 'AI for Beginners', 'AI', 'Meera Singh', 650, 5, 2023);

select * from books; 
select 
book_title,
category,
price from books;

select distinct category from books; 
select * from books where category = 'programming'; 
select * from books where price > 700; 
select * from books where stock <= 15; 
select * from books where category in ('programming', 'database', 'ai'); 
select * from books where price between 500 and 900 ; 
SELECT *
FROM books
WHERE book_title LIKE '%SQL%';
SELECT *
FROM books
WHERE book_title LIKE 'DATA%'; 

select price from books order by price desc; 
select * from books order by category asc , price desc; 
SELECT COUNT(*) AS total_books
FROM books; 

SELECT MAX(price) AS highest_price
FROM books; 

select min(price) as lowest_price from books;  
select avg(price) as average_price from books; 
SELECT SUM(stock) AS total_stock
FROM books; 
SELECT category, COUNT(*) AS number_of_books
FROM books
GROUP BY category; 
select avg(price) as average_price from books group by category ;
select sum(stock) as tot_stock from books group by category ; 
SELECT category, COUNT(*) AS number_of_books
FROM books
GROUP BY category
HAVING COUNT(*) > 1; 

SELECT category, AVG(price) AS average_price
FROM books
GROUP BY category
HAVING AVG(price) > 700; 

CREATE TABLE departments
(
department_id INT PRIMARY KEY,
department_name VARCHAR(50),
location VARCHAR(50)
);

CREATE TABLE employees
(
employee_id INT PRIMARY KEY,
employee_name VARCHAR(50),
department_id INT,
salary DECIMAL(10,2),
city VARCHAR(50),
manager_id INT
);

INSERT INTO departments VALUES
(10, 'IT', 'Hyderabad'),
(20, 'HR', 'Bangalore'),
(30, 'Finance', 'Mumbai'),
(40, 'Sales', 'Delhi'),
(50, 'Marketing', NULL);

INSERT INTO employees VALUES
(101, 'Rahul Sharma', 10, 75000, 'Hyderabad', 201),
(102, 'Priya Reddy', 10, 85000, 'Bangalore', 201),
(103, 'Amit Kumar', 20, 55000, NULL, 202),
(104, 'Sneha Patel', 30, 65000, 'Mumbai', 203),
(105, 'Arjun Verma', NULL, 60000, 'Chennai', 204),
(106, 'Neha Singh', 60, 50000, 'Delhi', NULL),
(107, 'Farhan Ali', 40, NULL, 'Hyderabad', 205),
(108, 'Meera Nair', 10, 90000, 'Pune', 201);

SELECT e.employee_name,
       e.salary,
       d.department_name,
       d.location
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id; 

SELECT e.employee_name,
       e.salary,
       d.department_name,
       d.location
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id; 

SELECT e.employee_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id
WHERE d.department_id IS NULL; 

SELECT e.employee_name,
       e.salary,
       d.department_name,
       d.location
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id; 


SELECT d.department_name
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
WHERE e.employee_id IS NULL; 

SELECT *
FROM employees 
WHERE salary IS NULL; 

SELECT *
FROM departments 
WHERE location IS NULL; 

SELECT department_id,
       COUNT(*) AS employee_count
FROM employees
GROUP BY department_id; 

SELECT d.department_name,
       AVG(e.salary) AS average_salary
FROM departments d
JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name; 

SELECT d.department_name,
       COUNT(e.employee_id) AS employee_count
FROM departments d
JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name
HAVING COUNT(e.employee_id) > 2; 

SELECT d.department_name,
       MAX(e.salary) AS highest_salary
FROM departments d
JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name;

CREATE TABLE customers_new
(
customer_id INT PRIMARY KEY,
customer_name VARCHAR(50),
city VARCHAR(50),
membership_type VARCHAR(30)
); 

CREATE TABLE payments
(
payment_id INT PRIMARY KEY,
customer_id INT,
amount DECIMAL(10,2),
payment_mode VARCHAR(30),
payment_status VARCHAR(30)
); 

INSERT INTO customers_new VALUES
(1, 'Ramesh Gupta', 'Hyderabad', 'Gold'),
(2, 'Sana Khan', 'Bangalore', 'Silver'),
(3, 'John Mathew', 'Mumbai', 'Gold'),
(4, 'Ayesha Begum', 'Chennai', 'Bronze'),
(5, 'Vikram Rao', 'Delhi', 'Silver'),
(6, 'Divya Sharma', 'Pune', NULL);

INSERT INTO payments VALUES
(1001, 1, 15000, 'UPI', 'Success'),
(1002, 1, 8000, 'Card', 'Success'),
(1003, 2, 5000, 'Cash', 'Pending'),
(1004, 3, 22000, 'UPI', 'Success'),
(1005, 7, 12000, 'Card', 'Failed'),
(1006, NULL, 3000, 'Cash', 'Pending'),
(1007, 4, NULL, 'UPI', 'Success'),
(1008, 5, 7000, NULL, 'Success'); 

SELECT c.customer_name,
       p.payment_id,
       p.amount
FROM customers c
INNER JOIN payments p
ON c.customer_id = p.customer_id; 

SELECT customer_name
FROM customers
WHERE customer_id NOT IN (
    SELECT customer_id
    FROM payments
); 

SELECT *
FROM payments
WHERE amount > (
    SELECT AVG(amount)
    FROM payments
);

SELECT c.customer_name, p.amount
FROM customers c
JOIN payments p
ON c.customer_id = p.customer_id
WHERE p.amount = (
    SELECT MAX(amount)
    FROM payments
); 

SELECT DISTINCT c.customer_name
FROM customers c
INNER JOIN payments p
ON c.customer_id = p.customer_id
WHERE c.customer_type = 'Gold'; 

SELECT c.customer_name,
       SUM(p.amount) AS total_payment
FROM customers c
JOIN payments p
ON c.customer_id = p.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(p.amount) > 10000; 

SELECT c.customer_name,
       SUM(p.amount) AS total_payment
FROM customers c
JOIN payments p
ON c.customer_id = p.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(p.amount) > 10000; 

SELECT p.payment_id
FROM payments p
LEFT JOIN customers c
ON p.customer_id = c.customer_id
WHERE c.customer_id IS NULL; 

SELECT c.customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM payments p
    WHERE p.customer_id = c.customer_id
); 

SELECT c.customer_name
FROM customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM payments p
    WHERE p.customer_id = c.customer_id
); 

SELECT c.customer_name,
       p.amount
FROM customers c
JOIN payments p
ON c.customer_id = p.customer_id
WHERE p.amount > ALL (
    SELECT amount
    FROM payments
    WHERE customer_id = 2
);