~~SPLIT~~
split() method returns a list of strings after breaking the given string by the specified separator.

str.split(separator, maxsplit)

# Splitting at 3 
print([word[i:i+3] for i in range(0, len(word), 3)]) 



~~RANDOM~~
random.sample (x, k)
where x is the list and k is the number of elements you want.


a = [1,2,3,4,5,6,7,8,9]
random.shuffle(a)
print a[:4] # prints 4 random variables


if you have a list called x, you can call random.shuffle(x)
to have the random shuffle function reorder the list in a randomized way

To choose a single element, use random.choice(x), where x is the name of your list.
The function returns a single, randomly selected element from list x. 


~~SORT~~
list.sort(reverse=True|False, key=myFunc)
#Sort the list by the length of the values:
# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)



#Sort the list by the length of the values and reversed:
# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
