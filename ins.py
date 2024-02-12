import sqlite3
conn = sqlite3.connect("exercise")
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (0,'FAITH KARIMI',23,3450000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (1,'LAGAT SHARLENE',23,3450000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'FOY TULLA',23,3450000.00)")

conn.commit()
print("Records inserted successfully")
conn.close()