create database hospital_db ;
use hospital_db; 

CREATE TABLE patients
(
patient_id INT PRIMARY KEY,
patient_name VARCHAR(100),
gender VARCHAR(10),
age INT,
city VARCHAR(50),
phone VARCHAR(15)
);

CREATE TABLE departments
(
department_id INT PRIMARY KEY,
department_name VARCHAR(100)
); 

CREATE TABLE doctors
(
doctor_id INT PRIMARY KEY,
doctor_name VARCHAR(100),
specialization VARCHAR(100),
department_id INT,
consultation_fee DECIMAL(10,2)
); 

CREATE TABLE appointments
(
appointment_id INT PRIMARY KEY,
patient_id INT,
doctor_id INT,
appointment_date DATE,
appointment_status VARCHAR(30)
); 

CREATE TABLE bills
(
bill_id INT PRIMARY KEY,
patient_id INT,
appointment_id INT,

bill_date DATE,
total_amount DECIMAL(10,2),
bill_status VARCHAR(30)
); 

CREATE TABLE payments
(
payment_id INT PRIMARY KEY,
bill_id INT,
payment_mode VARCHAR(30),
paid_amount DECIMAL(10,2),
payment_status VARCHAR(30)
); 

INSERT INTO patients
(patient_id, patient_name, gender, age, city, phone)
VALUES
(1, 'Arun Kumar', 'Male', 25, 'Chennai', '9876543210'),
(2, 'Priya Sharma', 'Female', 30, 'Bangalore', '9876543211'),
(3, 'Rahul Verma', 'Male', 45, 'Hyderabad', '9876543212'),
(4, 'Sneha Reddy', 'Female', 28, 'Mumbai', '9876543213'),
(5, 'Karthik Raj', 'Male', 35, 'Coimbatore', '9876543214'),
(6, 'Anjali Gupta', 'Female', 22, 'Delhi', '9876543215'),
(7, 'Vijay Kumar', 'Male', 50, 'Madurai', '9876543216'),
(8, 'Meena Patel', 'Female', 40, 'Ahmedabad', '9876543217'),
(9, 'Suresh Babu', 'Male', 33, 'Trichy', '9876543218'),
(10, 'Divya Nair', 'Female', 27, 'Kochi', '9876543219'),
(11, 'Ramesh Singh', 'Male', 60, 'Pune', '9876543220'),
(12, 'Lakshmi Devi', 'Female', 38, 'Salem', '9876543221');


INSERT INTO departments
(department_id, department_name)
VALUES
(1, 'Cardiology'),
(2, 'Neurology'),
(3, 'Orthopedics'),
(4, 'Pediatrics'),
(5, 'Dermatology'),
(6, 'Oncology'),
(7, 'Gynecology'),
(8, 'Emergency'); 

INSERT INTO doctors
(doctor_id, doctor_name, specialization, department_id, consultation_fee)
VALUES
(1, 'Dr. Ravi Kumar', 'Cardiologist', 1, 800.00),
(2, 'Dr. Priya Sharma', 'Neurologist', 2, 1000.00),
(3, 'Dr. Karthik Raj', 'Orthopedic Surgeon', 3, 900.00),
(4, 'Dr. Anjali Gupta', 'Pediatrician', 4, 700.00),
(5, 'Dr. Meena Patel', 'Dermatologist', 5, 650.00),
(6, 'Dr. Suresh Babu', 'Oncologist', 6, 1200.00),
(7, 'Dr. Lakshmi Devi', 'Gynecologist', 7, 850.00),
(8, 'Dr. Vijay Kumar', 'Emergency Physician', 8, 600.00); 

INSERT INTO appointments
(appointment_id, patient_id, doctor_id, appointment_date, appointment_status)
VALUES
(1, 1, 1, '2026-06-01', 'Completed'),
(2, 2, 2, '2026-06-02', 'Scheduled'),
(3, 3, 3, '2026-06-03', 'Scheduled'),
(4, 4, 4, '2026-06-04', 'Completed'),
(5, 5, 5, '2026-06-05', 'Cancelled'),
(6, 6, 6, '2026-06-06', 'Scheduled'),
(7, 7, 7, '2026-06-07', 'Completed'),
(8, 8, 8, '2026-06-08', 'Scheduled'),
(9, 9, 1, '2026-06-09', 'Completed'),
(10, 10, 2, '2026-06-10', 'Cancelled'),
(11, 11, 3, '2026-06-11', 'Scheduled'),
(12, 12, 4, '2026-06-12', 'Completed'),
(13, 1, 5, '2026-06-13', 'Scheduled'),
(14, 2, 6, '2026-06-14', 'Completed'),
(15, 3, 7, '2026-06-15', 'Cancelled'),
(16, 4, 8, '2026-06-16', 'Scheduled'),
(17, 5, 1, '2026-06-17', 'Completed'),
(18, 6, 2, '2026-06-18', 'Scheduled'),
(19, 7, 3, '2026-06-19', 'Completed'), 
(20, 8, 4, '2026-06-20', 'Scheduled'); 


INSERT INTO treatments
(treatment_id, appointment_id, treatment_name, treatment_cost)
VALUES
(1, 1, 'ECG Test', 1500.00),
(2, 2, 'Brain MRI', 5000.00),
(3, 3, 'Knee X-Ray', 1200.00),
(4, 4, 'Vaccination', 800.00),
(5, 5, 'Skin Allergy Test', 1800.00),
(6, 6, 'Chemotherapy Session', 10000.00),
(7, 7, 'Prenatal Checkup', 2000.00),
(8, 8, 'Emergency First Aid', 1500.00),
(9, 9, 'Heart Scan', 3500.00),
(10, 10, 'Neurological Assessment', 2500.00),
(11, 11, 'Fracture Treatment', 4000.00),
(12, 12, 'Child Health Screening', 1000.00),
(13, 13, 'Acne Treatment', 2200.00),
(14, 14, 'Cancer Screening', 4500.00),
(15, 15, 'Ultrasound Scan', 1800.00); 

INSERT INTO bills
(bill_id, patient_id, appointment_id, bill_date, total_amount, bill_status)
VALUES
(1, 1, 1, '2026-06-01', 2300.00, 'Paid'),
(2, 2, 2, '2026-06-02', 6000.00, 'Pending'),
(3, 3, 3, '2026-06-03', 2100.00, 'Paid'),
(4, 4, 4, '2026-06-04', 1500.00, 'Paid'),
(5, 5, 5, '2026-06-05', 2450.00, 'Cancelled'),
(6, 6, 6, '2026-06-06', 11200.00, 'Pending'),
(7, 7, 7, '2026-06-07', 2850.00, 'Paid'),
(8, 8, 8, '2026-06-08', 2100.00, 'Paid'),
(9, 9, 9, '2026-06-09', 4300.00, 'Pending'),
(10, 10, 10, '2026-06-10', 3500.00, 'Paid'),
(11, 11, 11, '2026-06-11', 4900.00, 'Pending'),
(12, 12, 12, '2026-06-12', 1700.00, 'Paid'),
(13, 1, 13, '2026-06-13', 2850.00, 'Pending'),
(14, 2, 14, '2026-06-14', 5500.00, 'Paid'),
(15, 3, 15, '2026-06-15', 2650.00, 'Pending'); 


INSERT INTO payments
(payment_id, bill_id, payment_mode, paid_amount, payment_status)
VALUES
(1, 1, 'Cash', 2300.00, 'Success'),
(2, 2, 'Credit Card', 3000.00, 'Partial'),
(3, 3, 'UPI', 2100.00, 'Success'),
(4, 4, 'Debit Card', 1500.00, 'Success'),
(5, 5, 'Cash', 0.00, 'Failed'),
(6, 6, 'Net Banking', 5000.00, 'Partial'),
(7, 7, 'UPI', 2850.00, 'Success'),
(8, 8, 'Credit Card', 2100.00, 'Success'),
(9, 9, 'Debit Card', 2000.00, 'Partial'),
(10, 10, 'Cash', 3500.00, 'Success'),
(11, 11, 'UPI', 2500.00, 'Partial'),
(12, 12, 'Net Banking', 1700.00, 'Success'),
(13, 13, 'Credit Card', 1000.00, 'Partial'),
(14, 14, 'UPI', 5500.00, 'Success'),
(15, 15, 'Debit Card', 1500.00, 'Partial'); 

select * from patients; 
select * from doctors; 
select * from bills;
select * from appointments;
select * from patients where city = 'Hyderabad'; 
select * from doctors where specialization= 'cardiologist' 
select * FROM appointments where appointment_date > '2026-01-01';  
select * from appointments where appointment_status = 'cancelled' ; 
select * from bills where total_amount > 5000; 
select * from payments where payment_mode = 'UPI';
select * from payments; 
select * from patients where age between 30 and 50 ; 
select * from doctors where consultation_fee > 800; 

select count(*) from patients; 
select count(*) from doctors; 
select avg(consultation_fee) from doctors; 
select max(consultation_fee) from doctors; 
select sum(consultation_fee) from doctors; 
select sum(total_amount) from bills; 
select total_amount from bills where bill_status = 'Paid'; 
select sum(total_amount) from bills where bill_status = 'Paid'; 
select count(*) from patients order by city; 
select count(*) from  doctors group by specialization; 
select count(*) from appointments group by appointment_status ; 

SELECT p.patient_name,
       a.appointment_date,
       a.appointment_status
FROM patients p
JOIN appointments a
ON p.patient_id = a.patient_id; 

SELECT d.doctor_name,
       dp.department_name
FROM doctors d
JOIN departments dp
ON d.department_id = dp.department_id; 

SELECT p.patient_name,
       d.doctor_name,
       a.appointment_date
FROM appointments a
JOIN patients p
ON a.patient_id = p.patient_id
JOIN doctors d
ON a.doctor_id = d.doctor_id; 

SELECT appointment_id,
       treatment_name,
       treatment_cost
FROM treatments; 

SELECT b.bill_id,
       p.patient_name,
       b.total_amount
FROM bills b
JOIN patients p
ON b.patient_id = p.patient_id; 

SELECT bill_id,
       payment_mode,
       paid_amount,
       payment_status
FROM payments; 

SELECT a.appointment_id,
       p.patient_name,
       d.doctor_name,
       dp.department_name,
       a.appointment_date,
       a.appointment_status,
       t.treatment_name,
       t.treatment_cost,
       b.bill_id,
       b.total_amount,
       py.payment_mode,
       py.paid_amount,
       py.payment_status
FROM appointments a
JOIN patients p
ON a.patient_id = p.patient_id
JOIN doctors d
ON a.doctor_id = d.doctor_id
JOIN departments dp
ON d.department_id = dp.department_id
LEFT JOIN treatments t
ON a.appointment_id = t.appointment_id
LEFT JOIN bills b
ON a.appointment_id = b.appointment_id
LEFT JOIN payments py
ON b.bill_id = py.bill_id; 
select * from appointments;
select count(appointment_date) from appointments group by doctor_id; 
SELECT dp.department_name,
       COUNT(a.appointment_id) AS total_appointments
FROM appointments a
JOIN doctors d
ON a.doctor_id = d.doctor_id
JOIN departments dp
ON d.department_id = dp.department_id
GROUP BY dp.department_name; 

SELECT dp.department_name,
       SUM(b.total_amount) AS total_revenue
FROM bills b
JOIN appointments a
ON b.appointment_id = a.appointment_id
JOIN doctors d
ON a.doctor_id = d.doctor_id
JOIN departments dp
ON d.department_id = dp.department_id
GROUP BY dp.department_name; 

SELECT treatment_name,
       SUM(treatment_cost) AS total_treatment_cost
FROM treatments
GROUP BY treatment_name; 

SELECT p.city,
       SUM(b.total_amount) AS total_billing
FROM bills b
JOIN patients p
ON b.patient_id = p.patient_id
GROUP BY p.city; 

SELECT d.doctor_name,
       COUNT(a.appointment_id) AS total_appointments
FROM doctors d
JOIN appointments a
ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id, d.doctor_name
HAVING COUNT(a.appointment_id) > 2; 

SELECT dp.department_name,
       SUM(b.total_amount) AS total_revenue
FROM bills b
JOIN appointments a
ON b.appointment_id = a.appointment_id
JOIN doctors d
ON a.doctor_id = d.doctor_id
JOIN departments dp
ON d.department_id = dp.department_id
GROUP BY dp.department_name
HAVING SUM(b.total_amount) > 20000; 

SELECT city,
       COUNT(patient_id) AS total_patients
FROM patients
GROUP BY city
HAVING COUNT(patient_id) > 2; 


SELECT *
FROM patients p
WHERE EXISTS (
    SELECT 1
    FROM appointments a
    WHERE a.patient_id = p.patient_id
); 

SELECT *
FROM patients p
WHERE NOT EXISTS (
    SELECT 1
    FROM appointments a
    WHERE a.patient_id = p.patient_id
); 

SELECT *
FROM doctors d
WHERE NOT EXISTS (
    SELECT 1
    FROM appointments a
    WHERE a.doctor_id = d.doctor_id
); 

SELECT *
FROM bills
WHERE total_amount >
(
    SELECT AVG(total_amount)
    FROM bills 
); 

SELECT p.patient_name,
       b.total_amount
FROM patients p
JOIN bills b
ON p.patient_id = b.patient_id
WHERE b.total_amount =
(
    SELECT MAX(total_amount)
    FROM bills
); 

SELECT *
FROM doctors
WHERE consultation_fee >
(
    SELECT AVG(consultation_fee)
    FROM doctors
); 

SELECT DISTINCT p.patient_name
FROM patients p
JOIN appointments a
ON p.patient_id = a.patient_id
JOIN doctors d
ON a.doctor_id = d.doctor_id
JOIN departments dp
ON d.department_id = dp.department_id
WHERE dp.department_name = 'Cardiology'; 

SELECT *
FROM bills
WHERE bill_status <> 'Paid'; 

SELECT *
FROM appointments a
WHERE EXISTS (
    SELECT 1
    FROM treatments t
    WHERE t.appointment_id = a.appointment_id
); 

SELECT p.patient_id,
       p.patient_name,
       SUM(b.total_amount) AS total_billing
FROM patients p
JOIN bills b
ON p.patient_id = b.patient_id
GROUP BY p.patient_id, p.patient_name
HAVING SUM(b.total_amount) >
(
    SELECT AVG(patient_total)
    FROM
    (
        SELECT SUM(total_amount) AS patient_total
        FROM bills
        GROUP BY patient_id
    ) AS avg_billing
);


SELECT a.*
FROM appointments a
LEFT JOIN treatments t
ON a.appointment_id = t.appointment_id
WHERE t.appointment_id IS NULL; 

SELECT b.*
FROM bills b
LEFT JOIN payments p
ON b.bill_id = p.bill_id
WHERE p.bill_id IS NULL; 

SELECT a.appointment_id,
       a.appointment_status,
       b.bill_id,
       b.total_amount
FROM appointments a
JOIN bills b
ON a.appointment_id = b.appointment_id
WHERE a.appointment_status = 'Cancelled'; 

SELECT b.bill_id,
       b.total_amount,
       p.paid_amount
FROM bills b
JOIN payments p
ON b.bill_id = p.bill_id
WHERE b.bill_status = 'Paid'
  AND p.paid_amount < b.total_amount; 
  
SELECT d.*
FROM doctors d
LEFT JOIN departments dp
ON d.department_id = dp.department_id
WHERE dp.department_id IS NULL; 

SELECT a.*
FROM appointments a
LEFT JOIN patients p
ON a.patient_id = p.patient_id
LEFT JOIN doctors d
ON a.doctor_id = d.doctor_id
WHERE p.patient_id IS NULL
   OR d.doctor_id IS NULL; 
   
SELECT 
    p.patient_name,
    p.city,
    COUNT(DISTINCT a.appointment_id) AS total_appointments,
    COALESCE(SUM(DISTINCT b.total_amount), 0) AS total_bill_amount,
    COALESCE(SUM(py.paid_amount), 0) AS total_paid_amount,
    COALESCE(SUM(DISTINCT b.total_amount), 0) - COALESCE(SUM(py.paid_amount), 0) AS pending_amount
FROM patients p
LEFT JOIN appointments a
    ON p.patient_id = a.patient_id
LEFT JOIN bills b
    ON p.patient_id = b.patient_id
LEFT JOIN payments py
    ON b.bill_id = py.bill_id
GROUP BY p.patient_id, p.patient_name, p.city;