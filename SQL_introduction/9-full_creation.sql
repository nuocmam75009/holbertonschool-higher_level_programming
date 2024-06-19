-- Script that creates a table second_table
-- Adds multiple rows in second_table
-- DB: hbtn_0c_0
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
)
INSERT INTO second_table (
    1,
    'John',
    10
)
INSERT INTO second_table (
    2,
    'Alex',
    3
)
INSERT INTO second_table (
    3,
    'Bob',
    14
)
INSERT INTO second_table (
    4,
    'George',
    8
);