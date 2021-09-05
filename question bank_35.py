dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
c=0
for x in dict.values():
    for i in x:
        c+=1
print(c)
    