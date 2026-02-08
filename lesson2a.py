# python lists
# A list is introduced by the use of the square brackets[]
# The items of a list are stored inside of indexes; In programing we start counting from index Zero(0).
cars = ["bmw", "benz","toyota", "subaru", "dodge", "probox", "Range"]
print(cars)
print(type(cars))

# Accessing items of a list
print(cars[2])
print("The car on index two is:",cars[2])
# Listing slicing -This is creating a list from a given bigger list
print(cars[4:])

# printing from index zero to index three
print(cars[:4])

# printing from certain point
print(cars[2:5])

# List - mutability
# We use the function oppend to add an item at the end of a list
cars.append("mclaren")
print(cars)

# we use the pop function to remove an item at the end of the list
cars.pop()
print(cars)

# we can use an index to add items to a list
cars[5] = "pajero"
print(cars)

# we can use the sort function to sort out items in alphabetical order
cars.sort()
print(cars)
