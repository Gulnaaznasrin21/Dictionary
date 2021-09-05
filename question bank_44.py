d={'science': [88, 89, 62, 95], 'language': [77, 78, 84, 80]}
a=d["science"]
b=d["language"]
l=[]
i=0
while i<len(a):
    dict={}
    dict["science"]=a[i]
    dict["language"]=b[i]
    l.append(dict)
    i+=1
print(l)