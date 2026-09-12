# syntax for args
def add(*args):
    print(args[0])   #acces to each args thorugh postions
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2,3,4,5,6))

# syntax for kwargs
def calculate(**kwargs):
    # print(kwargs)
    # for key ,value in kwargs.items():
    #     print(key,value)
    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)

calculate(add=3,multiply=5) #output will be dictonary

