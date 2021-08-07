print(f"\t Loading Variables...")
from random  import *
name = input(" What is your name? ").lower().title()
age = int(input(" How old are you? "))
print(f" Hello {name}!")

print(f"\n\t Cat Years")
print(f" 1 human year is 3.2 cat years.")
dogAge = age * 3.2
print(f" {name}, you are {age} years old, that means that you are {dogAge} dog years old!")

print(f"\n\t Cat Years")
print(f''' Cat years are a lot more complex than dog years. \n The first year of a cat's life is worth 15 human years. \n The second is worth nine. All other years are worth four.''')
if (age == 1):
    catAge = 15
elif (age == 2):
    catAge = 24
elif (age >= 3):
    catAge = age * 4 + 24
print(f" {name}, you are {age} years old, that means that you are {catAge} cat years old!")

print(f"\n\t List Making")
print(f' {name}, I want you to list some of your favorite things.')
things = [0, 1, 2]
for thing in things:
    if (thing == 0):
        things[thing] = input(' One of your favorite things: ')
    else:
        things[thing] = input(' Another one of your favorite things: ')
print(f'I love {things[0]}, {things[1]}, and {things[2]}!')

print(f'I have a game for you')
print(f'Try to guess what number im thinking of')
print(f'You get 5 tries')
print(f'Ill even give you hints!')

bob = randint(1,100)

turn = 1
turnsleft = 7

name = input("Welcome to the game, what is your name? ")

while True:
	print(f'\n{name.title()}, this is turn {turn}, you have {turnsleft} turns left')
	turn += 1
	turnsleft -= 1
	player = input("Please pick a number from 1-100 ")
	player = int(player)

	if bob == player:
		print("You guessed it! You win")
		break
	elif bob > player:
		print("Higher")
	else:
		print("Lower")
		
	if turn == 8:
		print("You ran out of turns!")
		break		
		
print('''

   _____                         ____                 _ 
  / ____|                       / __ \               | |
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __| |
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| |
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |  |_|
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|  (_)
                                                        
                                                        

''')		

print(f'The winning number was {bob}')
