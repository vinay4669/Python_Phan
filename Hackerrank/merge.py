def merge_the_tools(string, k):
    # your code goes here
    i = 0
    n = len(string)
    while string:
        l = list(string[:n//k])
        string = string[n//k:]
        l = list(set(l))
        out = ''.join(l)
        print(out)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)