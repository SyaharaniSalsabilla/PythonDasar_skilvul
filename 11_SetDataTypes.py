# Set - Definition and Declaration
days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' , 'Sun' ] # list
days_set = set(days_list) # membuat set dari list
print(days_set)

fruits_tuple = ('apple','orange','water melon')
fruits_set = set(fruits_tuple) # membuat set dari tuple
print(fruits_set)


# Set - Check Value in Sets
numbers = {2,1,3}
for x in numbers:
  print(x)

numbers = {2,1,3}
if 1 in numbers:
  print("1 terdapat dalam set")

numbers = {1,2,3}
numbers.add(4)
print(numbers)

numbers = {1,2,3,4}
numbers.remove(4)
print(numbers)