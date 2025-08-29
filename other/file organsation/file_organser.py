from pathlib import Path
import os
import shutil
# Create a single folder
#Path("my_folder").mkdir(exist_ok=True)

# Create nested folders
#Path("parent_folder/child_folder").mkdir(parents=True, exist_ok=True)





# Move file.txt into the folder "my_folder"
#shutil.move("file.txt", "my_folder/file.txt")




fileList = list(os.listdir())
print(fileList)
c = 0
for num in fileList:
    print(fileList[c])
    
    filename = str(fileList[c])
    c1 = 0
    fold = 0
    for num in filename:
        if filename[c1] == ".":
            fold = 1
            print("hit")
        c1 += 1
    if fold == 0:
        print("folder")
        fileList2 = list(os.listdir(filename))
        print(list(fileList2))
   
    if filename.endswith(".py"):
        print("python file")
        shutil.move(filename, "my_folder/" + filename)

    

    c += 1



