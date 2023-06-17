import os
import shutil
from_dir = "C:/TestDownload"
to_dir = "C:/WhiteHat/Python/Downloaded_Files"
list_of_files = os.listdir(from_dir)
print(list_of_files)
for filename in list_of_files:
    root, ext = os.path.splitext(filename)
    if ext == "":
        continue
    if ext in [".pdf",".docx",".txt",".doc",".rtf"]:
        path1 = from_dir + "/" + filename
        path2 = to_dir + "/" + "Document_Files"
        path3 = to_dir + "/" + "Document_Files" + "/" + filename
        if os.path.exists(path2):
            print("Moving...")
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print("Moving...")
            shutil.move(path1, path3)
