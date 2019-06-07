#!/usr/bin/python3

import os
import sys

def storing_folders(root):
    os.chdir(root)
    folders = os.listdir()
    #folders[:] = [x for x in folders if "." in x]

    print(folders)

    directory = {}
    
    for folder in folders:
        try:
            if os.path.isdir(folder):
                print(folder)
                directory.update(checking_folders(folder))
            else:
                continue
        except PermissionError:
            continue
        except FileNotFoundError:
            os.chdir("..")
    

    print(directory)

def checking_folders(root):
    prev = os.getcwd()
    os.chdir(prev + "/" + root)
    print(root)

    dirList = os.listdir()

    for item in dirList:
        if os.path.isdir(item):
            storing_folders(root)
        else:
            continue
    
    directory = {}
    print(dirList)
    directory[root] = dirList

    return directory
    #print(root)



if not len(sys.argv) > 1:
    root = os.getcwd()
else:
    root = sys.argv[1]

storing_folders(root)


