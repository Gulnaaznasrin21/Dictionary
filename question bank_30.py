d={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}

dict={}
for i in d.keys():
    s=""
    for k in i:
        if k==" ":
            continue
        else:
            s=s+k
    for j in d.values():
        dict[s]=j
        
print(dict)