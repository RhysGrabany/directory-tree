#!/usr/bin/python3

import os
import sys
from collections import defaultdict
import numpy as np

def storing_folders(rootf):

    indent = " "

    level = 1
    for ro, fol, fi in sorted(os.walk(rootf)):
        if level == 1:
            print(indent + "." + ro + "} .")
        else:
            print(indent*level + " " + str(level) + os.path.basename(ro))
        
        level += 1

        for f in sorted(fi):
            print(indent*level + " " + str(level) + f)
    
                
                
     





    
    return directory



# def walklevel(some_dir, level):
#     dirDict = {}

#     some_dir = some_dir.rstrip(os.path.sep)
#     assert os.path.isdir(some_dir)
#     num_sep = some_dir.count(os.path.sep)
#     for root, dirs, files in os.walk(some_dir):
#         yield root, dirs, files

#     num_sep_this = root.count(os.path.sep)
#     if num_sep + level <= num_sep_this:
#         del dirs[:]
    

if not len(sys.argv) > 1:
    rootf = os.getcwd()
else:
    rootf = sys.argv[1]

directory = storing_folders(rootf)

'''for root, folders, files in os.walk(rootf):
    print("Root: " + root)
    for folder in folders:
        print("Folder: " + folder)
        for f in files:
            print("File: " + f + "\n")'''

#print(directory)

for k1, v1 in directory.items():
    print(k1)
    for k2, v2 in directory[k1].items():
        print(v1, k2, v2)
        



#storing_folders(root)


