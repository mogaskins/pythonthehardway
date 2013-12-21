#import the package
from sys import argv
# need to type the file name and text file to read in
script, input_file = argv
#Create the print_all file function to print the whole file
def print_all(f):
	print f.read()
#define the rewind file function to go to the zero byte of the file	
def rewind(f):
	f.seek(0)
#f.readline reads a single line from a file
def print_a_line(line_count, f):
	print line_count, f.readline()
#sets the current file variable and opens the file
current_file = open(input_file)

print "First let's print the whole file: \n"
#prints the entire file and then makes a new line
print_all(current_file)

print "Now let's rewind, kind of like a tape."
#seek byte 0 like the function says
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file),

current_line += 1
print_a_line(current_line, current_file),

current_line += 1
print_a_line(current_line, current_file),


		
