#!/bin/bash
truncate logfile -s0
python3 execute.py type1.txt
cp logfile type1_1_result.txt
truncate logfile -s 0
python3 execute.py type2.txt
cp logfile type1_2_result.txt
truncate logfile -s 0
python3 execute.py type3.txt
cp logfile type1_3_result.txt
truncate logfile -s 0
python3 execute.py type4.txt
cp logfile type1_4_result.txt
truncate logfile -s 0