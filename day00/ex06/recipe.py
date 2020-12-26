#!/usr/bin/env python
# -*- coding: utf-8 -*-

cookbook = {
	'sandwich': 
		{
			'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
			'meal' : 'lunch',
			'prep_time' : 10,
		}, 
	'cake': 
		{
			'ingredients' : ['flour', 'sugar', 'eggs'],
			'meal' : 'dessert',
			'prep_time' : 60,
		}, 
	'salad': 
		{
			'ingredients' : ['avocado', 'arangula', 'tomatoes', 'spinach'],
			'meal' : 'lunch',
			'prep_time' : 15,
		}, 
}

def print_recipe(recipe_name):
	print("\nRecipe for ", recipe_name, ':', sep='')
	print("Ingredients list: ", cookbook[recipe_name]['ingredients'], sep='')
	print("To be eaten for ", cookbook[recipe_name]['meal'], '.', sep='')
	print("Takes ", cookbook[recipe_name]['prep_time'], " minutes of cooking", '.', sep='')
	#for key, value in cookbook[recipe_name].items():
	#	print(value)

def del_recipe(recipe_name):
	del cookbook[recipe_name]
	print("\n", recipe_name, " recipe deleted!", sep='')
#for key, value in cookbook.items():
#	print(key)
#	for key in value:
#		print(key + ':', value[key])

def add_recipe(recipe_name, ingredients, meal, prep_time):
	cookbook.update( {recipe_name : {'ingredients' : ingredients}})
	cookbook[recipe_name].update([ ('meal', meal) , ('prep_time', prep_time)] )

cont = True


print("\nPlease select an option by typing the corresponding number:")
print("1: Add a recipe")
print("2: Delete a recipe")
print("3: Print a recipe")
print("4: Print the cookbook")
print("5: Quit")

while cont is True:
	choice = input()

	if choice is '1':
		print("\nWhat recipe do you want to add?")
		nm = input()
		while True:
			try:
				n = int(input("How many ingredients?"))
				print("\nWhat are its ingredients?")
				ing = list()
				for i in range(0, n):
					stock = input()
					ing.append(stock)
				break
				#ing = tuple(ing)
			except:
				print("\nIngredients number should be a number!")
				continue
		while True:
			print("\nShould we eat it for lunch or dessert?")
			meal = input()
			if meal != "lunch" and meal != "dessert":
				print("It can either be lunch or dessert!")
				continue
			else:
				break
		while True:
			print("\nWhat's its preparation time?")
			try:
				pt = int(input())
				break
			except:
				print("Please enter the number of minutes!")
				continue
		add_recipe(nm, ing, meal, pt)
	elif choice is '2':
		print("\nWhat recipe should we delete?")
		try:
			rp_nm = input()
			del_recipe(rp_nm)
		except:
			print("Sorry, that recipe isn't in my cookbook yet!")
			continue
	elif choice is '3':
		print("\nPlease enter the recipe's name to get its details:")
		try:
			rp_nm = input()
			print_recipe(rp_nm)
		except:
			print("Sorry, that recipe isn't in my cookbook yet!")
			continue
	elif choice is '4':
		print("The cookbook contains :")
		for key, value in cookbook.items():
			str = key.title()
			print("	-", str)
	elif choice is '5':
		print("\nCookbook closed.")
		cont = False
	else:
		print("This option does not exist, please type the corresponding number.")
		print("To exit, enter 5.")

