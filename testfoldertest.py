"""from pathlib import Path
my_file = Path("/home/raja/testfolder")
if my_file.is_file():
    print("hi")

import glob
import shutil

fileList = glob.glob("/home/raja/testfolder/*.csv")
for trueFile in fileList:
    shutil.move("/home/raja/testfolder/*.csv","/home/raja/testfolder1/")

"""

import shutil
import os

from filecmp import dircmp

def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print("diff_file %s found in %s and %s" % (name, dcmp.left,
               dcmp.right))
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)
 
dcmp = dircmp('/home/raja/testfolder', '/home/raja/testfolder1')
print_diff_files(dcmp)
"""
source = '/home/raja/testfolder'
dest1 = '/home/raja/testfolder1'

files = os.listdir(source)

for f in files:
    shutil.move(f, dest1)
for file in glob.glob("/home/raja/testfolder1/*.csv"):
    print(file)
"""
"""
import glob   
path = "/home/raja/testfolder1/*.csv"   
files=glob.glob(path)
for file in files:
    print (file)
    f=open(file, 'r')  
    f.readlines()   
    f.close()
"""
dest1 = '/home/raja/testfolder1'
from os import listdir
from os.path import isfile, join
import time
from datetime import datetime


onlyfiles = [f for f in listdir(dest1) if isfile(join(dest1, f))]

for file1 in onlyfiles:
    #t = time.localtime()
    #timestamp = time.strftime('%b-%d-%Y_%H%M', t)
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H:%M:%S.%f")
    file_name = file1 +"_"+timestamp
    print(file_name)
    #f=open(file1, 'r')  

