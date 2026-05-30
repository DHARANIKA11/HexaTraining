CREATE TABLE products
(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(10,2),
    stock_quantity INT,
    supplier_city VARCHAR(30)
);
INSERT INTO products VALUES

(1,'Laptop','Electronics',55000,10,'Hyderabad'),

(2,'Mobile','Electronics',25000,25,'Bangalore'),

(3,'Printer','Electronics',18000,8,'Pune'),

(4,'Office Chair','Furniture',7500,15,'Mumbai'),

(5,'Desk','Furniture',12000,5,'Chennai'),

(6,'Notebook','Stationery',80,200,'Hyderabad'),

(7,'Pen','Stationery',20,500,'Delhi'),

(8,'Water Bottle','Accessories',500,50,'Bangalore');

select * from products;
 