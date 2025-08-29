alpabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
wp = 0
fbi = 0
fbi1 = 0
word = "hellomynameistomandilikehorsesihavetwohorsesoneiscalledorlaithshelovescuddlesandtheotheriscalledchloebutsheissmallerabcdefghjklmnopqrstv"
for num in word:
  bi = 1000001
  x = 0
  b = word[wp]
  wp = wp + 1
  x = 0
  v1 = 0
  for num in alpabet:
    
    if alpabet[v1] == b:
      c = 0
      while c != v1  :
        bi = bi +1
        if bi == 1000002:
          bi =   1000010
      
        elif bi == 1000012:
          bi =   1000100
        elif bi == 1000102:
          bi =   1000110
        elif bi == 1000112:
          bi =   1001000
        elif bi == 1001002:
          bi =   1001010
      
        elif bi == 1001012:
          bi =   1001100
        elif bi == 1001102:
          bi =   1001110
        elif bi == 1001112:
          bi =   1010000  
        elif bi == 1010002:
          bi =   1010010
      
        elif bi == 1010012:
          bi =   1010100
        elif bi == 1010102:
          bi =   1010110
        elif bi == 1010112:
          bi =   1011000
        elif bi == 1011002:
          bi =   1011010
      
        elif bi == 1011012:
          bi =   1011100
        elif bi == 1011102:
          bi =   1011110
        c = c + 1
      bi = str(bi)
      fbi = str(fbi)
      fbi1 = str(fbi1)
      if fbi == "0" :
        fbi = bi
        fb1 = bi
      
      else:
        fbi = fbi + "--" + bi
        print(fbi)
        fbi1 = fbi1 + bi
        print(fbi1)
        
      
    v1 = v1 +1 