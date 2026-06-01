Online Retail Sales Database Management System

Assessment Report

 1. Project Overview

The Online Retail Sales Database Management System is designed to manage customer orders, products, payments, and deliveries for an online retail business. The database enables efficient storage, retrieval, and analysis of sales data.

The project demonstrates the use of SQL concepts including:

* Database Design
* Primary and Foreign Keys
* Data Manipulation (INSERT, UPDATE, DELETE)
* Joins
* Aggregate Functions
* Group By and Having
* Subqueries
* Data Validation Queries
* Business Reports

---

 2. Database Design

The database consists of six tables:

 Customers

Stores customer information.

| Column          | Description                |
| --------------- | -------------------------- |
| customer_id     | Unique customer identifier |
| customer_name   | Customer name              |
| city            | Customer city              |
| state           | Customer state             |
| gender          | Gender                     |
| membership_type | Membership category        |

 Products

Stores product details.

| Column       | Description               |
| ------------ | ------------------------- |
| product_id   | Unique product identifier |
| product_name | Product name              |
| category     | Product category          |
| price        | Product price             |

 Orders

Stores order information.

| Column       | Description                |
| ------------ | -------------------------- |
| order_id     | Unique order identifier    |
| customer_id  | Customer placing the order |
| order_date   | Date of order              |
| order_status | Order status               |

 Order_Items

Stores products included in each order.

| Column     | Description            |
| ---------- | ---------------------- |
| item_id    | Unique item identifier |
| order_id   | Related order          |
| product_id | Related product        |
| quantity   | Quantity ordered       |

 Payments

Stores payment details.

| Column         | Description               |
| -------------- | ------------------------- |
| payment_id     | Unique payment identifier |
| order_id       | Related order             |
| payment_mode   | Payment method            |
| payment_status | Payment status            |
| amount         | Payment amount            |

 Deliveries

Stores delivery information.

| Column           | Description                |
| ---------------- | -------------------------- |
| delivery_id      | Unique delivery identifier |
| order_id         | Related order              |
| delivery_partner | Delivery service provider  |
| delivery_status  | Delivery status            |
| delivery_city    | Delivery destination city  |

---

 3. Table Relationships

The database follows a relational model.

Relationships

1. Customers → Orders

   * One customer can place many orders.
   * Foreign Key:
     orders.customer_id → customers.customer_id

2. Orders → Order_Items

   * One order can contain multiple products.
   * Foreign Key:
     order_items.order_id → orders.order_id

3. Products → Order_Items

   * One product can appear in many orders.
   * Foreign Key:
     order_items.product_id → products.product_id

4. Orders → Payments

   * Each order has a payment record.
   * Foreign Key:
     payments.order_id → orders.order_id

5. Orders → Deliveries

   * Each order has a delivery record.
   * Foreign Key:
     deliveries.order_id → orders.order_id

 Entity Relationship Flow

Customers
→ Orders
→ Order_Items
→ Products

Orders
→ Payments

Orders
→ Deliveries

---

 4. Reports Generated

The following business reports were created using SQL queries:

 Customer Reports

* Customer order details
* Customers with multiple orders
* Customers who never placed orders
* Customers whose spending exceeds average spending

 Product Reports

* Product-wise quantity sold
* Revenue by product category
* Products never ordered
* Products priced above average price

 Revenue Reports

* Total revenue by city
* Total revenue by customer
* Revenue by category

 Operational Reports

* Orders with successful payments
* Orders without payments
* Orders without deliveries
* Delivered orders with failed payments
* Cancelled orders with successful payments

 Data Validation Reports

* Invalid customer references
* Invalid product references
* Payments with NULL or zero amounts

---

 5. Key Insights from Reports

1. Revenue Analysis

   * Revenue can be analyzed by city, customer, and product category.
   * Electronics and high-value products contribute significantly to revenue.

2. Customer Behavior

   * Some customers place multiple orders and generate higher revenue.
   * Membership programs can be targeted toward frequent customers.

3. Product Performance

   * Product-wise sales quantity identifies best-selling products.
   * Unsold products can be identified for promotional activities.

4. Payment Monitoring

   * Failed and pending payments can be tracked.
   * Orders with successful payments can be distinguished from unpaid orders.

5. Delivery Tracking

   * Delivered, pending, and cancelled deliveries can be monitored.
   * Delivery performance can be evaluated by status reports.

6. Data Quality

   * Validation queries help identify missing references and incorrect records.
   * Foreign key relationships ensure data integrity.

---

6. Conclusion

This Online Retail Sales Database successfully demonstrates relational database design and SQL query implementation. The system supports customer management, order processing, product tracking, payment monitoring, delivery tracking, and business reporting. The generated reports provide valuable insights into sales performance, customer behavior, and operational efficiency.
