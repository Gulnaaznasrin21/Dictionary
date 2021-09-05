l=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
d={}
i=0
while i<len(l):
    list=[]
    list.append(l[i][1])
    list.append(l[i][2])
    d[l[i][0]]=list
    i+=1
print(d)
        
        
