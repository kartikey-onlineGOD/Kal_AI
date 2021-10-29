import random

#algo for returning any of the two strings with a 50-50 chance
def str_algo(str1, str2):
	number = random.randint(0, 50)
	if number%2 == 0:
		return str1
	else:
		return str2