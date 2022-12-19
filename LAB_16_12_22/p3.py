l = [int(i) for i in input().split()]
out = list(filter(lambda i : i%2==0, l))
print(out)