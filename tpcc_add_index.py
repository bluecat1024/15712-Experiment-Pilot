from utils.conn_utils import *
import time

creat_index_list = [
    "create index w_pkey on warehouse(w_id);",
    "create index d_pkey on district(d_w_id, d_id);",
    "create index i_pkey on item(i_id);",
    "create index s_pkey on stock(s_w_id, s_i_id);",
    "create index c_pkey on customer(c_w_id, c_d_id, c_id);",
    "create index o_pkey on oorder(o_w_id, o_d_id, o_id);",
    "create index no_pkey on new_order(no_w_id, no_d_id, no_o_id);",
    "create index ol_pkey on order_line(ol_w_id, ol_d_id, ol_o_id, ol_number);",
]

time.sleep(7.0)
conn = get_conn("localhost", "benchbase", "admin", "")
for sql in creat_index_list:
    run_query(conn, sql)
