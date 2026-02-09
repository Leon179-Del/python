# A for loop can also be used to iterate through a lidt , tuple , string or even a dictionary..

name = "Leon"

for letter in name:
    if letter == "o":
        print("The letter is o")
    else:
        print(letter)

print('===========')
# Below is a list of counties
counties = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu"]

print(counties)

for county in counties:
    print(county)


print('===========')
for county in counties:

 if "Mombasa" in counties:
    print("county found")
    break
else:
    print("county not found")


# The for loop can also be used to ilterate through a dictionary

player ={
   "name": "Mbape",
   "age": 25,
   "teams":["PSG", "Monaco", "France"],
   "nationality": "French"
} 

for key in player:
   print(key)

   print('===============')
for value in player:
   print(player[value])

print('===============')
# loop through the teams the player has played for
for team in player["teams"]:
   print(team) 
