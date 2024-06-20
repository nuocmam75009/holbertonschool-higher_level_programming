import MySQLdb
import sys
# Lists states starting with 'N' from DB hbtn

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        username=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cur.fetchall()

    for state in states():
        if state[1][0] == 'N':
            print(state)

    cur.close()
    db.close()
