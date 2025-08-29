import os

x = ""
an = int(input("1 if local list, 2 if in different folder: "))

if an == 1:
    fileList = list(os.listdir())
    print(fileList)

if an == 2:
    x = str(input("file path: "))
    fileList = list(os.listdir(x))
    print(fileList)

c = 0
for num in fileList:
    print(fileList[c])
    full_path = os.path.join(x, fileList[c])

    if fileList[c].endswith(".py"):
        print("python file")
    else:
        if os.path.isdir(full_path):  # Check if it's a folder
            fileList1 = list(os.listdir(full_path))
            print(fileList1)
        else:
            print("not a folder, skipping")

    c += 1
