"""
To delete an existing file or folder we need to import OS module which allows us to perform some operating system 
related operations
"""

import os

#DELETE AN EXISTING FILE USING REMOVE METHOD
# #NOTE: in this delete operation you do not need to open a file using open() method, instead use remove() method 
#os.remove("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes4.txt")
#NOTE: this deletes the specified file att the first successfull run, while the subsequent runs trigers and error 
# becouse the file was already deleted from the system

#the following are error proof to delete a file by checking its existence before it is removed
if os.path.exists("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes4.txt"):
  os.remove("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes4.txt")
else:
  print("The file was deleted and does not exist anymore")


#HOW TO SAFELY CREATE NEW FILE WHILE CHEKING IF ITS EXISTANCE
if os.path.exists("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes6.txt"):
   print("The file was already exist and cannot be created again")
else:
  var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes6.txt","x")
  var_file.close()
 