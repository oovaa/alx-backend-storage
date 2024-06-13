-- task 0
/*
 * Creates a table named 'users' if it does not already exist.
 * The table has three columns:
 * - id: an auto-incrementing integer column that serves as the primary key.
 * - email: a non-null varchar column with a maximum length of 255 characters, which must be unique.
 * - name: a varchar column with a maximum length of 255 characters.
 */

CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id)
);