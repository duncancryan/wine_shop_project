DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS producers;

CREATE TABLE producers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country VARCHAR(255),
    contact_number VARCHAR(255),
    contact_email VARCHAR(255)
)