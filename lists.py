# stick to the same datatype throughot the programming

# collection of data 
temparature=[25,24.04,36,-42.33,99/3]
print(temparature)
print(temparature[2])
print(temparature[4])
print(temparature[0])
print(temparature[1])

# first element starts with the zero(0)

print(len(temparature))
temparature.append(10.7)
print(temparature)
print(len(temparature))

temparature.reverse()
print(temparature)

temparature.remove(10.7)

print(temparature)
temparature.pop()
print(temparature)

new=temparature.copy()
print(new)
new.sort()
print(new)
print(new.index(24.04))

print(new.pop(1))
print(new)
new.insert(2,37)
print(new)


print(sum(temparature))
