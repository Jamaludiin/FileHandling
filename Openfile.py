"""
Python can handle external files by opening, creating, reading, updating and also deleting items inside the file.

The first function when handling a file is to open the file first, in this case we use the open() method.
the open() method takes two parameters, 
fileName and Mode.
the filename paramter is the first parameter to pass and it contains the file path and file name plus its extention.
this parameter has to be string and must be surrounded in a single or double quatations.
if the file name or path does not exist it will triger and error

the second parameter "Mode" has to be either one of the following string values. 
this means file can only be opned to perform for the following reasons
"r":  stands for Read: and is the Default value if the second parameter was not passed. 
      this values tells the compiler that this file should be opned for a reading purpose.
"a": stands for Append: this means the file can only be opened for appending purpose, 
     therefore it will create new file if the specified one does not exist
"w": stands for Write: this only Opens a file for writing purpose, if the file does not exist it will creates new one.
"x": stands for Create: this only be used when Creating a new file that does not exist and if it is exist it will triger an error

other parameter you can pass in the second parameter is 
In addition you can specify if the file should be handled as binary or text mode

"t" - stand for Text: this means the file should be handled as text mode and it is the Default value if you did not specify it.
"b" - stands for Binary: this means the file should be handled as Binary mode (for example image files)

simple Syntax
var = open("path and fileName","rt")
the above sytax include both parameters, note the second parameter cotains two types of file handling information including
the r for reading and t for text mode.

the following syntax also is similar to the above, since the second parameter r and t are both a default values if the second
parameter is not specified
var = open("path and fileName")
"""

var_file = open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes.txt")
#PRINT THE INFORMATION CONTAINED IN THE VAR_FILE
print(var_file)
#this has returned the file path and name and also mode such as read and text mode (encoding='UTF-8')

#PRINT THE TEXT CONTAINED IN THE TEXT FILE
print()
print(var_file.read())
#this has returned all the text written in the file

#NOTE: TWO read() METHODS CANNOT BE SEQUENCED EXAMPLE
print(var_file.read(10))
#WE PRINT 11 CHARECTERS FROM THE TEXT WHILE THE PREVIOUS READ METHOD READS ALL THE TEXT, 
#WE DID NOT CLOSED THE FILE AFTER THE FIRST OPERATION, THUS IT WILL NOT PRINT ANYTHING, EXCEPT LEAVES EMPTY SPACE

#SOLUTION IS TO CLOSE THE FILE AFTER EACH OPERATION, AND OPEN AGAIN FOR THE NEXT OPERATION
var_file.close()
#closing a file after each operation is recomended practice

#PRINT SOME OF THE TEXT CONTAINED IN THE TEXT FILE
print()
var_file = open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes.txt")
#repeat the openeing file process to start new operation
print(var_file.read(10))
#this has returned 10 charecters from the text written in the file including spaces.

