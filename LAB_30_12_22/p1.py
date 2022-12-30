import numpy as np
n = int(input("Enter the size of matrix : "))
l = []
print("Enter the matrix : ")
for i in range(n):
    l.append(list(map(int, input().split())))
a = np.array(l)
print("Transpose of the matrix : \n", a.transpose())
