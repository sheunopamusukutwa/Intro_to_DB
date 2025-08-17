-- CREATE DATABASE
CREATE DATABASE IF NOT EXISTS alx_book_store
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE alx_book_store;

-- AUTHORS
CREATE TABLE Authors (
  author_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  author_name VARCHAR(215) NOT NULL,
  PRIMARY KEY (author_id)
) ENGINE=InnoDB;

-- CUSTOMERS
CREATE TABLE Customers (
  customer_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  customer_name VARCHAR(215) NOT NULL,
  email VARCHAR(215) NOT NULL,
  address TEXT,
  PRIMARY KEY (customer_id),
  UNIQUE KEY uq_customers_email (email)
) ENGINE=InnoDB;

-- BOOKS
CREATE TABLE Books (
  book_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  title VARCHAR(130) NOT NULL,
  author_id INT UNSIGNED NOT NULL,
  price DOUBLE NOT NULL,
  publication_date DATE,
  PRIMARY KEY (book_id),
  KEY idx_books_author_id (author_id),
  CONSTRAINT fk_books_author
    FOREIGN KEY (author_id)
    REFERENCES Authors(author_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CHECK (price >= 0)
) ENGINE=InnoDB;

-- ORDERS
CREATE TABLE Orders (
  order_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  customer_id INT UNSIGNED NOT NULL,
  order_date DATE NOT NULL,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
) ENGINE=InnoDB;

-- ORDER_DETAILS
CREATE TABLE Order_Details (
  orderdetailid INT UNSIGNED NOT NULL AUTO_INCREMENT,
  order_id INT UNSIGNED NOT NULL,
  book_id INT UNSIGNED NOT NULL,
  quantity DOUBLE NOT NULL,
  PRIMARY KEY (orderdetailid),
  KEY idx_order_details_order_id (order_id),
  KEY idx_order_details_book_id (book_id),
  CONSTRAINT fk_order_details_order
    FOREIGN KEY (order_id)
    REFERENCES Orders(order_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT fk_order_details_book
    FOREIGN KEY (book_id)
    REFERENCES Books(book_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CHECK (quantity > 0)
) ENGINE=InnoDB;
