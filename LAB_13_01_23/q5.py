import numpy
m, n = list(map(int, input().split()))
l = []
for i in range(m):
    l.append(list(map(int, input().split())))
a = numpy.array(l)
tr = numpy.transpose(a)
ft = numpy.ndarray.flatten(a)
print(tr)
print(ft)