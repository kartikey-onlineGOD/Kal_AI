#Dice roll Simulator
import random
import os 


A1 = '''
------
|     |
| o  |
|     |
------ '''
A2 = '''
------
|o   |
|     |
|   o|
------ '''
A3 = '''
------
|o   |
| o  |
|   o|
------ '''
A4 = '''
------
|o o|
|     |
|o o|
------ '''
A5 = '''
------
|o o|
| o  |
|o o|
------ '''
A6 = '''
------
|o o|
|o o|
|o o|
------ '''

money = 1000


def DiceRoll( ):
    global money
    global gg
    global A1
    global A2
    global A3
    global A4
    global A5
    global A6    
    D1 = random.randint(1,6)
    D2 = random.randint(1,6)
    if(D1 == 1):
        if(D2 == 1):
            print(A1 , ' ' , A1)
        if(D2 == 2):
            print(A1 , ' ' , A2)
        if(D2 == 3):
            print(A1 , ' ' , A3)
        if(D2 == 4):
            print(A1 , ' ' , A4)
        if(D2 == 5):
            print(A1 , ' ' , A5)
        if(D2 == 6):
            print(A1 , ' ' , A6)
    if(D1 == 2):
        if(D2 == 1):
            print(A2 , ' ' , A1)
        if(D2 == 2):
            print(A2 , ' ' , A2)
        if(D2 == 3):
            print(A2 , ' ' , A3)
        if(D2 == 4):
            print(A2 , ' ' , A4)
        if(D2 == 5):
            print(A2 , ' ' , A5)
        if(D2 == 6):
            print(A2 , ' ' , A6)

    if(D1 == 3):
        if(D2 == 1):
            print(A3 , ' ' , A1)
        if(D2 == 2):
            print(A3 , ' ' , A2)
        if(D2 == 3):
            print(A3 , ' ' , A3)
        if(D2 == 4):
            print(A3 , ' ' , A4)
        if(D2 == 5):
            print(A3 , ' ' , A5)
        if(D2 == 6):
            print(A3 , ' ' , A6)

    if(D1 == 4):
        if(D2 == 1):
            print(A4 , ' ' , A1)
        if(D2 == 2):
            print(A4 , ' ' , A2)
        if(D2 == 3):
            print(A4 , ' ' , A3)
        if(D2 == 4):
            print(A4 , ' ' , A4)
        if(D2 == 5):
            print(A4 , ' ' , A5)
        if(D2 == 6):
            print(A4 , ' ' , A6)            
    if(D1 == 5):
        if(D2 == 1):
            print(A5 , ' ' , A1)
        if(D2 == 2):
            print(A5 , ' ' , A2)
        if(D2 == 3):
            print(A5 , ' ' , A3)
        if(D2 == 4):
            print(A5 , ' ' , A4)
        if(D2 == 5):
            print(A5 , ' ' , A5)
        if(D2 == 6):
            print(A5 , ' ' , A6)
    if(D1 == 6):
        if(D2 == 1):
            print(A6 , ' ' , A1)
        if(D2 == 2):
            print(A6 , ' ' , A2)
        if(D2 == 3):
            print(A6 , ' ' , A3)
        if(D2 == 4):
            print(A6 , ' ' , A4)
        if(D2 == 5):
            print(A6 , ' ' , A5)
        if(D2 == 6):
            print(A6 , ' ' , A6)
    print("")
    money = money + ((D1+D2)*1000)
    print(D1 + D2)
    


        
def main( ):
    global money
    global gh
    print(" You start with 1000 credits and you must bet each time to role ")
    print('''You get 1000 credits for every number you get on the roll
and enter m to check balance ''')
    c = input(" Press yes to roll dice ")
    if(c=="yes"):
        DiceRoll( )
    elif(c=="m"):
        print("Balance = " , money)
        main( ) 
    else :
        print(" Invalid choice")
        main( )
main( ) 
