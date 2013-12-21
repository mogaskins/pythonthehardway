#import the agrv module. this needs to be an array
from sys import argv

#in terminal, you need to add the program name and file name to unpack
script, filename = argv

#open your text file as text
txt = open(filename)
#Print the file name
print "Here's your file %r:" % filename
#read your file as text. Shows text in terminal
print txt.read()

#prompts you to type filename again
#assigns a variabe
#print "Type the filename again:"
#file_again = raw_input("> ")

#open file 
#txt_again = open(file_again)
#display file as text in terminal
#print txt_again.read()
