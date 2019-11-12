from collections import OrderedDict
dict={}
s=input()
# print (s)
# s=list(str(k))
for i in s:
	if i in dict:
		dict[i]+=1;
	else :
		dict[i]=1
# print (dict)
sor=(sorted(dict.items(),key=lambda x:(x[1],x[0]),reverse=True))
# print(sor)
for x,y in sor:
	print("{}: {}".format(x,y))
