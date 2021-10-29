
import toss
import ingame
import choice

print("Welcome to the cricket game - build v1.2.5   --- by Rohith (dev -- 25th May 2020 to present)")
while True:
	print("Pls choose a side while the coin is being flipped!")
	side = input()
	if side.lower() != 'heads' and side.lower() != 'tails':
		print("Type in a real side you knuckle head!")
		print("")
		continue
	#input for either heads or tails
	toss.cointoss(side.lower())
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

