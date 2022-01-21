create table taxi_log
(
    taxi_log_id     int          not null
        primary key,
    registration_no varchar(45)  null,
    `From`          varchar(45)  null,
    `To`            varchar(45)  null,
    action          varchar(100) null,
    add_time        time         null
);

INSERT INTO taxi_management_db.taxi_log (taxi_log_id, registration_no, `From`, `To`, action, add_time) VALUES (12, '12419732', 'delhi', 'agra', 'taxi added', null);
INSERT INTO taxi_management_db.taxi_log (taxi_log_id, registration_no, `From`, `To`, action, add_time) VALUES (13, '1021009', 'pune', 'mumbai', 'taxi added', null);
INSERT INTO taxi_management_db.taxi_log (taxi_log_id, registration_no, `From`, `To`, action, add_time) VALUES (14, '110021', 'gujarat', 'maharastra', 'taxi added', null);
INSERT INTO taxi_management_db.taxi_log (taxi_log_id, registration_no, `From`, `To`, action, add_time) VALUES (15, '2010912', 'chennai', 'white field', 'taxi added', null);
INSERT INTO taxi_management_db.taxi_log (taxi_log_id, registration_no, `From`, `To`, action, add_time) VALUES (16, '1801147', 'begaluru', 'pune', 'taxi added', '01:30:45');
INSERT INTO taxi_management_db.taxi_log (taxi_log_id, registration_no, `From`, `To`, action, add_time) VALUES (17, '1120149', 'vellur', 'chennai', 'taxi added', '17:10:43');