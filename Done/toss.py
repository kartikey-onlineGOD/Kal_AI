import choice
import random
import doub_str_algo

def cointoss(side):
	tossed_side = doub_str_algo.str_algo('heads', 'tails')
	#heads or tails is returned
	while True:
		if(side == tossed_side):
			print("You have won the toss! Do you want to bat or bowl first??")
			choice_made = input()
			if choice_made != 'bat' and choice_made != 'bowl':
				print("What else do you want to do in life huh? Type in a valid answer you twit!")
				print("")
				continue

			choice.choice_input(choice_made.lower())
			#user chooses either to bat first or bowl(in turn leads to chasing)
			break
			
		else:
			print("You lost the toss....")
			choice_made = doub_str_algo.str_algo('bat', 'bowl')
			#computer chooses as user lost the toss (50/50 chance using algo func)
			if(choice_made == 'bat'):
				print("Your opponent has chosen to bowl first!")
			else:
				print("Your opponent has chosen to bat first!")
			choice.choice_input(choice_made)
			break




