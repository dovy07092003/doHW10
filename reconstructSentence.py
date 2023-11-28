# File name: reconstructSentence.py
# This program will read from two text file and
# combine their contents to produce the complete output.
# The output will be exported to output.txt file
# To run: python3 reconstructSentence.py input1.txt input2.txt

import sys # Import the module to open the command line argument file

f1 = open(sys.argv[1]) # Open file 1
f2 = open(sys.argv[2]) # Open file 2
fo = open("output.txt","w") # Open file to write the result

f1_lines = f1.readlines() # Read input files
f2_lines = f2.readlines()

for l1 in f1_lines:
    f1_list = l1.split()

for l2 in f2_lines:
    f2_list = l2.split()

f1_length = len(f1_list) # Get the length of input list
f2_length = len(f2_list)

print("# of elements in list 1:", f1_length)
print("list 1 is: ", f1_list)
print("# of elements in list 2:", f2_length)
print("list 2 is: ", f2_list)


if f1_length > f2_length:
    length = f1_length
    diff = f1_length - f2_length

else:
    length = f2_length

print("The longest string contains", length,"elements")

i = 0
out_old = [] # Create an array for output
while i < length:
        out_new = ([f1_list[f1_length - 1 - i]],[f2_list[f2_length - 2 - i]]) # f2_length < f1_length
        out_old.extend(out_new)
        out_new = out_old # Swap
        i = i+1  
print(out_new)
fo.write(str(out_new)) # Convert to string to print out in the output.txt
