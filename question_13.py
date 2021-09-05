my_dict={"a":50,"b":58,"c":56,"d":40,"e":100}
max=0
s_max=0
t_max=0
b={}
for x in my_dict:
    if my_dict[x]>max:
        s_max=max
        max=my_dict[x]
    if s_max<my_dict[x] and my_dict[x]<max:
        s_max=my_dict[x]
    if my_dict[x]<max and my_dict[x]>t_max:
        t_max=my_dict[x]
    b["e"]=max
    b["b"]=s_max
    b["c"]=t_max
b.update()
print(b)

    
    