Group Members:

    Roxanne Dewing
    Jamie Kihira
    Justin Bao


Contents:
    1. sud2sat.py
       This program reads a partially solved sudoku puzzle and converts it to
       a CNF formula suitable for input to the miniSAT SAT solver.
       It is intended to be used with the sudoku (only one and not multiple)
       being piped in through stdin and the CNF formula being piped out through
       stdout.  i.e. it is intended to be used as follows:
       cat <file with sudoku> | python3 sud2sat.py > <file with CNF formula>
       or
       python3 sud2sat.py < <file with sudoku> > <file with CNF formula>
       Here is an example:
       cat grid01.txt | python3 sud2sat.py > sat_input01.txt

    2. sat2sud.py
       This program reads output from the miniSAT SAT solver and converts it to
       a solved sudoku puzzle.
       It is intended to be used with the filename of the output from the SAT
       solver being passed in as an argument and the solved sudoku being output
       through stdout.  Note that the different method for reading in input
       compared to sud2sat.py stems from the fact that these two programs were
       made by different students.
       The program should be run with:
       python3 sat2sud.py <file with miniSAT output> > <file with solved sudoku>
       Here is an example:
       python3 sat2sud.py sat_output01.txt > solution01.txt

    3. sud2sat_hard.py (For Extended Task 1)
       This program reads all the puzzles that can be found at magictour.free.fr/top95
       and converts them to CNF formulae suitable for the miniSAT SAT solver.
       Note that the CNF formula for each puzzle will be in separate files even
       if all the files are read from the same file.
       The program uses stdin for input and write to files called hard_grid#.txt where
       # is the order in which the puzzle came in in the first file.  i.e, this
       program writes a CNF formula to 95 different files named hard_grid#.txt
       where # ranges from 1 to 95.
       The program should be run with:
       cat <file with the hard sudoku puzzles> | python3 sud2sat_hard.py
       or
       python3 sud2sat_hard.py > <file with the hard sudoku puzzles>
       Here is an example:
       cat all_hard_puzzles.txt | python3 sud2sat_hard.py

    4. sud2sat_alt.py (For Extended Task 2)
       This program does the exact same thing as sud2sat.py except it uses an
       alternative encoding thought of by the group instead of the minimal
       encoding which is used in sud2sat.py.
       The program is intended to be run with:
       cat <file with sudoku puzzle> | python3 sud2sat_alt.py > <file with CNF formula>
       or
       python3 sud2sat_alt.py < <file with sudoku puzzle> > <file with CNF formula>
       Here is an example:
       cat grid01.txt | python3 sud2sat_alt.py > sat_input_alt01.txt

    5. nbyn_sud2sat.py (For Extended Task 3)
       This program essentially does the same thing as sud2sat.py except it is
       generalized for n by n sudoku puzzles.
       Some input modifications:
           The very first line of the file with the puzzle should have three
           space separated integers, n, r, c where n is the number of cells in
           a row or a column, r is the number of rows in a subgrid, and c is
           the number of columns in a subgrid. An error message will be output
           and execution terminated if r * c != n.
           The only wild card character allowed will be a '0' (no '.','*', or '?')
           and all numbers in the puzzle should be separated by spaces (this is
           to accomodate for two digit numbers).
           An example input file will look like the following:

           4 2 2
           1 0 0 3
           0 0 2 0
           0 3 0 0
           0 0 4 0

       The program is intended to have the input file piped in though stdin and the
       output file with the CNF formula written to through stdout.
       i.e. the program should be run with:
       cat <file with puzzle> | python3 nbyn_sud2sat.py > <file with CNF formula>
       or
       python3 nbyn_sud2sat.py < <file with puzzle> > <file with CNF formula>
       Here is an example
       cat 12by12_sudoku.txt | python3 nbyn_sud2sat.py > 12by12_input.txt

    6. nbyn_sat2sud.py (For Extended Task 3)
       This program essentially does the same thing as sat2sud.py except it is
       generalized for n by n puzzles.
       The program has all the input passed in as arguments.  The first argument
       will be a number n signifying the number of rows or columns in the puzzle,
       the second argument is the name of the file with the output from the SAT
       solver. Output is output through stdin.
       The program should be run with:
       python3 nbyn_sat2sud.py <number for size of puzzle> <file with SAT output> > <solved solution to sudoku puzzle>
       Here is an example:
       python3 nbyn_sat2sud.py 12 12by12_output.txt > 12by12_solution.txt

    7. Report
       The report is a pdf summarizing the results of solving sudoku puzzles
       with the miniSAT SAT solver.

Some Extra files in this Submission:
    8. check_sudoku.py
       This program was used to verify that the solutions given by the
       miniSAT and converted to a sudoku via sat2sud.py are valid solutions.
       Note that this program only works for 9 by 9 sudoku puzzles.
       The program outputs 'pass' to stdout if the sudoku is valid and 'fail'
       otherwise. The input file is intended to be input through stdin.
       The program is supposed to be run with:
       cat <sudoku to be checked> | python3 check_sudoku.py
       or
       python3 check_sudoku.py < <sudoku to be checked>
       Here is an example:
       python3 check_sudoku.py < solution01.txt

    9. minisat_standard_tasks.sh
       This is a shell script that runs sud2sat.py, the minisat, sat2sud.py
       and check_sudoku.py for all 50 puzzles of the basic tasks.
       The solution to each puzzle will be output to a file called
       solution#.txt where # is the order in which the puzzle came in.
       Note that for this script to work, the each puzzle must be stored in
       a file name grid#.txt with # as above. Note that # must be two digits
       so 1 would be 01.
       Should be run with:
       ./minisat_standard_tasks.sh

    10.run_hard_puzzles.sh (For Extended Task 1)
       Same idea as minisat_standard_tasks.sh except it is used for the hard
       inputs in the first extended task.  The solution to each puzzle will be
       output to a file called solution_hard#.txt where # is the order in which
       the puzzle is processed.
       Note that for this script to work, the hard inputs must be stored in a
       file called all_hard_processes.txt.
       Should be run with:
       ./run_hard_puzzles.sh

    11.minisat_standard_tasks_alt.sh (For Extended Task 2)
       This is essentially the same as minisat_standard_tasks.sh except it uses
       sud2sat_alt.py which uses the alternative encoding.
       Note that for this script to work, the each puzzle must be stored in
       a file name grid#.txt with # as above. Note that # must be two digits
       so 1 would be 01.
       Should be run with:
       ./minisat_standard_tasks_alt.sh
