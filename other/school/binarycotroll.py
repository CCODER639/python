from binarydenery import d_b
from binarydenery import b_d
def function():
    q = int(input("binary to denery 0  and denery to binary 1"))
    a = 0
    if q == 1:
        i = int(input("num"))
        a = d_b(i)
    elif q == 0:
        i = input("binary")
        a = b_d(i)
    else:
        print("enter 1 or 2")
        a = None
    print(a)

function()