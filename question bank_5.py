dic={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
s=sorted(dic.values())
d={}
for i in s:
    for j in dic.keys():
        if dic[j]==s[i]:
            d[j]=s[i]
print(d)

