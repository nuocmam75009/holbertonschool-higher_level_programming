import MySQLdb
# cur is cursor
def list_states(username, password, db_name):
    try:
        db = MySQLdb.connect(host='localhost', username = username, password = password, db = db_name)
        cur = db.cursor()
        cur.execute("SELECT name FROM states ORDER BY states.id ASC") # PUT SQL STATEMENTS
        states = cur.fetchall()

        for state in states:
            print(state[0])

    except MySQLdb.Error as error:
        print("Error connection to database: {}".format(error))

    finally:
        if cur:
            cur.close()
        if db:
            db.close()

if __name__ == "__main__":
    pass