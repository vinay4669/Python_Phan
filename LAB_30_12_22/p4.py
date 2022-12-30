import numpy
a, b = map(int, input("Dimension of matrix (R C) : ").split())
m = []
print("Elements of matrix : ")
for i in range(a):
    m.append(list(map(int, input().split())))
ar = numpy.array(m)
print("Max element : ", numpy.max(ar))
print("Min element : ", numpy.min(ar))