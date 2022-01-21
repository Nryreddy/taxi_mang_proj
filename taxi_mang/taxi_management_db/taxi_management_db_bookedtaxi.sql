create table bookedtaxi
(
    id                   int auto_increment
        primary key,
    registration_no      varchar(50) not null,
    taxi_type            varchar(50) not null,
    `From`               varchar(50) not null,
    `To`                 varchar(50) not null,
    yname                varchar(64) not null,
    Bdate                varchar(64) not null,
    Btime                varchar(64) not null,
    customer_customer_id int         null,
    taxi_taxi_id         int         null,
    constraint customer_customer_id_fk
        foreign key (customer_customer_id) references customer (customer_id)
            on update cascade on delete cascade,
    constraint taxi_taxi_id_fk
        foreign key (taxi_taxi_id) references taxi (taxi_id)
            on update cascade on delete cascade
);

create index customer_customer_id
    on bookedtaxi (customer_customer_id);

create index ix_bookedtaxi_Bdate
    on bookedtaxi (Bdate);

create index ix_bookedtaxi_Btime
    on bookedtaxi (Btime);

create index ix_bookedtaxi_From
    on bookedtaxi (`From`);

create index ix_bookedtaxi_To
    on bookedtaxi (`To`);

create index ix_bookedtaxi_registration_no
    on bookedtaxi (registration_no);

create index ix_bookedtaxi_yname
    on bookedtaxi (yname);

create index taxi_taxi_id
    on bookedtaxi (taxi_taxi_id);

INSERT INTO taxi_management_db.bookedtaxi (id, registration_no, taxi_type, `From`, `To`, yname, Bdate, Btime, customer_customer_id, taxi_taxi_id) VALUES (1, '1429', 'sedan', 'bengaluru', 'goa', 'nithesh', '19-01-2022', '22:00', null, null);
INSERT INTO taxi_management_db.bookedtaxi (id, registration_no, taxi_type, `From`, `To`, yname, Bdate, Btime, customer_customer_id, taxi_taxi_id) VALUES (2, '51542', 'sedan', 'bengaluru', 'raichur', 'nry', '20-01-2022', '20:00', null, null);
INSERT INTO taxi_management_db.bookedtaxi (id, registration_no, taxi_type, `From`, `To`, yname, Bdate, Btime, customer_customer_id, taxi_taxi_id) VALUES (3, '28461', 'hatchback', 'delhi', 'agra', 'sam', '21-01-2022', '12:00', 3, null);
INSERT INTO taxi_management_db.bookedtaxi (id, registration_no, taxi_type, `From`, `To`, yname, Bdate, Btime, customer_customer_id, taxi_taxi_id) VALUES (6, '9012', 'mini', 'dasarahalli', 'white field', 'nithesh', '21-01-2022', '10:00', 1, 4);
INSERT INTO taxi_management_db.bookedtaxi (id, registration_no, taxi_type, `From`, `To`, yname, Bdate, Btime, customer_customer_id, taxi_taxi_id) VALUES (7, '2121', 'sedan', 'goa', 'benagluru', 'nithesh', '22-01-2022', '9:00', 1, 3);
INSERT INTO taxi_management_db.bookedtaxi (id, registration_no, taxi_type, `From`, `To`, yname, Bdate, Btime, customer_customer_id, taxi_taxi_id) VALUES (8, '104221', 'sedan', 'mandya', 'mysore', 'Anu', '24-01-2022', '08:00', 4, 11);
INSERT INTO taxi_management_db.bookedtaxi (id, registration_no, taxi_type, `From`, `To`, yname, Bdate, Btime, customer_customer_id, taxi_taxi_id) VALUES (9, '149632', 'Limo', 'mumbai', 'bengaluru', 'nry', '24-01-2022', '20:00', 2, 8);
INSERT INTO taxi_management_db.bookedtaxi (id, registration_no, taxi_type, `From`, `To`, yname, Bdate, Btime, customer_customer_id, taxi_taxi_id) VALUES (10, '2121', 'sedan', 'goa', 'benagluru', 'pavan', '12-2-2001', '19.45', 1, 3);
INSERT INTO taxi_management_db.bookedtaxi (id, registration_no, taxi_type, `From`, `To`, yname, Bdate, Btime, customer_customer_id, taxi_taxi_id) VALUES (11, '1429', 'sedan', 'bengaluru', 'goa', 'nithesh', '28-01-2022', '10:00', 1, 1);
INSERT INTO taxi_management_db.bookedtaxi (id, registration_no, taxi_type, `From`, `To`, yname, Bdate, Btime, customer_customer_id, taxi_taxi_id) VALUES (12, '10710', 'sedan', 'vellur', 'white field', 'badhree', '25-01-2022', '09:00', 5, 10);
INSERT INTO taxi_management_db.bookedtaxi (id, registration_no, taxi_type, `From`, `To`, yname, Bdate, Btime, customer_customer_id, taxi_taxi_id) VALUES (13, '9012', 'mini', 'dasarahalli', 'white field', 'nithesh', '21-01-2022', '18:00', 1, 4);
INSERT INTO taxi_management_db.bookedtaxi (id, registration_no, taxi_type, `From`, `To`, yname, Bdate, Btime, customer_customer_id, taxi_taxi_id) VALUES (14, '2010912', 'limo', 'chennai', 'white field', 'sam', '24-01-2022', '18:00', 3, 15);