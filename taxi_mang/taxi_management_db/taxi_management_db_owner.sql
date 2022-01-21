create table owner
(
    owner_id      int auto_increment
        primary key,
    owner_name    varchar(50) not null,
    contact_no    varchar(50) not null,
    gender        varchar(50) not null,
    address       varchar(50) not null,
    password_hash varchar(60) not null,
    constraint contact_no
        unique (contact_no),
    constraint owner_name
        unique (owner_name)
);

INSERT INTO taxi_management_db.owner (owner_id, owner_name, contact_no, gender, address, password_hash) VALUES (1, 'nithesh', '8310977433', 'male', 'benagluru', '$2b$12$fPTlcfJEeI1oEKayj7BuSO.hkLCmpzBaV2ZVFdR/.U.3BUM3hty5S');
INSERT INTO taxi_management_db.owner (owner_id, owner_name, contact_no, gender, address, password_hash) VALUES (2, 'pavan kumar', '251611255', 'male', 'benagluru', '$2b$12$DyS0/WflkwQNaVcm2cYXxO6EGn7hO/6vETnKbG8Ulg7728KV1c0RW');