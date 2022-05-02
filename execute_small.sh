#!/bin/bash
num=$1

truncate logfile -s0
python3 execute.py type1_small.txt
cp logfile type${num}_1_result.txt
truncate logfile -s 0
python3 execute.py type2_small.txt
cp logfile type${num}_2_result.txt
truncate logfile -s 0
python3 execute.py type3_small.txt
cp logfile type${num}_3_result.txt
truncate logfile -s 0
python3 execute.py type4_small.txt
cp logfile type${num}_4_result.txt
truncate logfile -s 0