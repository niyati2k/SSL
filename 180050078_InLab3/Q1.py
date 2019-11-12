import math
def isSquare(a):
	if(a<0):
		return 0
	b=math.sqrt(a)
	c=int(b)
	if(c*c==a):
		return 1
	else:
		return 0

n=int(input())
l=map(int,input().split())
# print (l)
for a in l:
	# a=int(input())
	if(isSquare(a)==1):
		print("{} is a square number".format(a))
	else:
		print("{} is not a square number".format(a))
