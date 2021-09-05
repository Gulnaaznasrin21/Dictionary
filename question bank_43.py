d=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
n={}

for i in d:
    if i[0] in n:
        num=[]
        for j in n.keys():
            if i[0]==j:
                num.append(n[j])
                num.append(i[1])
                n[i[0]]=num
    else:
        n[i[0]]=i[1]
print(n)