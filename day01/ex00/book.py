#!/usr/bin/env python
# -*- coding: utf-8 -*-

from recipe import Recipe
import datetime

recipes_list = {
	'starter',
	'lunch',
	'dessert',
}

class Book(object):
	def __init__(self, name):
		self.name = name
		self.last_update = datetime.datetime.now()
		self.creation_date = datetime.datetime.now()
		self.recipes_list = {'starter' : {},'lunch' : {},'dessert' : {},}

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance""" 
		try:
			for a in self.recipes_list:
				for b in self.recipes_list[a]:
					if b == name:
						return(self.recipes_list[a][b])
		except:
			print("Sorry I don't know that one!")
		pass
	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """ 
		if recipe_type != 'starter' and recipe_type != 'lunch' and recipe_type != 'dessert':
			raise ValueError("Recipe_type must either be starter, lunch or dessert.")
		else:
			print("Here are all {} recipes: ", recipe_type)
			for key, value in self.recipes_list[recipe_type]:
				print("- {},\n", key)
		pass
	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update""" 
		name = input("Enter a recipe name: ")
		lvl = input("What cooking level (1-5) does it require: ")
		time = input("How long does it take to cook: ")
		while True:
			try:
				nb_ing = int(input("How many ingredients: "))
				break
			except:
				print("The number of ingredients should be.. a number")
				continue
		ingredients = list()
		a = 0
		while a < nb_ing:
			add = input("Enter ingredient: ")
			ingredients.append(add)
			a += 1
		description = ""
		description = input("Add a description? If not, just press enter: ")
		rtype = input("Is that recipe for starter, lunch or dessert: ")
		add = name
		try:
			add = Recipe(name, lvl, time, ingredients, rtype, description)
			self.recipes_list[rtype].update( {name : add})
			self.last_update = datetime.datetime.now()
		except ValueError as ex:
			print (ex)
		pass



#cookbook.update( {recipe_name : {'ingredients' : ingredients}})
#	cookbook[recipe_name].update([ ('meal', meal) , ('prep_time', prep_time)] )