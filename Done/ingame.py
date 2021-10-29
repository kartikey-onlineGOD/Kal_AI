import random
import scoretracker

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






