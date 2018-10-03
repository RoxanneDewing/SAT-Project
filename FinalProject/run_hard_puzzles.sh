#!/bin/bash

cat all_hard_processes.txt | python3 sud2sat_hard.py
for q in {1..95}
do
	echo "Checking hard_grid$q"
	minisat hard_grid$q.txt sat_output_hard$q.txt
	python3 sat2sud.py sat_output_hard$q.txt > solution_hard$q.txt
	python3 check_sudoku.py < solution_hard$q.txt
	echo "-------------------------------------------------"
done
