d={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
max=0
s_max=0
t_max=0
for x in d:
    if d[x]>max:
        s_max=max
        max=d[x]
    if s_max<d[x] and d[x]<max:
        s_max=d[x]
    if d[x]<max and d[x]>t_max:
        t_max=d[x]
for y in d.keys():
    if d[y]==max:
        print(y,d[y])
    elif d[y]==s_max:
        print(y,d[y])
    elif d[y]==t_max:
        print(y,d[y])
        