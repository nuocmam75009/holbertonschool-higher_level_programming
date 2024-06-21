import MySQLdb
import sys
# Lists states where name matches arg
# Sys.Args: username, password, db, state

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        username=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM STATES WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4]))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
