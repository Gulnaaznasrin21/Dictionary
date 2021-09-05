# d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# dict={}
# for i in d.keys():
#     b=[]
#     for j  in d[i]:
#         if j%2==0:
#             b.append(j)
#     dict[i]=b
# print(dict)




d={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
dict={}
for i in d.keys():
    b=[]
    for j  in d[i]:
        if j%2==0:
            b.append(j)
    dict[i]=b
print(dict)
