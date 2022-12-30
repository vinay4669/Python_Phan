import numpy
a, b = map(int, input("Dimension of first matrix (R C) : ").split())
m = []
print("Elements of first matrix : ")
for i in range(a):
    m.append(list(map(int, input().split())))
a1 = numpy.array(m)
c, d = map(int, input("Dimension of second matrix (R C) : ").split())
m = []
print("Elements of second matrix : ")
for i in range(c):
    m.append(list(map(int, input().split())))
a2 = numpy.array(m)
print("Their product : ")
print(numpy.dot(a1, a2))