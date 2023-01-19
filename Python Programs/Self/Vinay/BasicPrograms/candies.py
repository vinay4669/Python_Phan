N = int(input("No. of students"))
C = int(input('No. of candies'))
A = [0]*N
print(f'Enter {N} integers')
s = 0
for i in A:
    A[i] = int(input())
    s += A[i]
print('Yes' if s<=C else 'No')