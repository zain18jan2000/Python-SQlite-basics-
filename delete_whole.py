import sqlite3

# connecting to database
conn = sqlite3.connect('database.db')

# create a cursor object. Used to add and fetch data from database
cursor = conn.cursor()

# to delete a record from database
cursor.execute("""
DELETE from customers WHERE rowid = 1
""")

# commit the changes
conn.commit()

# delete the whole table in database file
cursor.execute("DROP TABLE customers")

conn.close()