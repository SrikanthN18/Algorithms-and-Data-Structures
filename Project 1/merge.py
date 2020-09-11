import time

def mergesort(inp):

	if len(inp)>1:
		mid = len(inp)//2
		i = 0
		lefthalf = []
		while(i != mid):
			lefthalf.append(inp[i])
			i += 1

		j = mid
		righthalf = []
		n = len(inp)
		while(j != n):
			righthalf.append(inp[j])
			j += 1

		mergesort(lefthalf)
		mergesort(righthalf)

		'''   Merging Code'''
		i = j = k = 0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				inp[k]=lefthalf[i]
				i=i+1
			else:
				inp[k]=righthalf[j]
				j=j+1
			k=k+1

		while i < len(lefthalf):
			inp[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			inp[k]=righthalf[j]
			j=j+1
			k=k+1

r = int(input("Enter the input size\n"))
f1 = open('random.txt','r')
l = []
for line in f1.readlines():
	l.append(line.rstrip('\n'))
f1.close()

inp = []
for i in range(r):
	inp.append(int(l[i]))


#TO SORT THE UNSORTED INPUT
start = time.time()
mergesort(inp)
end = time.time()
time1 = end - start
print(time1)

#TO SORT THE SORTED INPUT
start = time.time()
mergesort(inp)
end = time.time()
time2 = end - start
print(time2)


#TO SORT THE INVERSED SORTED INPUT
rev = inp[::-1]
start = time.time()
mergesort(rev)
end = time.time()
time3 = end - start
print(time3)


