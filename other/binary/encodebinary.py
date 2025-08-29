import random

key = ""
wor = "1001111101001010011001000001100100110101001001001"

for num in wor:

  ran = str(random.randint(0, 1))
  key = key + ran

wor_list = list(wor)
for i in range(len(key)):
    if key[i] == "1":
        # Flip the wor bit: '0' -> '1', '1' -> '0'
        wor_list[i] = '1' if wor_list[i] == '0' else '0'

# Join back to string
wor = ''.join(wor_list)
print("encripted word :" + wor)

x1 = str(key)
c1 = 0
d1 = 1
to1 = 0
numb1 = 0
for num in x1:
    d1 += 1
print(d1)
for num in x1:
    y1 = d1 - c1
    u1 = x1[c1]
    if c1 == 0:
      if u1 == "1":


        j1 = 1 ** 1
    if u1 == "1":
        j1 = 2 ** y1
        to1 +=  j1 /4
        
    c1 += 1
to1 = str(to1)
print("word key  :" + to1)
