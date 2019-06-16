#!/usr/bin/python3

import os
import sys
from termcolor import colored, cprint
#from colored import fg, bg
import argparse

# Commandline input arguments
ap = argparse.ArgumentParser()
ap.add_argument('-s', '--source', default='/home', required=False, help='The source directory from where the program will start at')
ap.add_argument('-l', '--level', default=1, help='How many levels of directories the program will go down')
ap.add_argument('-o', '--output', action='store_true', default=False, help='Print output to file')
ap.add_argument('-foc', '--foldercolor', default='magenta', help='Change print color of the folders')
ap.add_argument('-fic', '--filecolor', default='green', help='Change print color of the files')

# Return true if file, else false
def fileOrFolder(path, args):

    if (os.path.isdir(path)):
        colour = args['foldercolor']
    else:
        colour = args['filecolor']

    return colour

# The relative depth of an inputted path
def relative_depth(dir_path, level_offset):
    return dir_path.count(os.path.sep) - level_offset

# A method I found on SO that comes with a depth limiter
def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

# Method used to loop through the folders
def printToTerminal(args):

    # Store the values
    source = args["source"]
    level = int(args["level"])
    output = args["output"]


    indent = " "

    levelOff = source.count(os.path.sep) - 1

    if output:
        outputFile = open("output.txt", "w")

    for ro, fol, fi in sorted(walklevel(source, level=level)):

        level = relative_depth(ro, levelOff)

        if level == 1:

            color = fileOrFolder(ro, args)

            text = colored((indent + ro), color)
            print(text)

            if output:
                outputFile.write(indent + ro + "\n")
            
        else:
            color = fileOrFolder(ro, args)

            text = colored(((indent*level) + "| " + (os.path.basename(ro))), color)
            print(text)

            if output:
                outputFile.write((indent*level) + "| " + (os.path.basename(ro) + "\n"))

        level += 1

        for f in sorted(fi):
            color = fileOrFolder(f, args)

            text = colored(((indent*level) + "| " + os.path.basename(f)), color)
            print(text)

            if output:
                outputFile.write((indent*level) + "| " + os.path.basename(f) + "\n")

# Store the arguments into a dictionary
arguments = vars(ap.parse_args())

# Start the method
printToTerminal(arguments)

