import sys

def convert(i, j, k, t):
	return str(t * (81 * (i - 1) + 9 * (j - 1) + k))
	
def get_singletons(numbers, clauses):
	for i in range(len(numbers)):
		if numbers[i] > 0:
			clauses.append(' '.join([convert(int(i / 9) + 1, i % 9 + 1, numbers[i], 1), '0']))

def cell_limits(clauses):
	for i in range(1, 9 + 1):
		for j in range(1, 9 + 1):
			for k in range(1, 8 + 1):
				for l in range(k + 1, 9 + 1):
					clauses.append(' '.join([convert(i, j, k, -1), convert(i, j, l, -1), '0']))
					
def rows(clauses):
	l = []
	for k in range(1, 9 + 1):
		for i in range(1, 9 + 1):
			l = [convert(i, j, k, 1) for j in range(1, 9 + 1)]
			l.append('0')
			clauses.append(' '.join(l))

def cols(clauses):
	l = []
	for k in range(1, 9 + 1):
		for j in range(1, 9 + 1):
			l = [convert(i, j, k, 1) for i in range(1, 9 + 1)]
			l.append('0')
			clauses.append(' '.join(l))
			
def subgrids(clauses):
	for k in range(1, 9 + 1):
		for u in range(2 + 1):
			for v in range(2 + 1):
				l = []
				for i in range(3 * u + 1, 3 * u + 3 + 1):
					l.extend([convert(i, j, k, 1) for j in range(3 * v + 1, 3 * v + 3 + 1)])
				l.append('0')
				clauses.append(' '.join(l))

def get_rules(clauses):
	cell_limits(clauses)
	rows(clauses)
	cols(clauses)
	subgrids(clauses)

def main():
	s = sys.stdin.read().replace('.', '0').replace('\n', '').replace('\r', '').replace('*', '0').replace('?', '0').replace(' ', '')
	numbers = [int(c) for c in s]
	clauses = []
	get_singletons(numbers, clauses)
	get_rules(clauses)
	print(' '.join(['p cnf', '729', str(len(clauses))]))
	print('\n'.join(clauses))	

if __name__ == '__main__':
	main()
