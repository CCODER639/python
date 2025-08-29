x = int(input("num : "))
y = 0
dp = 100
v = 2** dp
v1 = 10 ** (dp-1)
a = 0
while a != dp:
    if x >= v:
        y = y + v1
        x = x -v
    v = v // 2
    v1 = v1 // 10
    a = a +1
y = int(y)
print(y)












