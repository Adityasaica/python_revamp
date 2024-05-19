import math
li=[]
while True:
    inp=int(input())
    if(inp==0):
        break
    else:
        li.append(inp)

def avg(li):
    avg=sum(li)/len(li)
    return round(avg,2)

print(avg(li))
