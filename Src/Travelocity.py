
#Initialization of Varibles 
name =""
pno = 0
mail =""
inloc =""
budget = 0
travm = " "
stay = 0
nop =0
choice = 0;
c="no"

def Bill( ):
    print("the total cost of your stay + food = " , (( 700+(c*choice)+200) *nop *stay))

# Basic user inputs
def basicInfo( ):
    print("Welcome to our company ,Travelocity")
    print(" ")
    name = input("Please enter your name : ")
    print(" ")
    pno = input("Please enter your phone number : ")
    print(" ")
    mail = input("Please enter your email id :")
    print("""
                Thank yor for registering with Travelocity """)
    
#Choice of location and form of travel
def Choice( ):
    inloc = input("Enter the location you want to visit :")
    print(" ")
    stay = int(input("Enter your length of stay in days "))
    print(" ")
    nop = int(input("Enter number of people travelling"))
    print(" ")
    budget = int( input("Please enter your budget for the trip per person "))
    print(" ")
    print("Please enter a medium of travell to " , inloc)
    if((budget) <= 5000):
        print('''We suggest you travel my road
                   A recommended hotel there would be Sai Inn or Kamat''')
        travm = input("enter yes if you agree") 
        cheap( )
    if (10000>=(budget) > 5000):
        print('''We suggest you travel by train
                  A recommended hotel there would be Ibis or G'lore''')
        travm = input("enter yes if you agree") 
        cheap( )
    if((budget) >= 10000):
        print('''We suggest you travel by flight
                  A recommended hotel there would be Holiday inn or Taj ''')
        travm = input("enter yes if you agree") 
        cheap( )
      
        

def cheap( ):
    c="no"
    while(c=="no"):
        choice =int(input("""Hotels available in your price range are
                     1. Sai Inn                        800 Rs / per day 
                     2. Kamat Residence      900 Rs / per day 
                     3. Ram Krishna Motel    1000 Rs / per day
                     
                     Please enter you choice number"""))
 
        print("")
        c = (input('''Enter yes to complete booking and
                         no to go back to selection of hotels ''' ))
        if(c=="yes"):
            Bill( )
        elif(c=="no"):
            Choice( ) 

def cheap( ):
    c="no"
    while(c=="no"):
        choice =int(input("""Hotels available in your price range are
                     1. Sai Inn                        800 Rs / per day 
                     2. Kamat Residence      900 Rs / per day 
                     3. Ram Krishna Motel    1000 Rs / per day
                     
                     Please enter you choice number"""))
 
        print("")
        c = (input('''Enter yes to complete booking and
                         no to go back to selection of hotels ''' ))
        if(c=="yes"):
            Bill( )
        elif(c=="no"):
            Choice( ) 

                       
              
def cheap( ):
    c="no"
    while(c=="no"):
        choice =int(input("""Hotels available in your price range are
                     1. Sai Inn                        800 Rs / per day 
                     2. Kamat Residence      900 Rs / per day 
                     3. Ram Krishna Motel    1000 Rs / per day
                     
                     Please enter you choice number"""))
 
        print("")
        c = (input('''Enter yes to complete booking and
                         no to go back to selection of hotels ''' ))
        if(c=="yes"):
            Bill( )
        elif(c=="no"):
            Choice( )           
                  

        
basicInfo( )
Choice( )
    
    
    
    
    

