import sqlite3

# Connect to SQlite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table

cursor = connection.cursor()

# create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25));
"""

cursor.execute(table_info)

# Insert some more records

cursor.execute('''Insert into STUDENT values('John', 'Machine Learning', 'A')''')
cursor.execute('''Insert into STUDENT values('Sundhar', 'Statistics', 'B')''')
cursor.execute('''Insert into STUDENT values('Darius', 'Probability', 'A')''')
cursor.execute('''Insert into STUDENT values('Vikas', 'Calculus', 'A')''')
cursor.execute('''Insert into STUDENT values('Yadhav', 'Devops', 'A')''')

# Display All the records

print("The inserted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

# Commit your changes in the database
connection.commit()
connection.close()