person = {'Name': 'David Doe', 'Age': 26, 'Weight' : 82}
person['Job'] = 'Data Scientist' # Key baru: masukkan nilai dari key tersebut
print(person)

person = {'Name': 'David Doe', 'Age': 26, 'Weight' : 82}
person['Age'] = 27 # Ubah value dari key yang sudah ada 'Age' 
print(person)

person = {'Name': 'David Doe', 'Age': 26, 'Weight' : 82}
del person['Age'] # Delete value dari key yang sudah ada 'Age' 
print(person)

a = {'abc':100,'def':200}
print(len(a))


# JSON - Read and Exporting
import json

data = '{"Name": "David Doe", "Age": 25, "Hobby": ["basketball"], \
"Family": {"father": "John Doe", "mother": "Marry Doe"}, "Married": true}'
json_data = json.loads(data)
print(type(json_data))
print(json_data['Name'])
print(json_data['Family'])
print(json_data['Married'])

Dictionary ={'Halo':123,'Semua':456}
json_string = json.dumps(Dictionary)
print('Result: ',json_string)
print('Tipe: ',type(json_string))