# Dictionary - Get Method
dic = {'a':10,'b':20,'c':30,'d':40}
a = dic.get('a') # fungsi get untuk mendapatkan value dari key a
print(a)

dic = {'a':10,'b':20,'c':30,'d':40}
b = dic.get('z',0) # tidak terdapat key z dalam dictionary dic sehingga dikembalikan value 0
print(b)


# Dictionary - Pop, PopItem, Clear Method
dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic.pop('a')) # meremove key-value pair dengan key a
print(dic)
print(dic.popitem())
dic.clear() # meremove semua value dalam dictionary dic
print(dic)


# Dictionary - Items, Keys, Values
dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic.keys()) # mengakses seluruh key yang ada dalam dictionary
print(dic.values()) # mengakses seluruh values yang ada dalam dictionary
print(dic.items()) # mengakses seluruh items yang ada dalam dictionary


# Dictionary - Update
dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic)
dic.update(a=90) # mengupdate value dari key a
print(dic)
dic.update(e=50) # karena key e belum ada maka key e dan value akan ditambahkan kedalam dictionary
print(dic)
dic.update(a=900,f=60) # mengupdate value a dan menambahkan key dan value f
print(dic)


# Dictionary - Assignment and Copying Method
x = {'a': 0, 'b': 0 , 'c': 0, 'd': 0}
y = x.copy()
print(x is y) # cek apakah kedua dictionary merupakan objek yang sama
print(x == y) # cek apakah key-value pairnya sama

x = {'a': {'python':'2.7'},'b':{'python':'3.6'}}
y = x.copy()
y['a']['python'] = '2.7.15' # merubah value dari key a - python
print(x)
print(y)


# Dictionary - From Keys Method
keys = ['a','b','c','d']
x = dict.fromkeys(keys)
print(x)

keys = ('a','b','c','d')
x = dict.fromkeys(keys)
print(x)

keys = ('a','b','c','d')
y = dict.fromkeys(keys,100)
print(y)