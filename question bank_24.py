a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
d={}
amount1=0
amount2=0
i=0
while i<len(a):
    if a[i]["item"]=="item1":
        amount1=amount1+a[i]["amount"]
        d["item1"]=amount1
    elif a[i]["item"]=="item2":
        amount2=amount2+a[i]["amount"]
        d["item2"]=amount2
    i+=1
print(d)      