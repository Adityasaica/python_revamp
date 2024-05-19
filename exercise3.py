n=int(input("Enter the number of elements:"))
li=[]
for i in range(n):
    i=int(input())
    li.append(i)
def maxvalue(lis):
    maxx=li[0]
    for i in lis:
        if i>maxx:
            maxx=i
    
    return maxx

print(maxvalue(li))
