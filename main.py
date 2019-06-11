#!/usr/bin/python3

import os
import sys
from colored import fg, bg

def fileOrFolder(dataFile):

    print(dataFile + str(os.path.isdir(dataFile)))

    if (os.path.isdir(dataFile)):
        return fg('magenta')
    else:
        return fg('green')


def relative_depth(dir_path, level_offset):
    return dir_path.count(os.path.sep) - level_offset

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

def storing_folders(rootf, depthlevel, output):

    indent = " "

    levelOff = rootf.count(os.path.sep) - 1

    if output is True:
        outputFile = open("output.txt", "w")


    for ro, fol, fi in sorted(walklevel(rootf, level=depthlevel)):

        level = relative_depth(ro, levelOff)

        if level == 1:
            
            color = fileOrFolder(ro)
            print(indent + (ro + color))

            if output is True:
                outputFile.write(indent + ro + "\n")
            
        else:
            color = fileOrFolder(ro)
            print(indent*level + "| " + (os.path.basename(ro)))

            if output is True:
                outputFile.write(indent*level + "| " + (os.path.basename(ro) + "\n"))
        
        level += 1

        for f in sorted(fi):
            color = fileOrFolder(f)
            print(indent*level + "| " + os.path.basename(f) + color)

            if output is True:
                outputFile.write(indent*level + "| " + os.path.basename(f) + "\n")
        
        
    

if not len(sys.argv) > 1:
    rootf = os.getcwd()
else:
    rootf = sys.argv[1]

storing_folders(rootf, 5, True)

