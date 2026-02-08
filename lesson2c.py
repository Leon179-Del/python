# A Dictionary is a data type that stores data in terms of key - value pair.
# it is introduced by the use of curly braces{}
# The values stored inside of a dictionary can be of any data type.
# To acces the values in a dictionary we use the keys


phonebook = {
    "Benson" : "2546768767",
    "Mary" : "2546766565",
    "Stephen":"25476876876"
}

# showing the entire dictionary
print(phonebook)
print(type(phonebook))

# print out bensons number
print(phonebook["Benson"])

print('====================')

player = {
    "name" : "Messi",
    "age" : 40,
    "teams" : ["PSG", "Barcelona", "Argentina"]
}
print(player[1])
