cd benchbase-2021-SNAPSHOT/
rm -r results
python3 ../tpcc_drop_index.py
truncate -s0 ../logfile
java -jar benchbase.jar -b tpcc -c config/postgres/sample_tpcc_config.xml --create=false --load=false --execute=true &
python3 ../tpcc_add_index.py