
l=[]
with open("initial","r") as f:
    for li in f:
        l.append(li.strip())

l=sorted(l)
print(l)


with open("final","w") as f1:
    for i in l:
        f1.write(i+'\n')
