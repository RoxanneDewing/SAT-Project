#Please use stdin for using the program
#run with python3 check_sudoku.py < file

import sys

def check_rows(sud, checker):
	for row in sud:
		for num in row:
			checker[num] = checker[num] + 1
			if checker[num] > 1:
				return False
		for i in range(len(checker)):
			checker[i] = 0
	for i in range(len(checker)):
		checker[i] = 0
	return True

def check_cols(sud, checker):
	for j in range(len(sud)):
		for i in range(len(sud)):
			checker[sud[i][j]] = checker[sud[i][j]] + 1
			if checker[sud[i][j]] > 1:
				return False
		for i in range(len(checker)):
			checker[i] = 0
	for i in range(len(checker)):
		checker[i] = 0
	return True
	
def check_grids(sud, checker):
	for u in range(3):
		for v in range(3):
			for i in range(3 * u, 3 * u + 3):
				for j in range(3 * v, 3 * v + 3):
					checker[sud[i][j]] = checker[sud[i][j]] + 1
					if checker[sud[i][j]] > 1:
						return False
			for i in range(len(checker)):
				checker[i] = 0
	for i in range(len(checker)):
		checker[i] = 0
	return True

def main():
	sud = [[int(c) for c in s.rstrip()] for s in sys.stdin.readlines()]
	checker = [0 for i in range(9 + 1)]
	if check_rows(sud, checker) and check_cols(sud, checker) and check_grids(sud, checker):
		print('pass')
	else:
		print('fail')

if __name__ == '__main__':
	main()