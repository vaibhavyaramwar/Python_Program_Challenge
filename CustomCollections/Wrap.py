
from CustomCollections.ListImpl import ListImpl

l1 = ListImpl()

l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(5)
l=l1.append(6)

print("Append")
print(l)

l11 = l1.copy()
print("Copy")
print(l11)

print("Count")
print(l1.count(5))


print("Extend")
l11=l1.extend([111,222,333,444,555,666])
print(l11)

print("Extend Tuple")
l11=l1.extend((1111,2222,3333,4444,5555,6666))
print(l11)

print("Extend Set")
l11=l1.extend({11111,22222,33333,44444,55555,66666})
print(l11)


print("Index")
print("Index of 5 : ",l1.index(52222222222222222222222))

print("insert")
l11=l1.insert(777777777777777777777777777,10)
print(l11)

print("pop")
l11=l1.pop()
print(l11)

print("remove")
l11=l1.remove(777777777777777777777777777)
print(l11)

print("reverse")
print(l1.reverse())

print("sort")
print(l1.sort())

print("clear")
l11=l1.clear()
print(l11)

