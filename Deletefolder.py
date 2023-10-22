"""
To delete a folder in python you need to import a os module
and use rmdir() method- rmdir stand for remove directory

"""

import os
#os.rmdir("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/newfolder")
#if the folder does not exist it will triger an error

#HOW TO SAFELY DELETE A FOLDER WHILE CHEKING ITS EXISTANCE
if os.path.exists("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/newfolder"):
  os.rmdir("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/newfolder")
  
else:
  print("The folder was already deleted or does not exist anymore")


  #HOW TO SAFELY DELETE A FOLDER that contain a file WHILE CHEKING ITS EXISTANCE
if os.path.exists("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/Python Case Studies"):
  os.rmdir("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/Python Case Studies")
  
else:
  print("The folder was already deleted or does not exist anymore or cannot be deleted becouse it is not empty")