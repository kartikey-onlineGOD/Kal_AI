import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
sword = 0
flower = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  print ("After a drunken night out with friends, \nyou awaken the "
  "next morning in a thick, dank forest. \nHead spinning and " 
  "fighting the urge to\nvomit, you stand and marvel at your new, "
  "unfamiliar setting. \nThe peace quickly fades when you hear a "
  "grotesque sound \nemitting behind you. A slobbering Cyclops \nis "
  "running towards you. You will:")
  time.sleep(1)
  print ("""  A. Grab a nearby rock and throw it at the Cyclops
  B. Lie down and wait to be mauled
  C. Run""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nWelp, that was quick. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_run()
    import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
sword = 0
flower = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  print ("After a drunken night out with friends, you awaken the\n "
  "next morning in a thick, dank forest.\n Head spinning and " 
  "fighting the urge to vomit, you\n stand and marvel at your new, "
  "unfamiliar setting. The peace\n quickly fades when you hear a "
  "loud sound behind you\n. A One eyed Cyclops is "
  "running towards\n you. You will:")
  time.sleep(1)
  print ("""  A. Grab a nearby rock and throw it at the Cyclops
  B. Lie down and wait to be mauled
  C. Run""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nWelp, that was quick. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()

def option_rock(): 
  print ("\nThe Cyclops is stunned\n, but regains control. He begins "
  "running towards you again. Will you:")
  time.sleep(1)
  print ("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou decided to throw another rock, as if the first " 
    "rock thrown did much damage\n. The rock flew well over the "
    "Cyclopss head. You missed. \n\nYou died!")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  print ("\nYou were hesitant, since the cave was dark and "
  "ominous. Before you fully enter\n, you notice a shiny sword on "
  "the ground. Do you pick up a sword. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    sword = 1 #adds a sword
  else:
    sword = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. Hide in silence
  B. Fight
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nReally? You're going to hide in the dark? I think "
    "Cyclopss can see very well in\n the dark, right? Not sure, but "
    "I'm going with YES, so...\n\nYou died!")
  elif choice in answer_B:
   if sword > 0:
    print ("\nYou laid in wait. The shimmering sword attracted "
    "the Cyclops, which thought you\n were no match. As he walked "
    "closer and closer, your heart \nbeat rapidly. As the Cyclops "
    "reached out to grab the \nsword, you pierced the blade into "
    "its chest. \n\nYou survived!")
   else: #If the user didn't grab the sword
     print ("\nYou should have picked up that sword. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As the Cyclops enters the dark cave, you sliently "
    "sneak out. You're several feet away, but the Cyclops\n turns "
    "around and sees you running.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nYou run as quickly as possible, but the Cyclops's "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for an Cyclops. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
  print ("\nWhile frantically running, you notice a \nrusted "
  "sword lying in the mud. You\n quickly reach down and grab it, "
  "but miss. You try to calm \nyour heavy breathing as you hide "
  "behind a delapitated building,\n waiting for the Cyclops to come "
  "charging around the \ncorner. You notice a purple flower "
  "near your foot. \nDo you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    flower = 1 #adds a flower
  else:
    flower = 0
  print ("You hear its heavy footsteps and ready \nyourself for "
  "the impending Cyclops.")
  time.sleep(1)
  if flower > 0:
    print ("\nYou quickly hold out the purple flower,\n somehow "
    "hoping it will stop the Cyclops. \nIt does! The Cyclops was looking "
    "for love. "
    "\n\nThis got weird, but you survived!")
  else: #If the user didn't grab the sword
     print ("\nMaybe you should have picked \nup the flower. "
     "\n\nYou died!")

intro()
