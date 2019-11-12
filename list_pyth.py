#list in python
#like array

print range
print(thislist[2:5])


change item
thislist[1]="hi"


loop through list
for x in thislist:
	print x


check if item exists or not
if "apple" in thislist:
	print ("Found")


length of the list
len(thislist)


add items
thislist.append("fjf")


insert at an index
thislist.insert(1,"orange")


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
removes specified item
thislist.remove("hello")


to pop from end
thislist.pop()


to delete specified index
del thislist[0]


to delete the list completely
del thislist


to empty the list
thislist.clear()


copy a list
mylist=thislist.copy()


to join two lists
list3=list1+list2

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
