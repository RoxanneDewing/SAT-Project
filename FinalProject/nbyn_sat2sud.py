import sys
	
def main():
	n = int(sys.argv[1])
	file = open(sys.argv[2],'r')
	
	#stores input on an array
	list = [int(x) for x in file.read().split()[1:] if int(x) > 0]
	file.close()
	list.sort() #just for good measure
	
	for i in range(len(list)):
		num = ((list[i] - 1) % n) + 1
		s = ''
		if i % n == n - 1:
			s = '\n'
		print('{:<4}'.format(num), end = s)
	
if __name__ == '__main__':
	main()