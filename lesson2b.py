# Tuple
# a Tuple is an imutable type of a list
# to introduce a Tuple we use parenthesis()
counties = ("Nairobi", "Mpmbasa", "Nakuru", "Eldoret", "Kajiado", "Kisii")
print(counties)
print(type(counties))

# Slicing of tuple
print(counties[3:])

# accesing items of a tuple by use of indexes
print(counties[5])
# Note: Below will generate an error
# Attribute error
counties.append("Machakos")
print(counties)