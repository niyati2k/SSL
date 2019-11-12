import os
fd="./Data/Heroes.txt"
file=open(fd,'r')
text=file.read()
file.close()
# print(text)
l=list(text.split("\n"))
l2=l
for i in range(len(l)):
	l2[i]=l[i].strip("\r")
# print(l)
i=0
os.mkdir("./Data/Survivors_of_Snap")
newdir="./Data/Survivors_of_Snap/"
path="./Data/Avengers_Universe/"
for filename in os.listdir(path):
	# i+=1
	file=open(path+filename,'r')
	text=file.read()
	l2=list(text.split("\n"))
	for j in l2:
		if j.strip("\r") in l:
			# print(filename)
			os.rename(path+filename,newdir+filename)
			break
	file.close()

# print(i)