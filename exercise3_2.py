li=[]
for i in range(5):
    inp=int(input())
    li.append(inp)


def avg(li):
    avg=sum(li)/len(li)
    return avg

print(avg(li))
