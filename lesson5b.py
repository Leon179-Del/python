# Functions with parameters
# Parameters -->They are values that get passed as arguments given to a function inside of parenthesis.

def greeting(name):
    print(f"{name} How are you? Hope everything is fine.")

greeting("leon")
greeting("Mary")
greeting("Joseph")

print("===============")
def message(name):
    print(f"Hello {name}. We shall be having a general meeting on date..... Please avail Yourself on date.")

message("Joy")
message("Stephen")  
# create a function that accepts parameter to add two numbers
def addition(num1, num2):
    sum = num1 + num2
    print("The sum of the number is:",sum)
addition(40, 47)
   