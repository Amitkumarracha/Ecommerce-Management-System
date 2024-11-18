CREATE DATABASE IF NOT EXISTS Ecommerce_M_S;
USE Ecommerce_M_S;

-- Existing Tables --

-- Categories Table
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);

-- Customers Table
CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    address VARCHAR(500),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Users Table with Role Column
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('Customer', 'Seller') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
SELECT password FROM users WHERE email = 'ash';

-- Products Table
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE SET NULL
);

-- Orders Table
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL,
    shipping_address TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

-- Additional Tables (Order_Details, Payments, Shipping, Order_Items, Reviews, Cart) --

-- Order_Details Table
CREATE TABLE Order_Details (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    shipping_status VARCHAR(50) DEFAULT 'Processing',
    discount_code VARCHAR(50),
    delivery_date DATE,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE
);

-- Payments Table
CREATE TABLE Payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE
);

-- Shipping Table
CREATE TABLE Shipping (
    shipping_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    shipping_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delivery_date TIMESTAMP NULL,
    status VARCHAR(50) DEFAULT 'Processing',
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE
);

-- Order_Items Table
CREATE TABLE Order_Items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);

-- Reviews Table
CREATE TABLE Reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    customer_id INT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

-- Cart Table
CREATE TABLE Cart (
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT NOT NULL,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);

-- Insert Sample Data into Users Table
INSERT INTO Users (name, email, password, role) VALUES 
('John Doe', 'johndoe@example.com', 'hashed_password_1', 'Customer'),
('Jane Smith', 'janesmith@example.com', 'hashed_password_2', 'Seller');

-- Additional Insertions for Other Tables (Categories, Customers, Products, Orders, etc.)

-- Relationships and Constraints (as needed)
-- Inserting Sample Data into Categories Table
INSERT INTO Categories (category_name) VALUES 
('Electronics'), ('Clothing'), ('Books'), ('Home & Kitchen'),
('Sports & Outdoors'), ('Health & Personal Care'), ('Toys & Games'),
('Automotive'), ('Beauty'), ('Office Supplies');

-- Inserting Sample Data into Customers Table
INSERT INTO Customers (full_name, email, password_hash, phone, address) VALUES
('Alice Johnson', 'alicejohnson@example.com', 'hashed_password_3', '2345678901', '789 Pine St, Springfield'),
('Bob Brown', 'bobbrown@example.com', 'hashed_password_4', '3456789012', '101 Maple St, Springfield');

-- Inserting Sample Data into Products Table
INSERT INTO Products (category_id, product_name, description, price, stock) VALUES 
(1, 'Smartphone', 'High-end smartphone with a stunning display and excellent camera.', 699.99, 50),
(2, 'Men\'s Casual Shirt', 'Comfortable cotton shirt for everyday wear.', 39.99, 70),
(3, 'Fiction Novel', 'Bestselling novel that captivates the reader.', 14.99, 150);

-- Inserting Sample Data into Orders Table
INSERT INTO Orders (customer_id, total_amount, shipping_address) VALUES
(1, 150.00, '123 Main St, Cityville, State, 12345'),
(2, 200.50, '456 Oak St, Townsville, State, 23456');

-- Inserting Sample Data into Order_Items Table
INSERT INTO Order_Items (order_id, product_id, quantity, price) VALUES
(1, 1, 2, 29.99),
(1, 2, 1, 19.99),
(2, 3, 1, 49.99);

-- Inserting Sample Data into Payments Table
INSERT INTO Payments (order_id, amount) VALUES
(1, 59.98),
(2, 49.99);

-- Inserting Sample Data into Shipping Table
INSERT INTO Shipping (order_id, delivery_date, status) VALUES
(1, '2024-10-11 10:00:00', 'Shipped'),
(2, '2024-10-12 11:00:00', 'Processing');

-- Inserting Sample Data into Cart Table
INSERT INTO Cart (customer_id, product_id, quantity) VALUES
(1, 1, 2),
(2, 2, 1);

-- Inserting Sample Data into Reviews Table
INSERT INTO Reviews (product_id, customer_id, rating, comment) VALUES
(1, 1, 5, 'Excellent product! Highly recommend.'),
(2, 2, 4, 'Very good quality, will buy again.');


-- Define Relationships
-- Orders → Order_Items (One-to-Many)
ALTER TABLE Order_Items 
ADD CONSTRAINT FK_Orders_OrderItems
FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE;

-- Products → Order_Items (Many-to-One)
ALTER TABLE Order_Items 
ADD CONSTRAINT FK_Products_OrderItems
FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE;

-- Customers → Orders (One-to-Many)
ALTER TABLE Orders 
ADD CONSTRAINT FK_Customers_Orders
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE;

-- Orders → Payments (One-to-One)
ALTER TABLE Payments 
ADD CONSTRAINT FK_Orders_Payments
FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE RESTRICT;

-- Orders → Shipping (One-to-One)
ALTER TABLE Shipping 
ADD CONSTRAINT FK_Orders_Shipping
FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE RESTRICT;

-- Customers → Reviews (One-to-Many)
ALTER TABLE Reviews 
ADD CONSTRAINT FK_Customers_Reviews
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE;

-- Products → Reviews (One-to-Many)
ALTER TABLE Reviews 
ADD CONSTRAINT FK_Products_Reviews
FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE;

-- Customers → Cart (One-to-Many)
ALTER TABLE Cart 
ADD CONSTRAINT FK_Customers_Cart
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE;

-- Orders → Order_Details (One-to-One)
ALTER TABLE Order_Details 
ADD CONSTRAINT FK_Orders_OrderDetails
FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE;
