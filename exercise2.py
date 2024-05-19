
def printdata(name,age):
    return f"your name is {name} and you are of age {age}"


n=input("Enter Name:")
a=int(input("Enter Age:"))

print(printdata(n,a))

def summ(a,b):
    add=a+b
    return add

a=int(input())
b=int(input())
print(summ(a,b))

li=[1.1,2.2,3.3,4.4,5.5,6.6]

def avg(li):
    av=sum(li)/len(li)
    return(av)

print(avg(li))

def convert(c):
    f=c*1.8+32
    return f

celcius=float(input("temp:"))
print(convert(celcius))
