import psycopg2
import time
import sys

cursor = None

def get_conn(host, dbname, user, password):
    global cursor
    conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
    cursor = conn.cursor()

    return conn

def run_query(conn, query):
    assert conn is not None
    global cursor
    is_select = query.lower().strip().startswith("select")\
        or query.lower().strip().startswith("explain")\
        or query.lower().strip().startswith("show")
    try:
        cursor.execute(query)
        if is_select:
            return cursor.fetchall()
        else:
            conn.commit()
            return None
    except:
        # Throw exceptions if on error again.
        conn.reset()
        cursor = conn.cursor()
        cursor.execute(query)
        if is_select:
            return cursor.fetchall()
        else:
            conn.commit()
            return None

file_path = sys.argv[1]
file = open(file_path, "r")
lines = file.readlines()
file.close()

conn = get_conn("127.0.0.1", "test", "ubuntu", "")
run_query(conn, "set max_parallel_workers_per_gather=0;")
run_query(conn, "set enable_bitmapscan=off;")

for line in lines:
    run_query(conn, line)