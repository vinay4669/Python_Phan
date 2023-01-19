n = int(input())
sq = 5 ** 0.5
for i in range(1, n+1):
    t = (((1+sq)**i)-((1-sq)**i))//((2**i)*sq)
    print(int(t))