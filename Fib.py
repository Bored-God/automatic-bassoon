a = 0
b = 1
c = 0
j = int(input("enter the range till which the program will run: "))
print(f'{a},{b}', end = ',')
for i in range(j-2):
  c = a+b
  a = b
  b = c
  print(b, end=",")
