import sqlite3


def connect(dbname):
    conn=sqlite3.connect(dbname)
    conn.execute("CREATE TABLE IF NOT EXISTS GSOC(NAME TEXT, DESC TEXT)")
    print("Table created successfully")
    conn.close()

def insert_into_table(dbname, values):
    conn=sqlite3.connect(dbname)
    insert_sql="INSERT INTO GSOC (NAME, DESC) VALUES(?,?)"
    conn.execute(insert_sql, values)
    conn.commit()
    conn.close()

def get_org_info(dbname):
    conn=sqlite3.connect(dbname)
    cur=conn.cursor()
    cur.execute("SELECT * FROM GSOC")
    table_data=cur.fetchall()
    for record in table_data:
        print(record)
    conn.close()