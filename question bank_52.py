d={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
max=0
s_max=0
for i in d.keys():
    if d[i]>max:
        max=d[i]
maximum=[]
for j in d.keys():
    if d[j]==max:
        maximum.append(j)
        print(maximum)