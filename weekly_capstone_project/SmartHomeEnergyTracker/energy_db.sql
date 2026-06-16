CREATE DATABASE energy_db;
USE energy_db;

CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_name VARCHAR(100),
    floor INT
);

CREATE TABLE devices (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT,
    device_name VARCHAR(100),
    device_type VARCHAR(50),
    status ENUM('ON','OFF') DEFAULT 'OFF',
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE energy_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    device_id INT,
    usage_kwh DECIMAL(10,2),
    log_date DATE,
    FOREIGN KEY (device_id) REFERENCES devices(device_id)
);

INSERT INTO rooms (room_name, floor)
VALUES ('Living Room', 1),
       ('Bedroom', 2);
       
INSERT INTO devices (room_id, device_name, device_type, status)
VALUES (1, 'Fan', 'Appliance', 'ON'),
       (1, 'Light', 'Lighting', 'OFF');
       
INSERT INTO energy_logs (device_id, usage_kwh, log_date)
VALUES (1, 2.5, '2026-06-16'),
       (2, 1.2, '2026-06-16');
       
SELECT * FROM rooms;
SELECT * FROM devices;
SELECT * FROM energy_logs;

UPDATE devices
SET status = 'OFF'
WHERE device_id = 1;

DELETE FROM energy_logs
WHERE log_id = 1;

SELECT 
    r.room_name,
    d.device_name,
    e.usage_kwh,
    e.log_date
FROM energy_logs e
JOIN devices d ON e.device_id = d.device_id
JOIN rooms r ON d.room_id = r.room_id;

DELIMITER $$

CREATE PROCEDURE room_daily_energy()
BEGIN
    SELECT 
        r.room_name,
        e.log_date,
        SUM(e.usage_kwh) AS total_energy
    FROM energy_logs e
    JOIN devices d ON e.device_id = d.device_id
    JOIN rooms r ON d.room_id = r.room_id
    GROUP BY r.room_name, e.log_date;
END $$

DELIMITER ;

CALL room_daily_energy();

CREATE INDEX idx_device_id ON energy_logs(device_id);
CREATE INDEX idx_log_date ON energy_logs(log_date);

