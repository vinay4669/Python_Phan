l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
out = list(filter(lambda i : i in l2, l1))
print(out)