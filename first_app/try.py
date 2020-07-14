import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute("INSERt INTO data values(?,?,?,?,?,?,?)",(District,Area,Amt,Name,Phone_no,email,result))

conn.commit()


cur.close()
conn.close()
