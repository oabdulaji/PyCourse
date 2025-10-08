
import json

company = '''
{
  "employee": 
  [
      { "name": "John Marker", "address": "Los Angeles", "age": 50, "salary": 7500 },
      { "name": "Peter Parker", "address": "New York", "age": 25, "salary": 2750 },
      { "name": "David Loe", "address": "Seattle", "age": 33, "salary": 4150 },
      { "name": "Marry Kelvin", "address": "London", "age": 32, "salary": 4150 },
      { "name": "Kate Levi", "address": "Los Angeles", "age": 22, "email": null, "salary": 2500 }
  ]
}
'''
data = json.loads(company)
print(data)

type(data)

for kisi in data['employee']:
    # print(kisi)
    # print("/////////////")
    print(kisi['name'])
    print(kisi['salary'])


with open("employee.json", "r") as dosya:
    data = json.load(dosya)

print(data)

for kisi in data['employee'] : 
    print(kisi)

for kisi in data['employee'] : 
    print(kisi['name'])

for kisi in data['employee'] : 
    print(kisi['age'])    

for kisi in data['employee'] : 
    print(kisi['name'],kisi['salary'],kisi['address'])    


# *-*-*-*--*-*-*-*- Python To Json

data2 = json.dumps(data)
print(data2)

data2 = json.dumps(data,indent=2,sort_keys= True)
print(data2)

with open('employee-2.json','w') as dosya :
    json.dump(data , dosya)

with open('employee-2.json','w') as dosya :
    json.dump(data , dosya , indent=3)