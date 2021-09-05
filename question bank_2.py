a="w3resource"
i=0
b={}
while i<len(a):
    j=0
    count=0
    while j<len(a):
        if a[i]==a[j]:
            count+=1
        j+=1
    if a[i] not in b:
        b[a[i]]=count
    i+=1
print(b)


