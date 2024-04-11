import cx_Oracle

print(type(cx_Oracle))


connection = cx_Oracle.connect("HR/HRS@localhost:1521/XE")
print(f"Connected to Oracle DB: Version {connection.version}")

cur = connection.cursor()
drop_table = """DROP TABLE HR.cities PURGE"""
create_table = """CREATE TABLE HR.cities
        (
            city_id int primary key,
            city_name varchar2(20) not null,
            country_id char(2)
        )"""
ins_rec = """INSERT INTO HR.cities VALUES (10, 'Berlin', 'GE')"""
cur.execute(drop_table)
cur.execute(create_table)
cur.execute(ins_rec)
connection.commit()

cur.close()
connection.close()