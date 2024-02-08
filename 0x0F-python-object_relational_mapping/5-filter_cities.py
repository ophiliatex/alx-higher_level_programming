#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """"
    Access to the database and get the cities
    from the database.
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("""
        SELECT
            cities.name
        FROM
            cities
        JOIN
            states
        ON
            cities.states_id = state.id
        WHERE
            states.name LIKE BINARY %(state_name)s
        ORDER BY
            cities.id ASC
        """, {
            'state_name': sys.argv[4]
        })

        rows = cur.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
