from pathlib import Path
import os
import shutil
end_l = [".py",".txt",".png",".jpg",".exe",".stl"]
c = 0
file_l =  list(os.listdir())
for num in file_l:
    file = file_l[c]
    print(file)
    c1 = 0
    for num in end_l:
        if file.endswith(end_l[c1]):
          Path(end_l[c1]).mkdir(exist_ok=True)
          shutil.move(file, end_l[c1] + "/" + file)
        c1 += 1
    c += 1
    