

#C:\\Users\john-\GCode\KarlsRib.txt
#!/usr/bin/env python3
preamble = " "
import re
index = True
while index:
    gcode_path = input("enter full path to file; ")

    print(gcode_path)
    try:
        #reading_file = open(gcode_path,"r")
        with open(gcode_path, 'r') as post_file:
            gcode_file = post_file.read()

            ind_pre = gcode_file.find("(Profile)")
            ind_post = gcode_file.find("(begin postamble)")
            ind_end = gcode_file.rindex("M2")
            ind_end = ind_end + 2

        # writing_file = open("preamble.txt", "w")

        # Split the string into preamble , gcode and postamble
            if len(gcode_file) > ind_end :
                preamble = gcode_file[0: ind_pre:]
                code = gcode_file[ind_pre : ind_post : ]
                post = gcode_file[ind_post : ind_end :]

        index = False
    except FileNotFoundError:
        print("File not found")

# Add G19

index = preamble.find('M5')
preamble = preamble[:index] + "G19 " + preamble[index:]

# Looking for M3 and speed using wildcard search

# initializing Substring
sub_str = 'M3 S....'
# Wildcard Substring search
# Using re.finditer()
temp = re.compile(sub_str)
res = temp.search(preamble)
try:
# printing result
    print("The substring match is : " + str(res.group(0)))
    word = str(res.group(0))

    preamble = preamble.replace(word," ")

    print(preamble)
except AttributeError: # catch exceptions if speed not set
    preamble = preamble.replace('M3', " ")

my_dict = {
    88: 89,
    89: 90,
    90: 88,
    73: 74,
    74: 75
}
code = code.translate(my_dict)

#Reassemble file

fin_file = preamble + code + post

print(fin_file)

#Add fm to file name to create new file

my_string = gcode_path
index = gcode_path.find('.txt')
gcode_file = gcode_path[:index] +"Fm"+ gcode_path[index:]

#Save file
with open(gcode_file, "w") as file:
    file.write(fin_file)
print("Operation Complete the new file is  " +  gcode_file)

