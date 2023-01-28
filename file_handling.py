
####################### File handling ###################

f = open("file.txt", "w") # Writes  into the file. Overrides the content of file.
f = open("file.txt", "a") # Appends content to the file. Contents won't be overridden
f.write("Hello freaking world written !!!")  # Write contents to the file
f = open("file.txt", "r") # Read the contents of the file
print(f.read()) # Print the contents

f.close() # Closes the file
