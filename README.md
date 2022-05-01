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

To switch to a certain branch and install invoke like `bash install_verion.sh sort`. Remember to re-launch postgres if switching to another postgres.

To start/stop pg instance locally, invoke `bash launch_pg.sh` and `bash stop_pg.sh`

Experiment procedures:
1. Generate dataset:
I have already included the dataset I used for experiment. The generation procedure is:
```bash
python3 gen_dataset.py
```

2. Generate test traces:
Note I used fixed scan range. SO NO SWITCHING HAPPENS! Need to fix this.
```bash
python3 gen_stmt.py
```

3. Run experiments:
First: load dataset
```
psql test
create table t1 (id int, value int);
COPY t1 FROM '/home/ubuntu/data.csv' DELIMITER ',' CSV HEADER;
```
Then: Change the script execute.sh which uses execute.py. After changing:
Argument: 1: ours, 2: pg, 3: force-replan
```bash
./execute.sh 1
```

4. Pre-process output
For each output:
```bash
python3 process_output.py type1_1_result.txt
```

5. Download all the outputs to your local PC. Then use the Draw.ipynb for later drawing.