color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
l=[]
for (i,x) in enumerate(color):
    if i not in (0,4,5):
        l.append(color[i])
print(l)
