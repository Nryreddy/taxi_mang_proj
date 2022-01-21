create table customer
(
    customer_id   int auto_increment
        primary key,
    customer_name varchar(50) not null,
    contact_no    varchar(50) not null,
    gender        varchar(10) not null,
    address       varchar(50) not null,
    password_hash varchar(60) not null,
    constraint customer_name
        unique (customer_name)
);

INSERT INTO taxi_management_db.customer (customer_id, customer_name, contact_no, gender, address, password_hash) VALUES (1, 'nithesh', '8310977433', 'male', 'bengaluru', '$2b$12$1T0.padv8ZWLijq2Dk0.dOAoVK1pBlcNMS4h3jD7o4H40WqWbz8eu');
INSERT INTO taxi_management_db.customer (customer_id, customer_name, contact_no, gender, address, password_hash) VALUES (2, 'nry', '11119', 'male', 'bengaluru', '$2b$12$4rj6zpRF5QtvtEgJgrePM.szhCVi17pz4U.jkR9/B.YxLt0obQysW');
INSERT INTO taxi_management_db.customer (customer_id, customer_name, contact_no, gender, address, password_hash) VALUES (3, 'sam', '123654', 'female', 'delhi', '$2b$12$tkTvvF8z7KVPla4LPNBWe.d14LAXdavGlxugKkGqk9JZRgmfbZBd2');
INSERT INTO taxi_management_db.customer (customer_id, customer_name, contact_no, gender, address, password_hash) VALUES (4, 'Anu', '92102451', 'female', 'mysore', '$2b$12$895utv3/aTNT.JHDg7w8FObYKw0kaMe9bvBzM4XcImXSdE.9rlHAq');
INSERT INTO taxi_management_db.customer (customer_id, customer_name, contact_no, gender, address, password_hash) VALUES (5, 'badhree', '9319010', 'male', 'kolar', '$2b$12$aW435XM65moZXsXmVAoSzeYsHUvqP8mNYZ.dhGIR42TAt1FU2.m1C');