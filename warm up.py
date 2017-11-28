##Solve me first!
def solveMeFirst(a, b):
    # Hint: Type return a+b below
    return a + b


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1, num2)
print(res)

##Simple Array Sum
import sys

def simpleArraySum(n, ar):
    return sum(ar)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)

##Compae the triplets
import sys

def solve(a0, a1, a2, b0, b1, b2):
    A = 0
    B = 0
    for i in range(len(l1)):
        if l1[i] > l2[i]:
            A += 1
        if l1[i] < l2[i]:
            B += 1
    return A, B
a0, a1, a2 = input().strip().split(' ')
l1 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
l2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (' '.join(map(str, result)))

##A very big sum
import sys

def aVeryBigSum(n, ar):
    return sum(ar)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)

##Diagonal Difference
import sys
n = int(input())
d1 = []
d2 = []
for i in range(n):
    r = input().split()
    d1.append(int(r[i]))
    d2.append(int(r[n-i-1]))
print (abs(sum(d1) - sum(d2)))

##Plus Minus
import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
pos = 0
neg = 0
zer = 0
for el in arr:
    if el > 0:
        pos += 1
    if el < 0:
        neg += 1
    if el == 0:
        zer += 1
print (format(pos/n,  '.6f'))
print (format(neg/n,  '.6f'))
print (format(zer/n,  '.6f'))

##Staircase
import sys


n = int(input().strip())
for i in range(1, n+1):
    print (' '*(n-i) + i*'#')

##Mini-Max Sum
import sys

arr = list(map(int, input().strip().split(' ')))
arr.sort()
print (sum(arr[:4]), sum(arr[1:]))

##Birthday Cake Candles
import sys

def birthdayCakeCandles(n, ar):
    ma = max(ar)
    print (ar.count(ma))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
#print(result)