people = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 22, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
]

for i in people:
    if i['age'] > 25:
        print(i['name'])

sorted_d = sorted(people, key= lambda people : people['age'], reverse =True)  
print(sorted_d)