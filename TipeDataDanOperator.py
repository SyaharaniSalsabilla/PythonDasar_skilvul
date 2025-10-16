print('I' + 'Love' + 'Python!')  # String dapat ditambahkan ke string.
print('Python' * 10)  # Menghasilkan string 'Python' diulang sebanyak 10 kali
print('*' * 50)  # Menghasilkan string '*' diulang sebanyak 50 kali
print(str(100) * 10)  # String '100' diulang sebanyak 10 kali


# String Built-In Function:

# split()
teks = "halo, nama saya, budi"
x = teks.split(", ")
print(x)

# islower()
a = "HaLo"
b = "halo"
print(a.islower())
print(b.islower())

# count()
tekss = "Halo semuanya, disini saya bersama dengan budi semuanya"
y = tekss.count("semuanya")
print(y)


# Operator Basic:
print(100 + 20)  # Temukan penambahan nilai numerik 100 dan 20
print(100 * 20)  # Temukan perkalian nilai numerik 100 dan 20
print(100 - 20)  # Temukan pengurangan nilai numerik 100 dan 20
print(100 / 20)  # Bagi nilai numerik 100 dan 20
print(100 // 20)  # Bagilah nilai numerik 100 dengan 20 dan temukan hasil bagi
print(100 % 20)  # Bagilah nilai numerik 100 dengan 20 dan temukan sisa bagi
print(10 + 20 * 30)  # Perkalian dihitung terlebih dahulu.
print((10 + 2) * 30)  # Operator dalam kurung dihitung terlebih dahulu.


# Built-in Function

# integer:
c = int("12")
d = int(12.5)
print(c)
print(d)

# float:
e = pow(3, 3) # 3 pangkat 3
f = pow(3, -3) # 3 pangkat -3
print(e)
print(f)

# string:
g = str(12)
h = str(12.5)
print(type(g))
print(type(h))