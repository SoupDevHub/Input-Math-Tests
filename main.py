print(f"\t Loading Variables...")
name = input(" What is your name? ").lower().title()
age = int(input(" How old are you? "))
print(f" Hello {name}!")

print(f"\n\t Dog Years")
print(f" 1 human year is 7 dog years.")
dogAge = age * 7
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