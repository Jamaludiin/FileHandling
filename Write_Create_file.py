"""
You can add a text to an existing file using the following ways/options
-add additional text to an existing file this is called append "a"
-overwrite the text of an existing file using write "w"

"a" for appned: adds additional text to an existing file especially at end of the text file
"w" for write: it overwrites all the text of an exsiting file
both of these file handling modes will create a new file if the specified file name does not exist in the target path


for creating a file we use "x" for create
"x" for creating a file, it will triger and error if the file already exist.
"""

#ADD ADITIONAL TEXT TO AN EXISTING FILE USING APPEND
#first you need to open the file and use the "a" operation mode
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes.txt","at")
"""add the following text
at uinversity putra malaysia - UPM"""
var_file.write(" at uinversity putra malaysia - UPM ")
#although we use the write method to add additional text to an existing, the operation is append not overwite
#after the appned operation you must close the file, otherwise it will tiger error, 
# it is also worth noting that the chnages we made in the file will only be visible after we close the file

#NOTE: The main problem of append is that everytime you run this block of code it will keep adding the same text again and again
var_file.close()

#to read the above effect, you must open again the file with the r operation mode
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes.txt","rt")
print(var_file.read())
var_file.close()
print("=============================================================================")



#LETS APPEND A FILE THAT DOES NOT EXIST
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes1.txt","at")
var_file.write("My name is Jamal Abdullahi Nuh")
#NOTE: The main problem of append is that everytime you run this block of code it will keep adding the same text again and again
var_file.close()

#read the created file
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes1.txt","rt")
print(var_file.read())
var_file.close()
print("=============================================================================")


#LETS OVERWRITE A FILE THAT DOES NOT EXIST
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes2.txt","wt")
var_file.write("My name is Jamal Abdullahi Nuh")
#NOTE: The main problem of append is that everytime you run this block of code it will create a new file
# while every other run only overwrites the existing text in the created file and only dds the specified text
var_file.close()

#read the created file
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes2.txt","rt")
print(var_file.read())
var_file.close()
print("=============================================================================")



#CREATE NEW FILE AND DO NOT ADD ANY TEXT IN IT
#var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes3.txt","xt")
#NOTE: the problem of this is that, only creates the file at the first suceesfull run 
# while it will triger and error at the sub sequent runs, becouse the file was already created
var_file.close()

#alternative ways of creating new file that does not exist
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes4.txt","wt")
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes5.txt","at")
#NOTE: the advantage of this is that, it will creates the file if does not exist at the first suceesfull run 
# and it will not triger and error at the sub sequent runs, becouse the file will be overwrite or appends only if found existing one
var_file.close()
print("=============================================================================")



#========================ADD LIST DATA INTO A FILE=======================
var_list = [1,2,3,4,5,6,7,8,9]
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/listdata.txt","wt")
#in this case we assign the values in the list variable to the textfile.
#NOTE the write method only accepts string although the values in the list is intiger, thus we have to convert it to string
var_file.write(str(var_list))
print("List data was successfully writen in listdata.txt")
var_file.close()

#========================ADD LIST DATA INTO A FILE ONE BY ONE=======================
var_list = [1,2,3,4,5,6,7,8,9]
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/listdataOnebyOne.txt","wt")
#in this case we assign the values in the list variable to the textfile.
#NOTE the write method only accepts string although the values in the list is intiger, thus we have to convert it to string
#WE USE FOR LOOP TO INSERT LIST DATA INTO A FILE TEXT ONE BY ONE
for i in range(len(var_list)):
    var_file.write(str(var_list[i]))
    var_file.write(", ")
print("List data was successfully writen in listdataOnebyOne.txt")
var_file.close()

#========================ALTERNATIVE ADD LIST DATA INTO A FILE ONE BY ONE=======================
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/listdataOnebyOne1.txt","wt")
#in this case we assign the values in the list variable to the textfile.
#NOTE the write method only accepts string although the values in the list is intiger, thus we have to convert it to string
#WE USE FOR LOOP TO INSERT LIST DATA INTO A FILE TEXT ONE BY ONE
for i in var_list: #without using range method i variable is only stores actual values
    #this loop will not use range method and perform silimar function to range if used
    var_file.write(str(i))#i has the index values, so store the index values only staring from 0
    var_file.write(", ")
print("List data was successfully writen in listdataOnebyOne1.txt")
var_file.close()


#========================ADD LIST INDEX VALUES INTO A FILE ONE BY ONE=======================
#var_list = [1,2,3,4,5,6,7,8,9]
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/listIndexValues.txt","wt")
#in this case we assign the values in the list variable to the textfile.
#NOTE the write method only accepts string although the values in the list is intiger, thus we have to convert it to string
#WE USE FOR LOOP TO INSERT LIST DATA INTO A FILE TEXT ONE BY ONE
for i in range(0, len(var_list)):#to access index you need to store the i the range values as index, 
    #without index is only stores actual values
    #this loop will not use range method and perform silimar function to range if used
    var_file.write(str(i))#i has the index values, so store the index values only staring from 0
    var_file.write(", ")
print("List index values was successfully writen in listIndexValues.txt")
var_file.close()

#========================ADD BOTH LIST VALUE AND LIST INDEX VALUES INTO A FILE ONE BY ONE=======================
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/listValueandIndexValues.txt","wt")
#in this case we assign the values in the list variable to the textfile.
#NOTE the write method only accepts string although the values in the list is intiger, thus we have to convert it to string
#WE USE FOR LOOP TO INSERT LIST DATA INTO A FILE TEXT ONE BY ONE
for k in range(0, len(var_list)):
    #this loop will not use range method and perform silimar function to range if used
    var_file.write(" List index: ")
    var_file.write(str(k))#i has the index values, so store the index values only staring from 0
    var_file.write(" List value: ")
    var_file.write(str(var_list[k]))
    var_file.write(", ")
print("both List index and list values was successfully writen in listValueandIndexValues.txt")
var_file.close()
