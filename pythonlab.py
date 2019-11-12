#!/usr/bin/env python
# coding: utf-8

# In[1]:


r=10
pi = 3.14
volume = (4/3)*pi*r*r*r
print (volume)


# In[ ]:


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def power(a,b):
    return pow(a,b)
def div(a,b):
    return a/b

def cal(d,a,b):
    return d(a,b)

cal(power,5,10)


# In[5]:


def is_triangle(a,b,c):
    if a+b>=c and b+c>=a and a+b>=c:
        return "YES"
    else:
        return "NO"

a = int(input())
b = int(input())
c = int(input())

is_triangle(a,b,c)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# In[1]:



def f(n):
    if n == 1 or n == 2:
        return 1
    return  f(n-1) + f(n-2)
        
n = int(input())
for i in range(1,n+1):
    print (f(i), end=" ")
f(n)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# In[27]:


import math
const = 2*math.sqrt(2)/9801
k = 0
s = 0
var = pow(10,-15)
while 1:
    temp = const*math.factorial(4*k)*(1103 + 26390*k)/(pow(math.factorial(k),4)*pow(396,4*k))
    if temp<var :
        break
    s = s+ temp
    k = k+1

print (1/s)
print(math.pi)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
# In[5]:


def my_reverse(s):
    rev_s = ''
    for i in s:
        rev_s = i + rev_s
    print (rev_s) 

s = input()    
my_reverse(s)    

#or
import math
def my_rev(s):
    s1=''
    n=len(s)
    for i in range(0,n):
        s1=s1+s[n-1-i]
    print(s1)
s=input()
my_rev(s)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
#QUES 7


def find_count(s, index, elem):
    l = len(s)
    k=0
    arr = []
    for i in range(index+1,l):
        if elem == s[i]:
            arr.append(i)
            k = k +1
    print(k,arr)        
s = input()
p = int(input())
elem = input()
find_count(s,p,elem)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
# QUES 8


arr = [int(i) for i in input().split()]
s = []
s.append(arr[0])

for j in range(1,len(arr)):
    s.append(s[j-1] + arr[j])
    
print (s)    
#or
import math 
def cum(l):
    ans=[]
    ans.append(l[0])
    for i in range(1,len(l)):
        ans.append(ans[i-1]+l[i])
    return ans
elem=[1,2,3,4]
print(cum(elem))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# QUES 9


def is_anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    else: 
        arr = []
        for i in range(26):
            arr.append(0)
        for i in s1:
            arr[ord(i)-ord('a')] +=1
        for i in s2:
            arr[ord(i)-ord('a')] -=1
            
        for i in range(26):
            if arr[i] != 0:
                return False
        return True    
s1 = input()
s2 = input()
is_anagram(s1,s2)
or
#import math
def is_ana(s1,s2):
    if len(s1) != len(s2):
        return False
    a= []
    b= []
    for i in range(0,len(s1)):
        a.append(s1[i])
        b.append(s2[i])    
    a.sort()
    b.sort()
    for i in range(0,len(s1)):
        if a[i] != b[i]:
            return False
    return True    
a=input()
b=input()
print(is_ana(a,b)) 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#QUES 10

Dic = {}

def frq(s):
    dic = {}
    for i in s:
        dic[i] = dic.get(i,0) +1
        Dic[s] = dic
    print (Dic)

s = input()
frq(s)
#or
import math
def qten(s):
    dic={}

    dic[s]={}
    for i in range(0,len(s)):
        if s[i] in dic[s]:
            dic[s][s[i]]+=1
        else:
            dic[s][s[i]]=1
    print(dic)
s=input()
qten(s)  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`

#QUES 11
import pickle
Dic = {}

def frq(s):
    dic = {}
    for i in s:
        dic[i] = dic.get(i,0) +1
        Dic[s] = dic
    
    
f = open('hello.txt',"r")
if f.mode == 'r':
    #contents = f.read()
    f1 = f.read()
    f1 = f1.split()
    for i in f1:
        frq(i)
        
    #print (Dic)
    
# Store data (serialize)
handle=open('Dic.pickle','wb')
pickle.dump(Dic, handle)
handle=open('Dic.pickle','rb')
b = pickle.load(handle)
handle.close()
print (b)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#QUES 12

import random
f= open("words.txt",r)
lines = f.read()
lines = lines.split()
lines = random.sample(lines,200)
lines.sort(key=len,reverse=True)
print(lines)
f.close()
f1 = open("words_200.txt", "w")

for i in lines:
    f1.write(i +'\n')
f1.close()    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os 
print(os.getcwd()) 
# To print absolute path on your system 
# os.path.abspath('.')  
  
# To print files and directories in the current directory 
# on your system 
# os.listdir('.') 
topdown − If optional argument topdown is True or not specified,
directories are scanned from top-down.
If topdown is set to False, directories are scanned from bottom-up.
import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#QUES 13

import os

def get_file_list(path):
    files= []

    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for k in f:
            files.append(os.path.join(r, k))
    for i in files:
         print(i)
        
path = os.getcwd()
get_file_list(path)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
# In[104]:


import sys

def sed(pattern,replace,file1,file2):
    f = open(file1,'r')
    filedata = f.read()
    f.close()

    newdata = filedata.replace(pattern,replace)

    f = open(file2,'w')
    f.write(newdata)
    f.close()

print ("enter pattern string")
s = input()
print ("enter replacement string")
r = input()
print ("enter file name 1")
f1 = input()
print ("enter file name 2")
f2 = input()

sed(s,r,f1,f2)   






