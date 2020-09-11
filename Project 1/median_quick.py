import time

r = int(input("Enter the input size\n"))
f1 = open('random.txt','r')
l = []
for line in f1.readlines():
  l.append(line.rstrip('\n'))
f1.close()

inp = []
for i in range(r):
  inp.append(int(l[i]))

def insertion_sort(a,low,high):
    for ele in range(low+1,high+1):
        key = a[ele]
        j = ele-1
        while(j>=0 and key < a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

def decide_algo(a,low,high):
   if(low + 10 <= high): 
      if low<high:
          piv = partition(a,low,high)
          decide_algo(a,low,piv-1)
          decide_algo(a,piv+1,high)
   else:
      insertion_sort(a,low,high)

def quicksort(a,low,high):
   decide_algo(a,low,high)   

def median(a, low, high, median):
  if a[low] < a[high]:
     
    return high if a[high] < a[median] else median
  else:
    return low if a[low] < a[median] else median

def partition(a,low,high):
   pindex = median(a, low, high, (low + high) // 2)
   a[low], a[pindex] = a[pindex], a[low]
   pivot = a[low]
   
   left = low
   right = high
   
   flag = False
   while not flag:
       while left <= right and a[left] <= pivot:
           left = left + 1

       while a[right] >= pivot and right >= left:
           right = right -1

       if right < left:
           flag = True
       else:
           a[left],a[right] =a[right],a[left]

   temp = pivot
   a[a.index(pivot)] = a[right]
   a[right] = temp
  


   return right



low = 0
high = len(inp)-1
#TO SORT THE UNSORTED LIST
start = time.time()
quicksort(inp,low,high)
end = time.time()
tim1 = end-start
print(tim1)

#TO SORT THE SORTED LIST
start = time.time()
quicksort(inp,low,high)
end = time.time()
tim2 = end-start
print(tim2)

#TO SORT THE REVERSED SORTED LIST
rev = inp[::-1]
start = time.time()
quicksort(rev,low,high)
end = time.time()
tim3 = end-start
print(tim3)
