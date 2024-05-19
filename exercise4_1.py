li=[]
with open("file_txt","r") as f:
    for line in f:
        li.append(int(line.strip()))
print(li)

def avg(l):
    average=sum(li)/len(li)
    return round(average,3)

print(avg(li))
