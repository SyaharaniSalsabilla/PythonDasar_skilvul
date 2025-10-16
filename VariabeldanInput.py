# identifier variabel
lebar = 10 # identifier untuk membedakan lebar persegi panjang dari data lain
tinggi = 5 # identifier untuk membedakan tinggi persegi panjang dari data lain
luas_kotak = lebar * tinggi
print('luas area kotak = ', luas_kotak)


# Variable Assignment:

# Simultaneous Assignment
x,y = 100,200
result = x + y
print(result)

# Multiple Assignment
num1 = num2 = num3 = 200
print(num1,num2,num3)

# Compound Assignment Operators
num = 200
num += 100
print(num)
num -= 100
print(num)
num *= 20
print(num)
num /= 2
print(num)


# operator aritmatika
berat = float(input("Masukkan berat anda dalam kg: "))
tinggi = float(input("Masukkan tinggi anda dalam m: "))
bmi = (berat/(tinggi ** 2))
print("BMI Anda =",bmi)


# Input Function
Name = input ("Enter Name: ")
print("Hello",Name)

#Input to Integers
a = int(input("Masukkan integer pertama:" ))
b = int(input("Masukkan integer kedua:" ))
s = a + b
print("Total dari",a,"dan",b,"adalah",s)