file = open("myfile.txt")
contents = file.read()
print(contents)
file.close()    #Very important to close a file otherwise It will take extra storage

# Better way to get rid of always closing a file 
with open("myfile.txt") as file:
    contents = file.read()
    print(contents) #NO need to close the file Now

# How to write or edit the file 
#Use "w" to delete rewrite everything  and If the file does not exist it creates a new file
with open("myfile.txt",mode ="a") as file: 
    file.write("\n I like playing chess a lot ")
    