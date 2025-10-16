# if statement
age = 18
if age < 20: # result dari age < 20 adalah True
    print('youth discount')
print ('Welcome')


# pass keyword
num = 2
if num % 2 == 0:
    print('Nomor genap')
if num % 3 == 0:
    pass


# elif adalah singkatan dari else if
score = int(input("Masukkan nilai: "))
if score >= 90:
    print("Nilai kamu A")
elif score >= 80:
    print("Nilai kamu B")
else:
    print("Nilai kamu C")


# Nested Conditional Statement
num = -100
if num < 0:
    print(num, 'adalah bilangan negatif. ')
else:
    print(num, 'adalah bukan bilangan negatif ')
    if num % 2 == 0:
        print(num, 'adalah bilangan genap')
    else:
        print(num, 'adalah bilangan ganjil')