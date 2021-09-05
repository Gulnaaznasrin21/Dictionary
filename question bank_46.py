l=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
l1=[]
l2=[]
for i in l:
    d={}
    d1={}
    for j in i.keys():
        d[j]=int(i[j])
        d1[j]=float(i[j])
        if d not in l1 or d1 not in l2:
            l1.append(d)
            l2.append(d1)
print(l1)
print(l2)