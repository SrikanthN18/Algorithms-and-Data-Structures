import time
r = int(input("Enter the input size\n"))
f1 = open('random.txt','r')
l = []
for line in f1.readlines():
	l.append(line.rstrip('\n'))
f1.close()

def insertion_sort(lst):
	for i in range(1,len(lst)):
		for j in range(i-1,-1,-1):
			if lst[j] > lst[j+1]:
				lst[j],lst[j+1] = lst[j+1],lst[j]
			else:
				break



inp = []
for i in range(r):
	inp.append(int(l[i]))


# TO SORT UNSORTED LIST
start = time.time()
insertion_sort(inp)
end = time.time()
tim1 = end - start
print(tim1)


#TO SORT SORTED LIST
start = time.time()
insertion_sort(inp)
end = time.time()
tim2 = end - start
print(tim2)


rev = inp[::-1]
#TO SORT REVERSED SORTED LIST
start = time.time()
insertion_sort(rev)
end = time.time()
tim3 = end - start
print(tim3)



