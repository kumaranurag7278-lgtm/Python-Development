# file error
try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["key"])
except FileNotFoundError :
    file = open("a_file.txt",mode='w')
    file.write("chutiya file tho bana leta ")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:                    #if try loop works then else loop works only
    content = file.read()
    print(content)
finally:                #runs no matter what happens
    file.close()
    print("File was closed")