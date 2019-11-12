import os
import sys
fd=sys.argv[1]
class Student:
	num_students=0
	# grades=[]
	# credits=[]
	def __init__(self,g=[],c=[]):
		self.grades=g
		# print(grades)
		self.credits=c
		# print(credits)
		Student.num_students+=1
	def CPI(self):
		sum_cred=0
		sumtotal=0
		for i in range(len(self.grades)):
			sum_cred+=self.credits[i]
			sumtotal+=(self.credits[i]*self.grades[i])
		return sumtotal/sum_cred
# fd=$1
file=open(fd,'r')
text=file.read()
l=text.split("---\n")
cp=[]
for i in l:
	gc=i.split("\n")
	# print(gc[0])
	# print(gc[1])
	g=list(map(int,gc[0].split(" ")))
	c=list(map(int,gc[1].split(" ")))
	x=Student(g,c)
	cp.append(x.CPI())
print(Student.num_students)

for i in cp:
	print("%.4f"%i)
