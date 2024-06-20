import MySQLdb
import sys
# cur is cursor
#

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, username = sys.argv[1], password = sys.argv[2], db = sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT name FROM states ORDER BY states.id ASC") # PUT SQL STATEMENTS
    states = cur.fetchall()

    for state in states:
                print(state)

    if cur:
                cur.close()
    if db:
                db.close()