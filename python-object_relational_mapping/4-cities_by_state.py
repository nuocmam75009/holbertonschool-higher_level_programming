#!/usr/bin/python3
import MySQLdb
import sys
# Lists states where name matches arg
# Sys.Args: username, password, db, state
# Safe from SQL injection -> not in SQL query

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities, states \
                INNER JOIN states \
                ON cities.state_id = states.id \
                ORDER BY cities.id ASC")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
