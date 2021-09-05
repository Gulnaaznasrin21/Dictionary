dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
b=[]
count=0
for x in dict:
    b.append(dict[x])
i=0
while i<len(b):
        count=count+len(b[i])
        i+=1
print("count of elements of keys which are in list is",count)
    