import sys

def convert(t):
	return (81 * (t[0] - 1) + 9 * (t[1] - 1) + t[2])

def get_singletons(numbers, clauses):
	for i in range(len(numbers)):
		if numbers[i] > 0:
			clauses.append(' '.join([str(convert((int(i / 9) + 1, i % 9 + 1, numbers[i]))), '0']))

def existence(clauses):
	for i in range(1, 9 + 1):
		for j in range(1, 9 + 1):
			s = [str(convert((i, j, k))) for k in range(1, 9 + 1)]
			s.append('0')
			clauses.append(' '.join(s))

def rows(clauses):
	for i in range(1, 9 + 1):
		for k in range(1, 9 + 1):
			for j in range(1, 8 + 1):
				for l in range(j + 1, 9 + 1):
					clauses.append(' '.join([str(-convert((i, j, k))), str(-convert((i, l, k))), '0']))

def cols(clauses):
	for j in range(1, 9 + 1):
		for k in range(1, 9 + 1):
			for i in range(1, 8 + 1):
				for l in range(i + 1, 9 + 1):
					clauses.append(' '.join([str(-convert((i, j, k))), str(-convert((l, j, k))), '0']))

def subgrids(clauses):

	for k in range(1, 9 + 1):
		for a in range(2 + 1):
			for b in range(2 + 1):
				for u in range(1, 3 + 1):
					for v in range(1, 2 + 1):
						for w in range(v + 1, 3 + 1):
							clauses.append(' '.join([str(-convert((3 * a + u, 3 * b + v, k))), str(-convert((3 * a + u, 3 * b + w, k))), '0']))
						
						
	for k2 in range(1, 9 + 1):
		for a2 in range(2 + 1):
			for b2 in range(2 + 1):
				for u2 in range(1, 3 + 1):
					for v2 in range(1, 3 + 1):
						for w2 in range(u2 + 1, 3 + 1):
							for t2 in range(1, 3+1):
								clauses.append(' '.join([str(-convert((3 * a2 + u2, 3 * b2 + v2, k2))), str(-convert((3 * a2 + w2, 3 * b2 + t2, k2))), '0']))
							
def get_rules(clauses):
	existence(clauses)
	rows(clauses)
	cols(clauses)
	subgrids(clauses)

def main():
	s = sys.stdin.read().replace('.', '0').replace('\n', '').replace('\r', '').replace('?', '0').replace('*', '0').replace(' ', '')
	numbers = [int(c) for c in s]
	clauses = []
	get_singletons(numbers, clauses)
	get_rules(clauses)
	print(' '.join(['p cnf', '729', str(len(clauses))]))
	print('\n'.join(clauses))

if __name__ == '__main__':
	main()
