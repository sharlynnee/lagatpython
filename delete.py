import sqlite3

conn = sqlite3.connect('exercise')
print("Opened database successfully")

conn.execute("DELETE FROM EMPLOYEES2 WHERE ID=1")
conn.commit()

cursor = conn.execute("SELECT * FROM EMPLOYEES;")

for row in cursor:
    print("ID", row[0])
    print("NAME", row[1])
    print("AGE", row[2])
    print("SALARY", row[3])
print("records found")
conn.close()