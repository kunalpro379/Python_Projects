import sqlite3
import csv
connection=sqlite3.connect('newdb.db')
cursor=connection.cursor()

name="patil"
position="patil"
# cursor.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEES (
#                Emp_Id INT,Name TEXT,Salary INT
# )''')
# #syntax
# #CREATE TABLE <table name>(<column name> <data type>, <column name> <data type>, <column name> <data type>);
# cursor.execute('''INSERT INTO EMPLOYEES VALUES(1222,'kunal',50000)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS newdb (
            name TEXT, position TEXT)''')

# Use placeholders in the VALUES clause
cursor.execute('''INSERT INTO newdb (name, position) VALUES(?, ?)''', (name, position))
newdb=[("kunal","developer"),("vedant", "kachrewala"),("atharva", "bhikari"),("kunal","developer"),("vedant", "kachrewala"),("atharva", "bhikari")]
cursor.executemany('''INSERT INTO newdb (name, position) VALUES(?, ?)''', newdb)

connection.commit()
connection.close()

connection=sqlite3.connect('data.db')
cursor=connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Population (
            city TEXT, Country TEXT,Pop_NO INT)''')
#file=open('Population_data.csv')
#
cursor.execute(''' select* from Population where city like '%It%' and Pop_NO>200000''')
#cursor.execute(''' select* from Population where Country =?  and Pop_NO>?''')

connection.commit()
print(cursor.fetchall())
#retrieving data
#SELECT Emp_Id,Name FROM Employees
#SELECT * FROM Employees 



connection.close()


"""
SELECT * EMPLOYEE 
WHERE SALARY>50000
WHERE SALARY>50000 AND EMP_ID>1000

UPDATE employees SET Name='kunal' WHERE Emp_Id=1222
UPDATE employees SET Name='kunal',Salary=50000 WHERE Emp_Id=1222

UPDATE employee
SET Name='kunal' , Surnmae='patil'
WHERE Emp_Id=1222

DELETE FROM employees WHERE Emp_Id=1222

"""
# connection=sqlite3.connect('newdb.db')

# cursor.execute("""UPDATE Employees set position='Senior Developer' where name='kunal'""")
# connection.commit()
# print(cursor.fetchall())
import sqlite3

# Create or connect to the database
connection = sqlite3.connect("great.db")
cursor = connection.cursor()

# Create the Employees table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Employees(Emp_ID INT, Name TEXT, Position TEXT)''')

# Update the position for an employee named 'prajwal'
name_update = 'prajwal'
position_update = 'web developer'
cursor.execute('''UPDATE Employees SET Position=? WHERE Name=?''', (position_update, name_update))

# Print information for debugging
print("Data after updating position:")

# Delete an employee named 'sagar'
name_delete = 'sagar'
cursor.execute('''DELETE FROM Employees WHERE Name=?''', (name_delete,))
cursor.execute('''DROP TABLE Employees''')#delete complete table

connection.commit()
connection.close()

import sqlite3

connection = sqlite3.connect("kunal.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Employees(Emp_Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Position TEXT, Salary INTEGER, Dep_Id INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Departments(Dep_Id INTEGER, Name TEXT)''')

employees = [('kunal patil', 'software dev', 1000, 2211), ('dont know', 'idk', 282, 2211), ('pfjjfj', 'dhjhfhdh', 2727, 28387)]
departments = [(2211, 'IT'), (28387, 'cs')]

cursor.executemany('''INSERT INTO Employees(Name, Position, Salary, Dep_Id) VALUES (?, ?, ?, ?)''', employees)

cursor.executemany('''INSERT INTO Departments VALUES (?, ?)''', departments)

connection.commit()
connection.close()
#SELECT * from Employees join Departments on Employees.Dep_Id=Departments.Dep_Id;
#SELECT Employees.*, Departments.Name from Employees join Departments on Employees.Dep_Id=Departments.Dep_Id;
