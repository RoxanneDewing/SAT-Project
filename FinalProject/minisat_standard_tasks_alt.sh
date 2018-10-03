#!/bin/bash

for q in {1..9}
do
	echo "Checking grid0$q"
	cat grid0$q.txt | python3 sud2sat_alt.py > alt_sat_input0$q.txt
	minisat alt_sat_input0$q.txt alt_sat_output0$q.txt
	python3 sat2sud.py alt_sat_output0$q.txt > alt_solution0$q.txt
	python3 check_sudoku.py < alt_solution0$q.txt
	echo "-------------------------------------------------"
done

for q in {10..50}
do
	echo "Checking grid$q"
	cat grid$q.txt | python3 sud2sat_alt.py > alt_sat_input$q.txt
	minisat alt_sat_input$q.txt alt_sat_output$q.txt
	python3 sat2sud.py alt_sat_output$q.txt > alt_solution$q.txt
	python3 check_sudoku.py < alt_solution$q.txt
	echo "-------------------------------------------------"
done
