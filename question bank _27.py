student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

count=0
for i in student:
    for j in i:
        if j=="id":
            count=count+i[j]
print(count)