#C:\\Users\john-\GCode\KarlsRib.txt
#!/usr/bin/env python3
import os
index = True
while index:
    gcode_path = input("enter full path to file; ")
    print(gcode_path)
    try:
        reading_file = open(gcode_path,"r")

        index = False
    except FileNotFoundError:
        print("File not found")
    #except

writing_file = open("preamble.txt", "w")

next_line = reading_file.readline()

#Sepeerate Postamble

profile_end = "(Profile)"
while next_line.strip() != profile_end:
    next_line = reading_file.readline()

    writing_file.write(next_line)
writing_file.close()

# Seperate GCode

profile_end = "(finish operation: Profile)"
writing_file = open("gcode.txt", "w")
while next_line.strip() != profile_end:
    next_line = reading_file.readline()
    writing_file.write(next_line)
writing_file.close()

# seperates Postamble

writing_file = open("postamble.txt", "w")
eof = True
while eof:
    next_line = reading_file.readline()
    writing_file.write(next_line)

    if not next_line:
        eof = False
writing_file.close()

reading_file.close()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#input file
file_in = open("preamble.txt", "rt")
#output file to write the result to
file_out = open("temp.txt", "wt")
#for each line in the input file
for line in file_in:
	#read replace the string and write to output file
	file_out.write(line.replace('M5', 'M5 G19'))
#close input and output files
file_in.close()
file_out.close()

#input file
file_in = open("temp.txt", "rt")
#output file to write the result to
file_out = open("preamble.txt", "wt")
#for each line in the input file
for line in file_in:
	#read replace the string and write to output file
	file_out.write(line.replace('M3 S2000', ''))
#close input and output files
file_in.close()
file_out.close()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx



reading_file = open("gcode.txt", "r")

#reading_file = open("C:\\Users\\john-\\GCode\\KarlsRib.txt", "r")
my_dict = {
    88: 89,
    89: 90,
    90: 88,
    73: 74,
    74: 75
}

preamble= ""
#print(preamble)
new_file_content = ""
for line in reading_file:
    stripped_line = line.strip()
    #new_line = stripped_line.replace("X", "A")
    new_line = stripped_line.translate(my_dict)
    new_file_content += new_line +"\n"
reading_file.close()


writing_file = open("gcode_mod.txt", "w")
#writing_file = open("C:\\Users\\john-\\GCode\\KarlsRibFoam.txt", "w")
writing_file.write(new_file_content)
writing_file.close()

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
my_string = gcode_path
index = my_string.find('.txt')
gcode_file = my_string[:index] +"Fm"+ my_string[index:]
#print(gcode_file)


#file = input("enter file")
#print(file)
gcode_path = gcode_file
#path = "C:\\Users\\john-\\GCode\\{}"


writing_file = open(gcode_path,"w")

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Reassemble file
#writing_file = open("final.txt", "a")
file = ["preamble.txt", "gcode_mod.txt","postamble.txt"]

for index in file:

    reading_file = open(index,"r")
    eof = True
    #print(index)
    while eof:
        next_line = reading_file.readline()
        writing_file.write(next_line)
     #   print(next_line)
        if not next_line:
      #     print("End Of File")
           eof = False
    reading_file.close()
writing_file.close()

print("File " + gcode_file +" created")

# Clean up
file = ["preamble.txt", "gcode_mod.txt","postamble.txt","gcode.txt", "temp.txt"]

for index in file:
    os.remove(index)


