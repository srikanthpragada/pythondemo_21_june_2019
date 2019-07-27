import sqlite3

con = sqlite3.connect(r"e:\classroom\python\june21\catalog.db")
cur = con.cursor()
cur.execute("select * from publishers")

for row in cur:
    print(f"{row[1]:20} {row[2]:30} {row[3]}")

cur.close()
con.close()
