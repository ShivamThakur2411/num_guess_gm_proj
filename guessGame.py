import random
number = random.randrange(0,9)

print("================NUMBER GUESSING GAME================")
guess = int(input("ENTER THE NUMBER YOU THINK OF - "))
attemptCount=0

while attemptCount<5:
	attemptCount = attemptCount + 1
	if guess>number:
		print("The number you guessed was higher than the correct number")
		guess = int(input("ENTER THE NUMBER YOU THINK OF - "))
	elif guess<number:
		print("The number you guessed was lower than the correct number")
		guess = int(input("ENTER THE NUMBER YOU THINK OF - "))
	elif guess==number:
		print("CONGRATULATIONS, YOU WON!!")
		break
	if attemptCount==5 & guess!=number:
		print("Sorry, you lost the game, the correct number was - " + str(number))
		break