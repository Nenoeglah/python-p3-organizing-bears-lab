import sqlite3
from sql_queries import (
    select_all_female_bears_return_name_and_age,
    select_all_bears_names_and_orders_in_alphabetical_order,
    select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest,
    select_oldest_bear_and_returns_name_and_age,
    select_youngest_bear_and_returns_name_and_age,
)

# Create the database and tables using create.sql
with open("create.sql", "r") as create_file:
    create_sql = create_file.read()
    conn = sqlite3.connect("bears.db")
    cursor = conn.cursor()
    cursor.executescript(create_sql)
    conn.commit()
    conn.close()

# Insert data using insert.sql
with open("insert.sql", "r") as insert_file:
    insert_sql = insert_file.read()
    conn = sqlite3.connect("bears.db")
    cursor = conn.cursor()
    cursor.executescript(insert_sql)
    conn.commit()
    conn.close()

# Connect to the database
conn = sqlite3.connect("bears.db")
cursor = conn.cursor()

# Execute SQL queries
# ...

# Close the database connection
conn.close()
