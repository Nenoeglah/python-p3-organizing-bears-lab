-- Create the "bears" table
-- CREATE TABLE IF NOT EXISTS bears (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     name TEXT,
--     age INTEGER,
--     status TEXT,
--     gender TEXT
-- );
CREATE TABLE bears (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER,
  sex TEXT,
  color TEXT,
  temperament TEXT,
  alive BOOLEAN
);