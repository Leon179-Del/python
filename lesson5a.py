# Python functions
# They are a block of code / statements that perfom a given task /action.They can be reused throuout the program to perfom different tasks
# Fenctions are defined using the def keyword .(define)
# We have two main types of functions i.e;
# 1. In-built functions-->They come preinstalled with the interprater i.e; print() ,pop(),range(),append(), e.t.c
# 2. User defined functions => They are created by a programmer to solve a given task.
# To define a function you need to give it a name followed by parenthesis.
# For the functions, it is usually indented and to invoke a function we use the function name.


def greetings():
    print("Hello how are you")

# below we call a function by its name
greetings()

print("==================")
# Addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the number is:",sum)
addition()

# create a function that is able to multiply three values
def multiplication():
    num1 = 10
    num2 = 60
    num3 = 5
    product = num1 * num2  * num3
    print("The product of the number is:",product)

multiplication()  

print("==================")
# Below is a division function.
def division():
    number1 = int(input("Enter the first number:"))
    number2 = int(input("Enter the second number"))
    Quotient = number1 / number2
    print("The number is:",Quotient)
    print("--------")
    
for function in range(5):
        division() 
               

    

 