#dictionary
#like maps

Get the value of the "model" key:
x=thisdict["model"]


Print all the key names in the dictionary
for x in thisdict:
	print (x)

Iterate through the values
for x in thisdict.values():
	print(x)


Loops through both keys and values
for x,y in thisdict.items():
	print(x,y)

Find if key present or not
if "model" in thisdict:
	print("yes")


Length
len(thisdict)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To removes the item with the specified key name:
thisdict.pop("model")	


Remove last inserted item
thisdict.popitem()


Remove item with specified key name
del thisdict["model"]

Delete the dictionary completely
del thisdict


Clear,Copy same aS lisT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys