#!/bin/bash
num=$1

truncate logfile -s0
python3 execute.py type1.txt
cp logfile type${num}_1_result.txt
truncate logfile -s 0
python3 execute.py type2.txt
cp logfile type${num}_2_result.txt
truncate logfile -s 0
python3 execute.py type3.txt
cp logfile type${num}_3_result.txt
truncate logfile -s 0
python3 execute.py type4.txt
cp logfile type${num}_4_result.txt
truncate logfile -s 0