import sys
	
def main():
#    line = input('Enter file name: ')
    file = open(sys.argv[1],'r')
    list = []
	
	#stores input on an array
    list = file.read().split()[1:]
    int_list = [int(x) for x in list]
    file.close()
    
    poslist = [x for x in int_list if x > 0]
    poslist.sort() #just for good measure
    
	
    for i in range(len(poslist)):
        num = ((poslist[i] - 1)%9) + 1
        s = ''
        if i % 9 == 8:
            s = '\n'
        print(num, end = s)
	
	
if __name__ == '__main__':
    main()
    
