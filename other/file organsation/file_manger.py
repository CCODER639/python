su = 1
x = 1
print("if you want to do anything to a file not in this directory put the " \
"path in before the name of the file ")
while su == 1:
    def file_wa():
        file = str(input("file name  "))
        with open(file, "a") as f:
            f.write(str(input("text ")))
    def file_ww():
        file = str(input("remenber .txt  : "))
        with open(file, "w") as f:
            f.write(str(input("text ")))
    def create():
        file = str(input("input the file "))
        f = open(file, "x")
        print(f)
        f.close()
    def read():
        file = str(input("file name  "))
        with open(file) as f:
            print(f.read())
    def deliat():
        import os
        os.remove(str(input("file name  ")))
    def createfile():
        from pathlib import Path
        Path(input("folder name  ")).mkdir(exist_ok=True)

    def move():
        import shutil
        print("if you want to rename you just put the organal name in one and changed name in " \
        "other if in diffrent direcroty use as usray and moving and changing name gust endter the 2 one diffrent")
        shutil.move(str(input("file name  ")), str(input("destination followed by file name eg folder/file_name  ")))
    def listi():
        import os
        an = int(input("1 if local list , 2 if in diffrent folder"))
        if an == 1:
            fileList = list(os.listdir())
            print(fileList)
        if an == 2:
            fileList = list(os.listdir(str(input("file path  "))))
            print(fileList)
  
  

    while x == 1:
        print("type, 1 write, 2 writeover, 3 create, 4 read, 5 Delete," \
        "6 create folder, 7 move file/ rename , 8 list files in folder ,'stop' stop program")
        inp = int(input("input num  "))
        if inp == 1:
            file_wa()
        if inp == 2:
            file_ww()
        if inp == 3:
            create()
        if inp == 4:
            read()
        if inp == 5:
            deliat()
        if inp == 6:
            createfile()
        if inp == 20:
            x = 0
            su = 0
        if inp == 7:
            move()
        if inp == 8:
            listi()
    
