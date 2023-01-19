def cigar_party(nc, wk):
    if nc>=40 and nc<=60 and not wk:
        return True
    elif nc>=40 and wk:
        return True
    return False

nc = int(input("Enter no. of cigars"))
wk = bool(input("Is it weekend?"))
print(cigar_party(nc, wk))