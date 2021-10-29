import time
import random
import tkinter 
import os


ch=0

print("Hello there , I am Jarvis " )
time.sleep(3)
print("Your personal assistant.....")
print(" ")

for i in range(0,15):
    print("*****" , end = " ")
    time.sleep(0.1)

print(' ')

def Choice( ):
    global ch
    print (''' Here are a list of things i can do for you
1. Set a Timer [ enter timer ]
2. Play a game [ enter game ]
3. ''')
    ch = input("\nJust enter the number of what you want to do : ")
    ch=ch.upper( )
    if(ch=="TIMER" or ch=="1"):
        timer( )
    elif(ch=="GAME"or ch=="2"):
        Game( ) 
    
        
def timer( ) :
    t = float(input("Enter how long you want the timer to be in minutes : "))
    for x in range(1 ,int( t*60+1)):
        if( x % 15 ==0):
            print("T - " , x , end = " seconds ")              

        time.sleep(0.9)
    print("Time up ") 

def Game( ):
    ch=int(input('''I have three games you can play
1. I try and guess the number you thinking of in under 12 tries
2. Tik Tak Toe [2 player game]
3. Hand Cricket
4. HangMan [ Animals and Words ]
5. Adventure Game 
Enter your choice '''))
    for i in range(0,15):
        print("*****" , end = " ")
        time.sleep(0.1)
    print("")    
    if(ch==1):
        NG( )
    elif(ch==2):
        TicTacToe( )
    elif(ch==3):
        HC( )
    elif(ch==4):
        HM( )
    elif(ch==5):
        AG( )


def NG( ):
    print("Hello !!!")
    print("My name is Jarvis , I am a master of mathematics and strategy ")
    time.sleep(1)
    for x in range ( 0 , 20):
        print("*****" , end="")
        time.sleep(0.1)
   
    time.sleep(1)
    print("\nThink of a number between 0 to 1000")
    time.sleep(5)
    print("Done ?")
    time.sleep(1)
    print("Well done ")
    ch = 'n'
    s=0
    l=1000
    m=500
    count = 1
    while( ch == 'n') :
        print(" Is your number above " , m)
        k = input("y/n or enter e if equal ")
        if(k=='n'):
            l=m
        elif(k=='y'):
            s=m
        elif(k=='e'):
            print(" Your number is found " , m , " and it only took me " , count , " guesses")
            break 
        m=int((l+s)//2)
        count = count + 1    


def TicTacToe( ):
    os.system("TicTacToeCode.py")
    Choice( ) 

def HC( ):
    import main
    main.Start( )
    print("")
    Choice( ) 

def HM( ):
    import Hangman
    Hangman.HangMan( )
    print("")
    Choice( ) 

def AG( ):
    import AdventureGame
    AdventureGame.intro( )
    print("")
    Choice( )


    
Choice( )
m=input("Do you want me to do any other task [y/n]")
if(m=='y'):
    Choice( )
elif(m=='n'):
    print("Thank you for letting me assist you")







        
