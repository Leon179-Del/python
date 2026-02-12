# create afunction that takes no parameters,uses arithmethic operators to calculate the area of a rectangle and prints the result
def area():
    length = 20
    width = 50
    area = length*width
    print(area)


print("==================")
# create a function that accepts two parameters,returns their sum,product and difference 
def arithmetic_operations(num1,num2):
    sum=num1+num2
    product=num1*num2
    division=num1/num2
    difference=num1-num2
    return sum,product,division,difference

result=arithmetic_operations(10,5)
print("The sum is:",result[0])
print("The difference is:",result[3])
print("The product is:",result[1])
print("This is the Quotient:",result[2])

print("==================")

# a function that accepts a number(uses input functions),checks weather the number is positive negative or zero and prints the results using if elif else
def check_number():
 

 num=int(input("Enter your number"))
 if num>0:
    print("The number is positive")
 elif num < 0:
    print("The number is negative")
 else:
    print("zero")
check_number()

print("==================")

# a function that accepts a number ,uses a while loop and calculates the square of numbers from 1 to that number
def square_of_numbers(n):
   i=1
   while i<=n:
      square=i**2 
      print("The squre of ",i,"is:",square)
      i+=1
n=int(input("Enter your number:"))  
square_of_numbers(n)


print("==================")

# a function that accepts a number n ,uses a for loop and calculates the sum from 1 to n
def sum_of_number(n):
   sum=0
   for i in range(1,n+1):
      sum+=1
   print("The sum of the numbers from 1 to",n,"is",sum)
n = int(input("Enter a number:"))
sum_of_number(n)
      

   