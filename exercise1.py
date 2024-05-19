# ihis code will solve the exercise1

# First
name=input("Enter the Name:")
age=int(input("Enter the Age:"))
print(name,age)
print(f"the name is {name} age is {age}")

# Second
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print(f"the sum of two numbers is {num1+num2}")

# Third
floating=[3.4,5.4,6.7,2.3]
print(sum(floating))

summ=0
for i in floating:
    summ+=i
print(summ)
# average was

avg=sum(floating)/len(floating)
print(avg)
