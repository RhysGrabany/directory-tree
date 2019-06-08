#!/usr/bin/python3

import os
import sys
from collections import defaultdict

def storing_folders(root):

    directory = defaultdict(dict)

    for root, folders, files in os.walk(root):

        try:
            directory[root] = {}

            for folder in folders:
                if folder in directory:
                    continue
                else:
                    directory[root][folder] = {}
                
                for f in files:
                    if f in directory[root][folder]:
                        continue
                    else:
                        directory[root][folder] = f
            
        except PermissionError:
            continue

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

print(directory)

#for k, v in directory.items():
#    print(str(k) + "\n" + str(v))



#storing_folders(root)


