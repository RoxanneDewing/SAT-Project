#!/bin/bash

for q in {1..9}
do
	echo "Checking grid0$q"
	cat grid0$q.txt | python3 sud2sat.py > sat_input0$q.txt
	minisat sat_input0$q.txt sat_output0$q.txt
	python3 sat2sud.py sat_output0$q.txt > solution0$q.txt
	python3 check_sudoku.py < solution0$q.txt
	echo "-------------------------------------------------"
done

for q in {10..50}
do
	echo "Checking grid$q"
	cat grid$q.txt | python3 sud2sat.py > sat_input$q.txt
	minisat sat_input$q.txt sat_output$q.txt
	python3 sat2sud.py sat_output$q.txt > solution$q.txt
	python3 check_sudoku.py < solution$q.txt
	echo "-------------------------------------------------"
done
