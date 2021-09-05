a="MISSISSIPPI" 
i=0
b={}
while i<len(a):
    j=0
    count=0
    while j<len(a):
        if a[i]==a[j]:
            count+=1
            b[a[i]]=count
        j+=1
    i+=1
print(b)