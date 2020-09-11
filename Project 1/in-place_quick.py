import time
import sys
sys.setrecursionlimit(300000)
def partition(lst,first,last):
    pivot = lst[last]
    i = first - 1
    for k in range(first,last):
        if lst[k] <= pivot:
            i += 1
            lst[i],lst[k] = lst[k],lst[i]
    lst[i+1],lst[last] = lst[last],lst[i+1]
    return i+1


def quicksort(unsorted_list,first,last):
    if last > first:
        pivot = partition(unsorted_list,first,last)
        quicksort(unsorted_list,first,pivot-1)
        quicksort(unsorted_list,pivot+1,last)




f1 = open('random.txt','r')
l = []
for line in f1.readlines():
	l.append(line.rstrip('\n'))
f1.close()


r = int(input("Enter the input size\n"))
inp = []
for i in range(r):
	inp.append(int(l[i]))


first = 0
last = len(inp)-1

#TO SORT THE UNSORTED INPUT
start = time.time()
quicksort(inp,first,last)
end = time.time()
tim1 =  end - start
print(tim1)


#TO SORT THE SORTED INPUT
start = time.time()
quicksort(inp,first,last)
end = time.time()
tim2 =  end - start
print(tim2)


#TO SORTED THE INVERSED INPUT
rev = inp[::-1]
start = time.time()
quicksort(rev,first,last)
end = time.time()
tim3 =  end - start
print(tim3)



