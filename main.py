#!/usr/bin/python3

import os
import sys
from colored import fg, bg
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-s', '--source', default='/home', required=False, help='The source directory from where the program will start at')
ap.add_argument('-l', '--level', default=1, help='How many levels of directories the program will go down')
ap.add_argument('-o', '--output', action='store_true', default=False, help='Print output to file')

def fileOrFolder(dataFile):

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

    if output:
        outputFile = open("output.txt", "w")

    for ro, fol, fi in sorted(walklevel(rootf, level=depthlevel)):

        level = relative_depth(ro, levelOff)

        if level == 1:
            
            color = fileOrFolder(ro)
            print(indent  + (ro + color))

            if output:
                outputFile.write(indent + ro + "\n")
            
        else:
            color = fileOrFolder(ro)
            print((indent*level) + "| " + os.path.basename(ro))

            if output:
                outputFile.write((indent*level) + "| " + (os.path.basename(ro) + "\n"))
        
        level += 1

        for f in sorted(fi):
            color = fileOrFolder(f)
            print((indent*level) + "| " + os.path.basename(f) + color)

            if output:
                outputFile.write((indent*level) + "| " + os.path.basename(f) + "\n")


arguments = vars(ap.parse_args())

source = arguments["source"]
level = int(arguments["level"])
output = arguments["output"]

print(source, level, output)
print(type(source), type(level), type(output))



storing_folders(source, level, output)

