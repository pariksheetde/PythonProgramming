# THE CODE EXECUTES IN python 3.8.0

import cx_Oracle
print(type(cx_Oracle))

try:
    # create Oracle DB connection
    connection = cx_Oracle.connect("HR/HR@localhost:1521/xe")
    print(f"Connected to Oracle DB: Version {connection.version}")
except Exception as err:
    print("Error while connecting to Oracle DB...", err)
    