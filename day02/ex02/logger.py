#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
from random import randint
from timeit import default_timer as timer
import getpass
from functools import wraps


def log(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		f = open("machine.log", "a")
		start_time = timer()
		ret = func(*args, **kwargs)
		name = func.__name__.replace('_', ' ').capitalize()
		name = name.ljust(20, ' ')
		delta = timer() - start_time
		print (delta)
		if delta < 0.001:
			delta = delta * 1000
			f.write('(' + str(getpass.getuser()) + ')Running: '+ name + ' [exec-time = {:.3f} ms]\n'.format(delta))
		else:
			f.write('(' + str(getpass.getuser()) + ')Running: '+ name + ' [exec-time = {:.3f} s]\n'.format(delta))
		return ret
	return wrapper

class CoffeeMachine(): 
	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20: 
			return True
		else:
			print("Please add water!") 
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine(): 
			for _ in range(20): 
				time.sleep(0.1)
				self.water_level -= 1 
			print(self.boil_water()) 
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5)) 
		self.water_level += water_level 
		print("Blub blub blub...")

if __name__ == "__main__":
	machine = CoffeeMachine() 
	for i in range(0, 5):
		machine.make_coffee()
	
	machine.make_coffee() 
	machine.add_water(70)