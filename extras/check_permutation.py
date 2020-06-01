def check_permutaion(a, b):
    a = sorted(a)
    b = sorted(b)
    a = ''.join(a)
    b = ''.join(b)
    return a == b

inp = [x for x in input('Enter strings: ').split(' ')]
a = str(inp[0])
b = str(inp[1])

if check_permutaion(a, b):
    print('Yes')
else:
    print('No')