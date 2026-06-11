from binarydenery import d_b
from hex import hex
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


def sort(text):
    f = ""
    f1 = ""
    for b in text:
        for i in range (16):
            for x in range (8):
                if ascii_matrix[x][i] == b:
                    b2 = d_b(i)
                    b1 = d_b(x)
                    binary = str(b1.zfill(4)) + (b2.zfill(4))
                    f += binary
                    f1 += binary + " "


    return(f,f1)



text = str(input("Enter text: "))
b,b1 = sort(text)
print(b)
print(b1)

