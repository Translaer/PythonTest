import array

# a = range(10,20)
a = [1,2,3,4,5,6]
b = "abcdefgh"

ar1 = array.array("b",a)
ar2 = array.array("u",b)
ar3 = array.array("b")
print(ar3)
for i in range(10):
    ar3.append(i)
print(ar3)
for i in ar3:
    print(i)