for i in range(3):
    print('Welcome to everyone!!')


# sequence object iteration
numbers = [11, 22, 33, 44, 55, 66]
for n in numbers:
    print('n =',n)


# break
st = 'Programming' # fungsi akan di eksekusi selama huruf adalah konsonan
for ch in st:
    if ch in ['a','e','i','o','u']:
        break # stop loop jika menemukan huruf vokal
    print(ch)
print('The end')


# continue
st = 'Programming' # fungsi akan di eksekusi selama huruf adalah konsonan
for ch in st:
    if ch in ['a','e','i','o','u']:
        continue # skip eksekusi kode dibawah jika huruf vokal
    print(ch)
print('The end')