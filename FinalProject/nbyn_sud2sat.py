import sys

def convert(n, i, j, k, t):
	return str(t * ((n ** 2) * (i - 1) + n * (j - 1) + k))
	
def get_singletons(n, numbers, clauses):
	for i in range(len(numbers)):
		if numbers[i] > 0:
			clauses.append(' '.join([convert(n, int(i / n) + 1, i % n + 1, numbers[i], 1), '0']))

def existence(n, clauses):
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			s = [convert(n, i, j, k, 1) for k in range(1, n + 1)]
			s.append('0')
			clauses.append(' '.join(s))

def rows(n, clauses):
	for i in range(1, n + 1):
		for k in range(1, n + 1):
			for j in range(1, n - 1 + 1):
				for l in range(j + 1, n + 1):
					clauses.append(' '.join([convert(n, i, j, k, -1), convert(n, i, l, k, -1), '0']))

def cols(n, clauses):
	for j in range(1, n + 1):
		for k in range(1, n + 1):
			for i in range(1, n - 1 + 1):
				for l in range(i + 1, n + 1):
					clauses.append(' '.join([convert(n, i, j, k, -1), convert(n, l, j, k, -1), '0']))

def subgrids(n, subrows, subcols, clauses):
	for k in range(1, n + 1):
		for a in range(subcols - 1 + 1):
			for b in range(subrows - 1 + 1):
				for u in range(1, subrows + 1):
					for v in range(1, subcols - 1 + 1):
						for w in range(v + 1, subcols + 1):
							clauses.append(' '.join([convert(n, subrows * a + u, subcols * b + v, k, -1), convert(n, subrows * a + u, subcols * b + w, k, -1), '0']))
											
	for k2 in range(1, n + 1):
		for a2 in range(subcols - 1 + 1):
			for b2 in range(subrows - 1 + 1):
				for u2 in range(1, subrows + 1):
					for v2 in range(1, subcols + 1):
						for w2 in range(u2 + 1, subrows + 1):
							for t2 in range(1, subcols + 1):
								clauses.append(' '.join([convert(n, subrows * a2 + u2, subcols * b2 + v2, k2, -1), convert(n, subrows * a2 + w2, subcols * b2 + t2, k2, -1), '0']))
							
def get_rules(n, subrows, subcols, clauses):
	existence(n, clauses)
	rows(n, clauses)
	cols(n, clauses)
	subgrids(n, subrows, subcols, clauses)

def main():
	s = sys.stdin.readline().split()
	n = int(s[0])
	subrows = int(s[1])
	subcols = int(s[2])
	if subrows * subcols != n:
		print('Error: the number of rows/columns is not equal to the number of cells in the subgrid')
		sys.exit()	
	numbers = [int(c) for c in sys.stdin.read().split()]
	singletons = []
	get_singletons(n, numbers, singletons)
	clauses = []
	get_rules(n, subrows, subcols, clauses)
	print(' '.join(['p cnf', str(n ** 3), str(len(clauses) + len(singletons))]))
	print('\n'.join(singletons), end = '\n')
	print('\n'.join(clauses))

if __name__ == '__main__':
	main()