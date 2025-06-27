CREATE DATABASE IF NOT EXISTS bookstore;
USE bookstore;

CREATE TABLE IF NOT EXISTS books (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    price FLOAT,
    stock INT,
    image_url VARCHAR(512)
);
