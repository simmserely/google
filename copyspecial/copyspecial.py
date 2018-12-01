#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
a file name is special if something has two under bars followed by a word and
another two under bars. e.g. > zz__something__.jpg

Part A
takes a directory and finds all the special files in it and lists them by their
absolute path (i.e wherever that file is so it doesn't depend on the current directory)

Part B
finds all the special files and creates a directory w/ a name. if the directory doesn't
exist, creates that directory and copies all the special files to it

Part C
finds all the special files and invokes the zip utility to zip all the files up"""


# +++your code here+++
# Write functions and modify main() to call them
def sp_file_printer(adir):
    if adir == '.':
        core_dir = adir
    else:
        core_dir = (re.search(r'[\w.]+\/',adir)).group()
    files_lst = os.listdir(core_dir)
    files_list_str = ' '.join(files_lst)
    sp_files_list = re.findall(r'\w+__\w+__\S+',files_list_str)
    abspath_sp_files_lst = []
    for afile in sp_files_list:
        file_path = os.path.join(core_dir, afile)
        abs_file_path = os.path.abspath(file_path)
        abspath_sp_files_lst.append(abs_file_path)
    return abspath_sp_files_lst

def sp_dir_printer(adir):
    src_path_list = sp_file_printer(adir)
    if not os.path.exists(adir):
        os.mkdir(adir)
    dst_path = os.path.abspath(adir)
    for src in src_path_list:
        shutil.copy(src, dst_path)
    sys.exit(1)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  tozip = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0]
  elif args[0] == '--tozip':
    tozip = args[1]
    del args[0]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  sp_dir_printer(todir)

if __name__ == "__main__":
  main()
