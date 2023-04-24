import cx_Oracle

print(type(cx_Oracle))

try:
    # create Oracle DB connection
    connection = cx_Oracle.connect("Hr/Hr@localhost:1521/prod")
    print(f"Connected to Oracle DB: Version {connection.version}")
except Exception as err:
    print("Error while connecting to Oracle DB...", err)
    