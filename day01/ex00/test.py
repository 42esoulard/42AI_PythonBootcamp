#!/usr/bin/env python
# -*- coding: utf-8 -*-

from book import Book 
from recipe import Recipe

name = "cookbook"
cookbook = Book(name)

try:
	#tourte = Recipe(name, lvl, time, ingredients, rtype, description)
	
	cookbook.add_recipe("tourte")
	print(cookbook.get_recipe_by_name("tourte"))
except ValueError as ex:
	print (ex)
except NameError as ex:
	print (ex)

