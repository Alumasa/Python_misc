# Use a file handler to open a file for writing
write_file = open("text.txt", "w")

# Open the file for reading
read_file = open("text.txt", "r")

# Write to the file then close it
write_file.write("Not closing files is VERY BAD. \nClosing files is very important!!!")
write_file.close()


#read from the file and then close it
print(read_file.read())
read_file.close()

#Using with...as to automatocally close the file:
with open("text.txt", "w") as my_file:
    my_file.write("This is a new concept to me. \nI enjoy learning it!")

    if my_file.closed == False:
        my_file.close()

print(my_file.closed)

