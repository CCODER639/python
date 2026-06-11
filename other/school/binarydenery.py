import math
def b_d(n):
    lenght = len(n)
    denery_num = 0 
    for x in n:
        lenght -= 1
        if x == "1":
            denery_num += 2**lenght
        
    return(denery_num)
    
def d_b(n):
    binary = ""
    while True:
        
        if (n /2).is_integer():
            binary += "0"
            print(0)
        else:
            binary += "1"
            print(1)
        n = math.floor(n/2)
        if n == 0:
            binary = binary[::-1]
            return(binary)
