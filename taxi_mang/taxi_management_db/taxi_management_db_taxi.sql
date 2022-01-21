create table taxi
(
    taxi_id            int auto_increment
        primary key,
    taxi_type          varchar(50) not null,
    registration_no    varchar(50) not null,
    `From`             varchar(50) not null,
    `To`               varchar(50) not null,
    flag               int         null,
    owner_owner_id     int         null,
    driver_driver_name varchar(50) null,
    constraint registration_no
        unique (registration_no),
    constraint driver_driver_name_fk
        foreign key (driver_driver_name) references driver (driver_name)
            on update cascade on delete cascade,
    constraint taxi_ibfk_1
        foreign key (owner_owner_id) references owner (owner_id)
            on update cascade on delete cascade
);

create index driver_driver_name
    on taxi (driver_driver_name);

INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (1, 'sedan', '1429', 'bengaluru', 'goa', 1, 1, null);
INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (3, 'sedan', '2121', 'goa', 'benagluru', 1, 1, null);
INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (4, 'mini', '9012', 'dasarahalli', 'white field', 1, 1, null);
INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (5, 'sedan', '51542', 'bengaluru', 'raichur', 0, 2, 'rohit');
INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (6, 'mini', '31974', 'tumakuru', 'chennai', 0, 2, null);
INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (7, 'hatchback', '28461', 'delhi', 'agra', 0, 2, null);
INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (8, 'Limo', '149632', 'mumbai', 'bengaluru', 1, 1, null);
INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (9, 'mini', '10750', 'mysore', 'chennai', 0, 1, null);
INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (10, 'sedan', '10710', 'vellur', 'white field', 1, 1, null);
INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (11, 'sedan', '104221', 'mandya', 'mysore', 0, 2, null);
INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (12, 'mini', '12419732', 'delhi', 'agra', 0, 1, null);
INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (13, 'mini', '1021009', 'pune', 'mumbai', 0, 1, 'Richard Branson');
INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (14, 'sedan', '110021', 'gujarat', 'maharastra', 0, 1, 'beenu');
INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (15, 'limo', '2010912', 'chennai', 'white field', 1, 1, 'ashwin');
INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (16, 'sedan', '1801147', 'begaluru', 'pune', 0, 2, 'Alastair Cook');
INSERT INTO taxi_management_db.taxi (taxi_id, taxi_type, registration_no, `From`, `To`, flag, owner_owner_id, driver_driver_name) VALUES (17, 'limo', '1120149', 'vellur', 'chennai', 0, 1, 'danush');