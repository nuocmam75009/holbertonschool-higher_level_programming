#!/usr/bin/python3
"""
        Lists states where name matches arg
        Sys.Args: username, password, db, state
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM STATES WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4]))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
