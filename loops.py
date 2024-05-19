# For loops
for i in range(10):
    print("hello "+str(i))

# indentaition was more important
print('test')
# only indented codes were runned in the loop

# two kinds of loops
# for loops and while loops

i=1
while(i<10):

    print(f"hello {i}")
    i+=1
# we have the same behaviour
# we can give the conditional statement 


# while loops were the condition oriented
li=range(100)
for i in li:
    print(i)
l=[1,2,3,-4,-2]
for i in l:
    if(i<0):
        print("negative")
    elif i>0:
        print("Positive")
    else:
        print("Zero")
