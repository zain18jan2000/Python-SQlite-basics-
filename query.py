import sqlite3

# connecting to database
conn = sqlite3.connect('database.db')

# create a cursor object. Used to add and fetch data from database
cursor = conn.cursor()

# query the database
# A 'QUERY' is a request to database to fetch or manipulate some data in that database
cursor.execute("SELECT * FROM customers") # * --> everything, customers --> table name

# to fetch every thing from database file
print(cursor.fetchall())
print('\n')

cursor.execute("SELECT * FROM customers")

# to query the first tuple data
# cursor.fetchone() basically provides a tuple containing info of one row 
print(cursor.fetchone())
print('\n')

cursor.execute("SELECT * FROM customers")
# cursor.fetchmany() provides a list with a tuple in it
print(cursor.fetchmany())


conn.close()