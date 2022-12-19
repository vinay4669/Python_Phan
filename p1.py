def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        print(f'\t{i}\t{oct(i)[2:]}\t{hex(i)[2:]}\t{bin(i)[2:]}\t')

print_formatted(17)