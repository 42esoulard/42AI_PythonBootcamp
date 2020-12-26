#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Recipe(object):
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
		if isinstance(name, str):
			self.name = name
		else:
			raise ValueError("Name must be a string.")
		if cooking_lvl.isnumeric() and 0 < int(cooking_lvl) < 6:
			self.cooking_lvl = cooking_lvl
		else:
			raise ValueError("Cooking_lvl must be between 1 and 5.")
		if cooking_time.isnumeric() and int(cooking_time) >= 0:
			self.cooking_time = cooking_time
		else:
			raise ValueError("Cooking_time must be a positive number of minutes.")
		if isinstance(ingredients, list):
			self.ingredients = ingredients
		else:
			raise ValueError("Ingredients must be a list.")
		if isinstance(description, str) or description == "":
			self.description = description
		else:
			raise ValueError("Description should be a string.")
		if recipe_type != 'starter' and recipe_type != 'lunch' and recipe_type != 'dessert':
			raise ValueError("Recipe_type must either be starter, lunch or dessert.")
		else:
			self.recipe_type = recipe_type

	def __str__(self):
		"""Return the string to print with the recipe info""" 
		txt = "Recipe for {}: lvl {}, {} minutes, cook for {}.\n Ingredients: {}\n{}".format(self.name, 
			self.cooking_lvl, self.cooking_time, self.recipe_type, self.ingredients, self.description)
		"""Your code goes here"""
		return txt

