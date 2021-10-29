
import random





#print the score when the user asks for it
def score_track(score, bat):
	if bat == 'score':
		print(f"Score : {score}")
		print("")
		


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




def bat():
	score = 0
	print("BAT!")
	while True:
		ball = random.randint(0, 7)
		bat = input()
		if bat != "score" and bat.isdigit() == False:
			print("Type in a number noob!")
			print("")
			continue
		#user inputs a number or asks for score
		scoretracker.score_track(score, bat)
		if bat.isdigit() == False:
			#reruns the loop and skips the following code if user enters a string
			continue
		bat = int(bat)
		#bat is always converted into an int ifs it is not a string
		if bat > 6:
			print("Obey the rules! Dont think your smarter than me. You cannot score more than 6 runs at a time!! BAT!")
			#just a little touchy feature to stop players from breaking my game xD
			continue
		if(bat == ball):
			#print messages according to the case
			print("Your out!")
			if score == 0:
				print("You got out for a Duck xD!")
			else:
				print(f"You scored {score} runs!")
			break
		else:
			#print messages according to the case
			print(f"You scored +{bat}")
			score = score + bat		
	score1 = random.randint(0, 101)
	#computer will randomly generate a total score
	if score1 > score:
		#print messages according to the case
		print("Your opponent chased down the score!")
		print("You lost!")
		print("Game over!")
	else:
		#print messages according to the case
		print("Your opponent couldnt chase down your score")
		print("You won!")
		print("Congrats!")


def chase():
	score1 = random.randint(0, 101)
	#computer will randomly generate a total score
	print(f"Your opponent has scored {score1}!")
	print("BAT!")
	score = 0
	#below code functions similar to the earlier code
	while True:
		ball = random.randint(0, 7)
		bat = input()
		if bat != "score" and bat.isdigit() == False:
			print("Type in a number fool!")
			print("")
			continue	
		scoretracker.score_track(score, bat)
		if bat.isdigit() == False:
			continue
		bat = int(bat)

		if bat > 6:
			print("Obey the rules! Dont think that yur smarter than me! You cant score more than 6 at a time! BAT!")
			continue
		if(bat == ball):
			#print messages according to the case
			print("Your out!")
			if score == 0:
				print("You got out for a Duck xD!")
			else:
				print(f"You scored {score} runs!")
			print("GAME OVER :C")
			break
		else:
			#print messages according to the case
			print(f"You scored +{bat}")
			score = score + bat
			
			
			if score > score1:
				print("Your opponent couldnt defend their score!")
				print("You won!")
				print("Congrats!")
				break


def str_algo(str1, str2):
	number = random.randint(0, 50)
	if number%2 == 0:
		return str1
	else:
		return str2


def choice_input(choice_made):
	#depedning on result of toss and choice, the user will either bat() or chase()
	if choice_made == 'bat':
		ingame.bat()
	else:
		ingame.chase()



print("Welcome to the cricket game - build v1.2.5   --- by Rohith (dev -- 25th May 2020 to present)")
while True:
	print("Pls choose a side while the coin is being flipped!")
	side = input()
	if cointoss(side.lower()) != 'heads' and side.lower() != 'tails':
		print("Type in a real side you knuckle head!")
		print("")
		continue
	#input for either heads or tails
	cointoss(side.lower())
	print("Do you want to play again?")
	yn = input()
	#stop the program or reruns it depending on the input    
	if(yn == 'yes'):
		continue
	elif(yn == 'no'):
		break
	else:
		print("You didnt give me a legit answer fancy boi, so imma challenge you again!")
		print("")
		continue

print("Thx for playing!")
		


