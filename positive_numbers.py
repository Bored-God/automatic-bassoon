a = list(input().strip('[]').split(','))
for i in range(len(a)-1,-1,-1):
    if int(a[i]) < 0:
        a.pop(i)
        i = 0
    else:
        a[i] = int(a[i])
print(a)