# Dictionary - Get Method
dic = {'a':10,'b':20,'c':30,'d':40}
a = dic.get('a') # fungsi get untuk mendapatkan value dari key a
print(a)

dic = {'a':10,'b':20,'c':30,'d':40}
b = dic.get('z',0) # tidak terdapat key z dalam dictionary dic sehingga dikembalikan value 0
print(b)