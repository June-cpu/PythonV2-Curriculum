
# Functions-Assignment.ipynb exercise 1
def square(x):
	return x * x
def hello():
	print("Hello Python!")

# Functions-Assignment.ipynb exercise 2

def add(a, b):
	return a + b	

def is_even(num):
	if num % 2 == 0:
		return True
	else:
		return False
	
# Functions-Assignment.ipynb exercise 3

def greet_user(name = "Guest"):
	print("Hello " + name)

def describe_pet(animal_type, pet_name):
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name + ".")

# Functions-Assignment.ipynb Challenges
	
def max_of(a, b, c):
	if a > b and a > c:
		return a
	elif b > a and b > c:
		return b
	else:
		return c
	
def concat_strings(*args):
	return ''.join(args)


