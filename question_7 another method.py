d=[

     {"first":"1"}, 

     {"second": "2"}, 

     {"third": "1"}, 

     {"four": "5"}, 

     {"five":"5"}, 

     {"six":"9"},

     {"seven":"7"}

]
i=0
a=[]
while i<len(d):
    k=d[i]
    for x in k:
        if k[x] not in a:
            a.append(k[x])
    i+=1
print(a)
