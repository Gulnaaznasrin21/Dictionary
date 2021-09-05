d={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for x in d.keys():
    print(x,end=" ")
print()
a=d['C1']
b=d['C2']
c=d['C3']
i=0
while i<len(a):
    print(a[i],b[i],c[i])
    print()
    i+=1