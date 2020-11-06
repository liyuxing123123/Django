#/python3

import sys, os

def Rename():
    Path = input("请输入你需要操作的目录(格式如'D:\\B_configure')：")
    filelist = os.listdir(Path)
    print(filelist)
    for files in filelist:
        Olddir = os.path.join(Path, files)
        print(files)
        if os.path.isdir(Olddir):
            continue
        filename = os.path.splitext(files)[0]
        Newdir = os.path.join(Path, filename+ '.txt')
        os.rename(Olddir, Newdir)

Rename()

