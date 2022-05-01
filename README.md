# 15712-Experiment-Pilot
Experiment Framework for 15-712: Adaptive Compiled Query

To install the dependency:
```
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
sudo apt install gcc make libreadline8 libreadline-dev zlib1g zlib1g-dev build-essential bison postgresql-client llvm clang flex
pip3 install psycopg2 pandas matplotlib
```

To set environment variables:
```
LD_LIBRARY_PATH=/usr/local/pgsql/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH
PATH=/usr/local/pgsql/bin:$PATH
export PATH
```

To clone and build a certain branch, invoke like `bash build_version.sh sort`

To switch to a certain branch and install invoke like `bash install_verion.sh sort`

To start/stop pg instance locally, invoke `bash launch_pg.sh` and `bash stop_pg.sh`