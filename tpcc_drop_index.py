from utils.conn_utils import *

index_names = [
    "w_pkey",
    "d_pkey",
    "c_pkey",
    "i_pkey",
    "no_pkey",
    "o_pkey",
    "ol_pkey",
    "s_pkey",
]

conn = get_conn("localhost", "benchbase", "admin", "")
for name in index_names:
    run_query(conn, f"drop index if exists {name};")