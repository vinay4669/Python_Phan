l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
out = list(filter(lambda i : i not in l2, l1))
out += (list(filter(lambda i : i not in l1, l2)))
print(out)