#!/usr/bin/env python3
# Copyright 2022 Pariksheet DE
# db-query.py as of 2021-04-07
# runs on Python 3.8.0

import cx_Oracle

def main():
    db = cx_Oracle.connect("HR/HRS@localhost:1521/XE")
    cur = db.cursor()
    qry_dept = """SELECT 
                    d.department_id, 
                    d.department_name,
                    d.location_id
                    FROM 
                    departments d ORDER by 1 ASC"""
    cur.execute(qry_dept)
    row = cur.fetchall()
    print(row)

    print(f"Record(s) returned: {cur.rowcount}")

    cur.close()
    db.close()


if __name__ == "__main__":
    main()