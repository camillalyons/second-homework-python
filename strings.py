#Making Anagrams
#!/bin/python3

import sys

def makingAnagrams(s1, s2):
    ss = s1+s2
    c = 0
    for letter in set(ss):
        a = s1.count(letter)
        b = s2.count(letter)
        c += abs(a-b)
    print (c)

s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
#print(result)

#Game of Thrones - I
# !/bin/python3

import sys


def gameOfThrones(s):
    flag = 0
    for letter in set(s):
        if s.count(letter) % 2 == 1:
            flag += 1
    if flag >= 2:
        print('NO')
    else:
        print('YES')


s = list(input().strip())
result = gameOfThrones(s)
# print(result)

#Two Strings
#!/bin/python3

import sys

def twoStrings(s1, s2):
    res = 'NO'
    for letter in set(s1):
        for let in set(s2):
            if letter==let:
                res = 'YES'
    else:
        print (res)

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    #print(result)

#Sherlock and the Valid String
#!/bin/python3

import sys
import collections
def isValid(s):
    freq = collections.Counter(s)
    vals = list(freq.values())
    vals.sort()    #this list contains all the values of each letter's occurrance
    if len(vals) == vals.count(vals[0]) or (len(vals)-1 == vals.count(vals[0]) and vals[-1]-vals[-2])==1 or (len(vals)-1==vals.count(vals[-1]) and vals[0]==1):
        #if all the occurrances are the same, or if there is only 1 letter thar differes of 1, or if one letter has occurrance 1 and all the other have the same occurrance
        print ('YES')
    else:
        print ('NO')
s = input().strip()
result = isValid(s)
#print(result)

#Palindrome Index
#!/bin/python3
n=int(input())
for n0 in range(n):
    s=list(input())
    if s[::-1]==s:
        print (-1)
    else:
        for i in range(1,(len(s)//2)+1):
            if s[i-1]!= s[-i]:
                break
        s1=s[:]
        del s[i-1]
        del s1[-i]
        if s[::-1]==s:
            print (i-1)
        else:
            print (len(s)+1-i)