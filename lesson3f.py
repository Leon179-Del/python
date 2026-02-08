# create a python program that is able to determine weather a number entered is an even number or an odd number.
# number = int(input("Enter your number here"))
# if number % 2  == 0:
#     print("The number is even")
# else:
#     print("Odd")    
 
#  Create a python program that is able to determine weather a person can donate blood based on age and weight of a person..If the weight is greater than 50 kg and age is above 18 and weight above 50 kg else not possible
age = int(input("Enter your ange"))
weight = float(input("Enter your weight"))

if age >= 18 and weight > 50:
    print("Can donate")
else:
    print("not possible")