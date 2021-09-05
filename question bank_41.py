d={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
dict={}
for i in d:
    a=d[i]
    for j in a:
        height=a[0]
        weight=a[1]
        if height > 6 and weight>= 70:
            dict[i]=a
print(dict)

        