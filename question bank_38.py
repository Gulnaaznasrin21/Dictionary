d={'c1': 'Red', 'c2': 'Green', 'c3': None}
dictionary={}
for i in d.keys():
    if bool(d[i])==True:
        dictionary[i]=d[i]
print(dictionary)