#!/usr/bin/python3
import MySQLdb
import sys
# Lists states starting with 'N' from DB hbtn

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        if row[1][0] == 'N':
            print(row)

    cur.close()
    db.close()
