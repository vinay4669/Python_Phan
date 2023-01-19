def caught_speeding(s, bd):
    if bd==True:
        s -= 5
    print(s)
    return 0 if s<61 else 1 if s>60 and s<81 else 2

s = int(input("Enter speed : "))
bd = bool(input("Birthday or not?"))
print(caught_speeding(s, bd))