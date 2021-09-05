d={"bijendar":45,"deepak":60,"param":20,"anjali":30,"roshni":50}
s=sorted(d.values())
dic={}
for x in s:
    for j in d.keys():
        if d[j]==x:
            dic[j]=d[j]
            break
print(dic)