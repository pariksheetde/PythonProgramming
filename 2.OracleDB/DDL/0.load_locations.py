import cx_Oracle

print(type(cx_Oracle))

try:
    # create Oracle DB connection
    connection = cx_Oracle.connect("HR/HRS@localhost:1521/XE")
    print(f"Connected to Oracle DB: Version {connection.version}")
except Exception as err:
    print("Error while connecting to Oracle DB...", err)

else:
    try:
        cur = connection.cursor()
        drop_table = """DROP TABLE HR.cities purge"""
        create_table = """CREATE TABLE HR.cities
                (
                    city_id INT primary key,
                    city_name VARCHAR2(20) not null,
                    country_id CHAR(2)
                )"""
        cur.execute(drop_table)
        cur.execute(create_table)
    except Exception as err:
        print("Error while creating Table:", err)
    else:
        print("Table Created successfully")
        connection.commit()
finally:
    cur.close()
    connection.close()