#Big Sorting
#!/bin/python3

import sys
import collections as c

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)

d = c.defaultdict(list)

for i in unsorted:
    d[len(i)].append(i)

for key in sorted(d.keys()):
    print(*sorted(d[key]), sep='\n')

#Insertion Sort - Part 1
n = int(input())
arr = list(map(int, input().strip().split(' ')))
e = arr[-1]
arr[-1] = []
f = []
for i in range(1,n):
    ee = arr[-i-1]
    r = arr[:-i-1]    #elements to the right of ee
    l = arr[-i:]    #elements to the left of ee
    if ee>e:    #the list won't be sorted
        r.append(ee)
        r.append(ee)
        for x in l:
            r.append(x)
        r.pop()
        print (' '.join(str(x) for x in r))
    if ee<e:    #the list will be sorted unless e is the smallest element of the array
        r.append(ee)
        r.append(e)
        for x in l:
            r.append(x)
        r.pop()
        print (' '.join(str(x) for x in r))
        break
    if i == n-1:    #if e is the smallest element of the array
        f.append(e)
        f.append(ee)
        l.pop()
        for x in l:
            f.append(x)
        print (' '.join(str(x) for x in f))

#Insertion Sort - Part 2
n = int(input())
list = list(map(int, input().strip().split(' ')))
for i in range(1, len(list)):
        for j in range(0, i):
            if (list[i] < list[j]):
                item = list.pop(i)
                list.insert(j, item)
        print (' '.join(str(x) for x in list))

#Correctness and the Loop Invariant
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))


#Running Time of Algorithms
n = int(input())
list = list(map(int, input().strip().split(' ')))
c = 0
for i in range(1, len(list)):
        for j in range(0, i):
            if (list[i] < list[j]):
                c += 1
print (c)

#Quicksort 1 - Partition
n = int(input())
arr = list(map(int, input().strip().split(' ')))
p = arr[0]
left = []
right = []
final = []
for el in arr[1:]:
    if el < p :
        left.append(el)
    else:
        right.append(el)
for el in left:
    final.append(el)
final.append(p)
for el in right:
    final.append(el)
for el in final:
    print (el, end=' ')

#Counting Sort 1
n = int(input())
arr = list(map(int, input().strip().split(' ')))
f = []
for el in range(100):
    c = arr.count(el)
    f.append(c)
print (*f)

#Counting Sort 2
n = int(input())
arr = list(map(int, input().strip().split(' ')))
f = []
for el in range(100):
    c = arr.count(el)
    while c != 0:
        f.append(el)
        c -= 1
print (*f)

#The Full Counting Sort
n = int(input())
dct = {}
for i in range(n):
    t = input().strip().split()
    num = int(t[0])
    lin = t[1]

    if i < n / 2:
        lin = "-"

    if num in dct:  # the keys are the numbers, the values are the ascii characters
        dct[num].append(lin)
    else:
        dct[num] = [lin]

maxNum = max(dct.keys())
output = []

for i in range(maxNum + 1):
    if i in dct:
        for line in dct[i]:
            output.append(line)


#Closest Numbers
n = int(input())
l = list(map(int, input().strip().split()))
l.sort()
diff = l[1]-l[0]
f = [l[0], l[1]]
for i in range(1, len(l)-1):
    d = l[i+1]-l[i]    #he difference between the two numbers we are comparing
    if d == diff:
        f.append(l[i])
        f.append(l[i+1])
    if d < diff:
        f = []    #empty the list because there is a new pair of numbers with lowest difference
        f.append(l[i])
        f.append(l[i+1])
        diff = abs(d)
print (*f)