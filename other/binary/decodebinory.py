

key = int(input("key  :"))
wor = str(input("encrited word  :"))
x = key
y = 0
dp = 64
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
y = str(y)
key = y




wor_list = list(wor)

for i in range(len(key)):
    if key[i] == "1":
        # Flip the wor bit: '0' -> '1', '1' -> '0'
        wor_list[i] = '1' if wor_list[i] == '0' else '0'

# Join back to string
wor = ''.join(wor_list)
print("encripted word :" + wor)
