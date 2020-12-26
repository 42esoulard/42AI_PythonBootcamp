#!/usr/bin/env python
# -*- coding: utf-8 -*-


from random import randint

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")

myst = randint(1, 99)
atp = 1
while True:
	print("What's your guess between 1 and 99?")
	nb = input()
	if nb == 'exit':
		print("Goodbye!")
		break
	try:
		nb = int(nb)
	except:
		print("That's not a number!")
		continue
	if nb is myst:
		if myst is 42:
			print("The answer to the ultimate question of life, the universe and everything is 42.")
		if atp is 1:
			print("Congratulations! You've got it on your first try!")
		else:
			print("Congratulations, you've got it!")
			print("You won in", atp, "attemps!")
		break
	elif nb < myst:
		print("Too low!")
	elif nb > myst:
		print("Too high!")
	atp += 1
