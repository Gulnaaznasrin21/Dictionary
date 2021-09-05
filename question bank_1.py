d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"d":300}
dic={}
for x in d1.keys():
    for y in d2.keys():
        if x ==y:
            dic[x]=d1[x]+d2[y]
else:
    dic[x]=d1[x]
print(dic)