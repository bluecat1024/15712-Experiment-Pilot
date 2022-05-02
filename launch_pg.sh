bash stop_pg.sh

sudo mkdir /usr/local/pgsql/data
sudo chown ubuntu /usr/local/pgsql/data
initdb -D /usr/local/pgsql/data
sudo cp default.conf /usr/local/pgsql/data/postgresql.conf
pg_ctl -D /usr/local/pgsql/data -l logfile start

createdb benchbase
createuser -s -e admin 

createdb test