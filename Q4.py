n = int(input())
l1=[]
for i in range(n):
	l1.append(input())
#print(l1)
dict1=dict(item.split(":") for item in l1)
#print(dict1)

dict2={}
for k,v in dict1.items():
	#print(v)
	x = v.split(",")
	#print(x)
	dict2.__setitem__(k,dict(item.split("-") for item in x))
#print(dict2)

for k,v in dict2.items():
	for k1,v1 in v.items():
		v[k1]=int(v1)

#print(dict2)

dict3={}
for k,v in dict2.items():
	for k1,v1 in v.items():
		dict3[k1]=dict3.get(k1,0)+v1

#print(dict3)

l=[]
for k,v in dict3.items():
	l.append((k,v))

print(l)
sorted_l = sorted(l, key=lambda t: (t[1],t[0]),reverse=True)
print(sorted_l)


