d={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
dict={}
for i in d.keys():
    if type(d[i])==list:
        dict[i]=[]
print(dict)