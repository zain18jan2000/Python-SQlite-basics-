import sqlite3
from sqlite3.dbapi2 import connect

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

# searching the row in the table in which First_name = 'Muhammad'
cursor.execute("SELECT * FROM customers WHERE First_name = 'Muhammad'")
items = cursor.fetchall()
print(items)

# searching the row in the table in which First_name starts with 'Ab'
cursor.execute("SELECT * FROM customers WHERE First_name LIKE 'Ab%'")
print('\n')
data = cursor.fetchall()
print(data)

# searching the rows in the table in which Email contatains 'gmail.com' 
cursor.execute("SELECT * FROM customers WHERE Email LIKE '%gmail.com'")
print('\n')
data = cursor.fetchall()
print(data)