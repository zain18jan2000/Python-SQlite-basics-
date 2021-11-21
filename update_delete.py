import sqlite3

# connecting to database then it will be created automatically
conn = sqlite3.connect('database.db')

# create a cursor object. Used to add and fetch data from database
cursor = conn.cursor()

# Update the record in database
# changing the email in row in which First_name='Hamza' and Last_name='Nadeem'
cursor.execute("""
UPDATE customers SET Email = 'hamza.2005@gmail.com' WHERE First_name = 'Hamza' AND
 Last_name = 'Nadeem'
""")

# save the changes
conn.commit()

# We can also use primary key (row id) to specify the row need to be updated
cursor.execute("""
UPDATE customers SET Email = 'rana_abubakr@gmail.com' WHERE rowid = 4
""")

# save the changes
conn.commit()

