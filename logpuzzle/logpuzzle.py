#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  f = open(filename, 'r')
  text = f.read()
  urls = re.findall(r'GET ([\w./~-]+puzzle[\w./~-]+) ', text)
  host = (re.search(r'_(\S+)',filename)).group(1)
  prefix = 'http://'
  full_url_lst = []
  for url in urls:
      full_url = prefix + host + url
      full_url_lst.append(full_url)
  '''Here's what the end of a file looks like: images/puzzle/p-baah-bbic.jpg'''
  def custom_sort(url):
      return (re.search(r'(\w+)-(\w+).jpg', url)).group(2)
  if (re.search(r'(\w+)-(\w+).jpg', url)).group(2):
      sorted_url_lst = sorted(full_url_lst, key=custom_sort)
  else:
      sorted_url_lst = sorted(full_url_lst)
  def rem_dupes(lst):
      i = 1
      while i < len(lst):
          if lst[i] == lst[i-1]:
              lst.remove(lst[i])
              i =-1
          i +=1
      return lst
  final_url_lst = rem_dupes(sorted_url_lst)
  return final_url_lst

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  file_prefix= '/img'
  file_suffix = 0
  if not os.path.exists(dest_dir):
      os.mkdir(dest_dir)
  abs_path = os.path.abspath(dest_dir)
  filename_lst =[]
  for url in img_urls:
      img_tag = 'img' + str(file_suffix)
      filename = abs_path + file_prefix + str(file_suffix)
      urllib.request.urlretrieve(url, filename)
      filename_lst.append(img_tag)
      print('Retrieving ' + img_tag + '...')
      file_suffix +=1
  htmlname = dest_dir + '/' + 'index.html'
  f = open(htmlname, 'w')
  print('<html><body>\n', file=f)
  for name in filename_lst:
      print('<img src ="' + name + '">', file=f, end='')
  print ('\n</body></html', file=f)
  f.close()

def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
