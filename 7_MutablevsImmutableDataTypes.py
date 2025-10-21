# Mutable
a = ['apple','banana','orange']
print(id(a))
a.append('grapes')
print(id(a))
print(a)


# Immutable
# string
e = 'Halo, semua!'
print(id(e))
e = 'Halo, Apa kabar?'
print(id(e))
print(e)


# List - Declaration
fruits = ['banana', 'apple', 'orange', 'kiwi']  # list with strings
print(fruits)
mixed_list = [100, 200, 'apple', 400]
print(mixed_list)


# List - Indexing
n_list = [11,22,33,44,55,66]
print(n_list)
print(len(n_list))
print(n_list[0]) # indeks item pertama dari list adalah 0
print(n_list[1]) # index item kedua dari list adalah 1


# List - Addition and Deletion
# Addition
person1 = ['David Doe', 20,1,180.0,100.0]
person2 = ['John Smith', 25,1,170.0,70.0]
person_list = person1 + person2  # + Operator (tambahkan item dari dua list untuk membuat satu list)
print(person_list)

a_list = ['a','b','c','d','e']
a_list.append('f') # menambahkan karakter f
print(a_list)

list1 = ['a','b','c']
list2 = [1,2,3]
list1.extend(list2)
print(list1)
list1.extend('d')
print(list1)

# Deletion
n_list = [11,22,33,44,55,66]
print(n_list) # print seluruh items
del n_list[3] # delete 44
print(n_list)

n_list = [10,20,30]
print(n_list) # print seluruh items
n = n_list.pop()
print('n = ',n)
print('n_list =',n_list)

n_list = [11,22,33,44,55,66]
print(n_list)
n_list.remove(44)
print(n_list)


# Sequence Data Types - Iterator
list1 = [11,22,33,44] * 2
print(list1)

tup1 = (1,2,3)
print(tup1 * 2)

str2 = 'hello'
print(str2 * 3)

ran = list(range(5)) * 3
print(ran)


# Sequence Data Types - Count Method
list1 = [11,11,11,22,33,44] 
print(list1.count(11)) # mencari total angka 11 dalam list

tup1 = (11,11,11,22,33,44) 
print(tup1.count(11)) # mencari total angka 11 dalam tuple

str1 = 'hello world'
print(str1.count('l')) # mencari total huruf l dalam string

ran = range(0,5,1)
print(len(ran))
print(ran.count(2))


# Sequence Data Types - Linking
list1 = [11,22,33,44]
list2 = [55,66]
print(list1)
print(list1 + list2)

tup1 = (1,2,3)
tup2 = (4,5,6)
print(tup1 + tup2)

str1 = 'hello'
str2 = 'world'
print(str1 + str2)

print(list(range(10)) + list(range(10,20)))
print(tuple(range(10)) + tuple(range(10,20)))


# Sequence Data Types - Operators
list1 = [10,20,30,40]
print(10 in list1)
print(10 not in list1)

tup = (1,2,3,4)
print(3 in tup)

print('a' in 'abcd')
