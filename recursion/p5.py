def sum(N):
    if N>1:
        return N + (sum(3 * N + 1) if N%2 else sum(N // 2))
    return N
    
N = 5
print(sum(N))# prints (5 + 16 + 8 + 4 + 2 + 1)