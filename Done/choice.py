import ingame

def choice_input(choice_made):
	#depedning on result of toss and choice, the user will either bat() or chase()
	if choice_made == 'bat':
		ingame.bat()
	else:
		ingame.chase()

