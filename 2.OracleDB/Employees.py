#!/usr/bin/env python3
# Copyright 2022 Pariksheet DE
# db-query.py as of 2021-04-07
# runs on Python 3.8.0


import cx_Oracle

def main():
    db = cx_Oracle.connect("HR/HRS@localhost:1521/XE")
    cur = db.cursor()
    qry_emp = """SELECT 
                    e.employee_id, 
                    e.first_name||' '||e.last_name as name
                    FROM 
                    employees e order by 1 asc"""
    cur.execute(qry_emp)
    row = cur.fetchall()
    print(row)

    print(f"Record(s) returned: {cur.rowcount}")

    cur.close()
    db.close()


if __name__ == "__main__":
    main()