d={"bijendar":45,"deepak":60,"param":20,"anjali":30,"roshni":50}
s=sorted(d.values())
i=-1
m=[]
while i>(-len(s)):
    m.append(s[i])
    i-=1
dic={}
for x in m:
    for y in d.keys():
        if d[y]==x:
            dic[y]=d[y]
print(dic)
     