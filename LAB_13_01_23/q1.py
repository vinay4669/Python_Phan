import numpy
arr = list(map(int, input().split()))
a = numpy.array(arr, float)
print(numpy.flip(a))