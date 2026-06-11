ascii_matrix = [
    # Rows 0-7, each containing 16 elements (Columns 0-15)
    ["NUL", "SOH", "STX", "ETX", "EOT", "ENQ", "ACK", "BEL", "BS",  "HT",  "LF",  "VT",  "FF",  "CR",  "SO",  "SI"],  # Row 0
    ["DLE", "DC1", "DC2", "DC3", "DC4", "NAK", "SYN", "ETB", "CAN", "EM",  "SUB", "ESC", "FS",  "GS",  "RS",  "US"],  # Row 1
    [" ", "!",   '"',   "#",   "$",   "%",   "&",   "'",   "(",   ")",   "*",   "+",   ",",   "-",   ".",   "/"],  # Row 2
    ["0",   "1",   "2",   "3",   "4",   "5",   "6",   "7",   "8",   "9",   ":",   ";",   "<",   "=",   ">",   "?"],  # Row 3
    ["@",   "A",   "B",   "C",   "D",   "E",   "F",   "G",   "H",   "I",   "J",   "K",   "L",   "M",   "N",   "O"],  # Row 4
    ["P",   "Q",   "R",   "S",   "T",   "U",   "V",   "W",   "X",   "Y",   "Z",   "[",   "\\",  "]",   "^",   "_"],  # Row 5
    ["`",   "a",   "b",   "c",   "d",   "e",   "f",   "g",   "h",   "i",   "j",   "k",   "l",   "m",   "n",   "o"],  # Row 6
    ["p",   "q",   "r",   "s",   "t",   "u",   "v",   "w",   "x",   "y",   "z",   "{",   "|",   "}",   "~",   "DEL"] # Row 7
]
from binarydenery import b_d

binary = ""
def bTT(b):
    asciitext = ""
    d = bTd(b)
    lenght = len(d)
    x = 0
    for i in range (lenght//4):
        row = int(d[x:x+2])
        collom = int(d[x+3:x+4])
        t = ascii_matrix[row][collom]
        x += 4
        asciitext += t

    return(asciitext)



def bTd(b):
    lenght = len(b)
    d = ""
    x = 0
    for l in range (lenght//4):
        bi = b[x:x+4]
        de = str(b_d(bi))
        de = de.zfill(2)
        d += de
        x += 4
    return(d)
    
    
text = bTT(str(input("input 8bit ascii :")))
print(text)
