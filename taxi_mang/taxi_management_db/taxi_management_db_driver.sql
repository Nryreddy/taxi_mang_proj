create table driver
(
    driver_id   int auto_increment
        primary key,
    driver_name varchar(50) not null,
    contact_no  varchar(50) not null,
    gender      varchar(10) not null,
    address     varchar(50) not null,
    constraint driver_name
        unique (driver_name)
);

INSERT INTO taxi_management_db.driver (driver_id, driver_name, contact_no, gender, address) VALUES (1, 'rohit', '142578', 'male', 'mumbai');
INSERT INTO taxi_management_db.driver (driver_id, driver_name, contact_no, gender, address) VALUES (2, 'ram', '143987', 'male', 'chennai');
INSERT INTO taxi_management_db.driver (driver_id, driver_name, contact_no, gender, address) VALUES (3, 'ricky', '1475246', 'male', 'begaluru');
INSERT INTO taxi_management_db.driver (driver_id, driver_name, contact_no, gender, address) VALUES (4, 'deepu', '919102', 'male', 'mangalore');
INSERT INTO taxi_management_db.driver (driver_id, driver_name, contact_no, gender, address) VALUES (5, 'ttt', '1452', 'male', 'mnmkj');
INSERT INTO taxi_management_db.driver (driver_id, driver_name, contact_no, gender, address) VALUES (6, 'chhhk', '1021993', 'male', 'miinj');
INSERT INTO taxi_management_db.driver (driver_id, driver_name, contact_no, gender, address) VALUES (7, 'ramu', '123120', 'male', 'kmmm');
INSERT INTO taxi_management_db.driver (driver_id, driver_name, contact_no, gender, address) VALUES (8, 'smith', '1091924', 'male', 'chennai');
INSERT INTO taxi_management_db.driver (driver_id, driver_name, contact_no, gender, address) VALUES (9, 'Richard Branson', '10991101', 'male', 'pune');
INSERT INTO taxi_management_db.driver (driver_id, driver_name, contact_no, gender, address) VALUES (10, 'seenu', '4013279', 'male', 'mumbai');
INSERT INTO taxi_management_db.driver (driver_id, driver_name, contact_no, gender, address) VALUES (12, 'reenu', '41013279', 'male', 'mumbai');
INSERT INTO taxi_management_db.driver (driver_id, driver_name, contact_no, gender, address) VALUES (14, 'beenu', '21013279', 'female', 'gandhinagar');
INSERT INTO taxi_management_db.driver (driver_id, driver_name, contact_no, gender, address) VALUES (15, 'ashwin', '91810210', 'male', 'chennai');
INSERT INTO taxi_management_db.driver (driver_id, driver_name, contact_no, gender, address) VALUES (16, 'Alastair Cook', '98319741', 'male', 'begaluru');
INSERT INTO taxi_management_db.driver (driver_id, driver_name, contact_no, gender, address) VALUES (17, 'danush', '9741251', 'male', 'vellur');