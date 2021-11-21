import sqlite3

# connecting to database
# if database file doesnot exist then it will be created automatically
conn = sqlite3.connect('database.db')

# create a cursor object. Used to add and fetch data from database
cursor = conn.cursor()

# create a table with the following fields
# 1- First_name  2- Last_name  3- Email TEXT
# after every field we need to specify its data type
# sqlite has 5 data types
# INTEGER
# TEXT
# NULL (nothing)
# REAL (a real number)
# BLOB (image,mp3,mp4 file etc)

cursor.execute("""
CREATE TABLE customers(First_name TEXT,Last_name TEXT,Email TEXT)
""")


# adding data in table
# here I used triple quotes but I can also used  used single qoutes but in that
# case you have to write this statement in a single line
cursor.execute("""
INSERT INTO customers VALUES('Muhammad','Zain','zain.18j2000@gmail.com')
""")

data = [
    ('Saqib','Iqbal','saqibiqbal@gmail.com'),
    ('Hamza', 'Nadeem','hamza.22jul@gmail.com'),
    ('Abu Bakr','Rana','123RANA@gmail.com') 
]

# to add multiple sets of information
# (?,?,?) --> refering to number of field in database, in this case we have 3 fields
# so 3 times '?'
cursor.executemany("""
INSERT INTO customers VALUES (?,?,?)
""",data)

# saving the table to database
conn.commit()

# close connection (not neccessary)
conn.close()

