a= [
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
i=0
b={}

while i<len(a):
    b.update(a[i])
    i+=1
d=[]
for x in b:
    if b[x] not in d:
        d.append(b[x])
print(d)