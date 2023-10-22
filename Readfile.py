#to read a file, you need to open first using the open method, while passing its parameters such as path+name and mode(e.g. r+t)

var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes.txt")
#this is also similar like this
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes.txt","r")
#or even like this 
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes.txt","rt")
#all obove declarations are same

#use the read() to read all the content found in the text file
print(var_file.read())
#although all the text was read by the above statement, if you specify again the same satatemnt, nothing will be printed
#except a new empty space
print(var_file.read())
print("=============================================================================")
var_file.close()

#PRINT SOME CHARECTERS IN THE TEXT E.G. FIRST 8 CHARECTERS
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes.txt","rt")
print()
#the following reads the first eight charecters found in the text file
print(var_file.read(8))
#read another eight charecters from text file using same statement
print(var_file.read(8))
print("=============================================================================")
var_file.close()

#PRINT THE FIRST LINE OF THE TEXT IN THE FILE
#to read a line we use readline method
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes.txt","rt")
print()
print(var_file.readline())
#this reads only the first line found in the text file
#if you want aonther line (second line) you need to write another similar statement like this
print(var_file.readline())
#Note after each print, there is a new line inserted

#what will happen if you specify many readline statements as follows
#nothing will be printed after all the lines found in the text file was prnted, except new empty lines
print(var_file.readline())
print(var_file.readline())
print(var_file.readline())
print(var_file.readline())
print("=============================================================================")
var_file.close()

#ANOTHER ALTERNATIVE WAYS TO READ FILE CONTENTS IS BY USING LOOPS
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes.txt","rt")
print()
#this examples prints all the lines in the text file one by one
for i in var_file:
    print(i)
    #evey execution it will create new line
print("=============================================================================")
var_file.close()

#PRINT THE NUMBER OF LINES CONTAIN IN A TEXT FILE
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes.txt","rt")
print()
num_line =0
for i in var_file:
    num_line+=1
    #evey execution it will create new line
print("the number of lines contain in the text file is ",num_line)
print("=============================================================================")
var_file.close()

#PRINT ALL THE CHARECTERS CONTAIN IN A TEXT FILE ONE BY ONE
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes.txt","rt")
print()
for i in var_file.read():
    print(i)
    #evey execution it will create new line
print("=============================================================================")
var_file.close()


#PRINT THE NUMBER OF charecters CONTAIN IN A TEXT FILE
var_file=open("/Users/jamalabdullahi/Python Tutorial/Python 101/File Handling/mynotes.txt","rt")
print()
num_line =0
for i in var_file.read():
    num_line+=1
    #evey execution it will create new line
print("the number of charecters contain in the text file is ",num_line)
print("=============================================================================")
var_file.close()


