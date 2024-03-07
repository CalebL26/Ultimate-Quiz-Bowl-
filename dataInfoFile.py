import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('databaseQA.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a query to retrieve table names from sqlite_master table
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all the table names from the cursor
table_names = cursor.fetchall()

# Print the table names
for table in table_names:
    print(table[0])
  

# Close the cursor and connection
cursor.close()
conn.close()
