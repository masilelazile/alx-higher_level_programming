#!/usr/bin/python3
"""
Take in an argument and display all values in the states table
of hbtn_0e_0_usa where name matches the argument.
This script is safe from MySQL injections.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    query = """
            SELECT *
            FROM states
            WHERE name = %s
            ORDER BY id ASC
            """
    cur.execute(query, (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
