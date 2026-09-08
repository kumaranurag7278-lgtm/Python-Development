numbers = [1,2,3,4,5]
new_numbers = [i+1 for i in numbers]
print(new_numbers)


#Syntax should be like :
# list = [1,2,3,4]
# new_list = [conditon for i in List]

'''   
create a new list from a range where the list items are double the values in the range
'''
num1 = [ i for i in range(1,5)]
num2 = [ j*2 for j in num1]
print(num2)

# use of if statement in list comprehenison :
# Syntex should be like :
# new_list = [ new_item for item in list if test]

names = ["Alex","Beth","caroline","Dave","Elanor","Freddie"]

short_names = [name for name in names if len(name) <= 4 ]
print(short_names)


upper_names = [name.upper() for name in names if len(name) >= 5]
print(upper_names)
