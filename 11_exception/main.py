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
    raise TypeError("This is an error that I Made up")




# raise your own exception

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 5:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
