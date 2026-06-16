USE expense_db;
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100)
);
CREATE TABLE expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    category_id INT,
    amount DECIMAL(10,2),
    expense_date DATE,
    note VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

SHOW TABLES;
DESCRIBE users;

INSERT INTO users (name, email)
VALUES ('sangyan', 'sangyan@gmail.com');

INSERT INTO categories (category_name)
VALUES ('Food'), ('Travel'), ('Shopping');

INSERT INTO expenses (user_id, category_id, amount, expense_date, note)
VALUES (1, 1, 250.00, '2026-06-01', 'Lunch');

SELECT * FROM users;
SELECT * FROM categories;
SELECT * FROM expenses;

SELECT e.expense_id, u.name, c.category_name, e.amount
FROM expenses e
JOIN users u ON e.user_id = u.user_id
JOIN categories c ON e.category_id = c.category_id;

UPDATE expenses
SET amount = 300
WHERE expense_id = 1;

DELETE FROM expenses
WHERE expense_id = 1;

DELIMITER $$

CREATE PROCEDURE monthly_expense_total()
BEGIN
    SELECT 
        c.category_name,
        MONTH(e.expense_date) AS month,
        SUM(e.amount) AS total_amount
    FROM expenses e
    JOIN categories c ON e.category_id = c.category_id
    GROUP BY c.category_name, MONTH(e.expense_date);
END $$

DELIMITER ;

CALL monthly_expense_total();