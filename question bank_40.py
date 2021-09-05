list1=['S001', 'S002', 'S003', 'S004']
list2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
list3=[85, 98, 89, 92]
d1={}
d2={}
l=[]
i=0
while i<len(list1):
    d2[list1[i]]={list2[i]:list3[i]}
    i+=1
l.append(d2)
print(l)
