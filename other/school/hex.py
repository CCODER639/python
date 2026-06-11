import math
abc = "ABCDEF"
def hex(n):
    if n/16 >= 1:
        h1 = math.floor(n/16)
        h2 = n - (h1*16)
        print(h1,h2)
        h1 = hex1(h1)
        h2 = hex1(h2)
        f = str(h1) + str(h2)
        return(f)
    else:
        x = hex1(n)
        return(x)


        


def hex1(n):
    for x in range (5):
        if n <10:
            return(str(n))
        if x+10 == n:
            return(abc[x])
        
