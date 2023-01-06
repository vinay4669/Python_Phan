f = open("sample.txt", 'r')
l = f.readlines()
for i in l:
    print('#'.join(i.split()))
f.close()