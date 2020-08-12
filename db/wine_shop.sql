DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS producers;

CREATE TABLE producers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country VARCHAR(255),
    contact_number VARCHAR(255),
    contact_email VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    cost DECIMAL,
    price FLOAT,
    case_price FLOAT,
    stock INTEGER,
    producer_id INT REFERENCES producers(id) ON DELETE CASCADE,
    reduction INT
);