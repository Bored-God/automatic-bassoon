a = 0
b = 1
j = int(input('enter the length of sequence: '))
print(a,b, end=' ')
for i in range(j-2):
    c = a+b
    a = b
    b = c
    print(b, end = ' ')
