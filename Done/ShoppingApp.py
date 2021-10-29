# Dummy shopping application for all sort of Items
# Kartikey Pandey
# 22/5/2020

import time
Tp = 0
Items =[ ] 
price =[ ]
c = 0

#Introduction Page
pn =0
pn2=0

def Page_0( ):
    print("                                           𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝓢𝓱𝓸𝓹 𝓙𝓪𝓶")
    time.sleep(2)
    print("  ")
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    print(" ")
    print('''Page 1 : Electronic Gadgets and Devices
Page 2 : Home Appliances
Page 3 : Furniture
Page 4 : Stationary ''')
    pn = int(input("Enter page number from above list to view Items on the page "))
    time.sleep(2)
    print("  ")
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    if(pn==1):
        Page_1( )
    if(pn==2):
        Page_2( )
    if(pn==3):
        Page_3( )
    if(pn==4):
        Page_4( )
    if(pn>=6):        
        print("invalid choice")
        print(" ")
        Page_0( )
        
def Page_1( ) :
    c=0
    print('''1. Smart Phones
2. Featured Phones
3. Laptops
4. Speakers and Headphones ''')
    c=(int)(input('''Enter your choice of type of device
or Enter 0 to go back to home page '''))
    print("  ")
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    
    if(c==1):
           Page_1g1( )
    if(c==2):
           Page_1g2( )
    if(c==3):
           Page_1g3( )
    if(c==4):
           Page_1g4( )
    if(c==0):
           Page_0( ) 
   
        
def Page_1g1( ) :
    global c
    global Tp
    global Items
    global price
    print('''1. Samsung S10              Rs. 54,999
2. OnePlus 7                    Rs. 36,999
3. OnePlus 7 pro              Rs. 40,999
4. Iphone 11 pro               Rs. 1,05,499
5. Google Pixel 4              Rs. 98,999''')
    c1=int(input('''Enter your choice of smart phone
or Enter 0 to go back to home page '''))
    print("  ")
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    
    if(c1==1):
          Items.insert( c+1 , "Samsung S10")
          price .append( c+1 , "Rs. 54,999")
          Tp = Tp + 54999
          c=c+1
    if(c1==2):
          Items.insert( c+1 , "OnePlus 7")
          price.insert( c+1 , "Rs. 36,999" )
          Tp = Tp + 36999
          c=c+1
    if(c1==3):
          Items.insert(c+1 ,  "OnePlus 7 pro")
          price.insert( c+1 , "Rs. 40,999")
          Tp = Tp + 40999
          c=c+1
    if(c1==4):
          Items.insert(  c+1,"Iphone 11 pro")
          price.insert(c+1, "Rs. 1,05,499")
          Tp = Tp + 105999
          c=c+1
    if(c1==5):
          Items.insert( c+1,"Google Pixel 4")
          price.insert( c+1,"Rs. 98,999")
          Tp = Tp + 98999
          c=c+1
    gg = input("Do you want to continue shopping for Items [y/n] : ")
    if(gg=="y"):
        Page_0( )
    elif(gg=="n"):
        Billing( ) 


      

def Page_1g2( ) :
    global c
    global Tp
    global Items
    global price
    print('''1. Nokia 3100                  Rs. 1,999
2. Nokia 4900                  Rs. 3,099
3. Motorolla X 50             Rs. 3,999''')
    
              
    c2=int(input('''Enter your choice of featured phone
or Enter 0 to go back to home page '''))
    print("  ")
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    
    if(c2==1):
          Items.insert(c+1,"Nokia 3100")
          price.insert( c+1,"Rs. 1,999")
          Tp = Tp + 1999
          c=c+1
    if(c2==2):
          Items.insert(c+1, "Nokia 4900")
          price.insert( c+1,"Rs. 3,099" )
          Tp = Tp + 3099
          c=c+1
    if(c2==3):
          Items.insert( c+1,"Motorolla X 50")
          price.insert( c+1,"Rs. 3,999")
          Tp = Tp + 3999
          c=c+1
    if(c2==0):
           Page_0( )
    gg = input("Do you want to continue shopping for Items [y/n] : ")
    if(gg=="y"):
        Page_0( )
    elif(gg=="n"):
        Billing( ) 


           

def Page_1g3( ) :
    global c
    global Tp
    global Items
    global price
    print('''1. Dell Inspirion 13 5000                  Rs. 65,999
2. Macbook pro                               Rs. 1,65,099
3. Microsoft Surface                        Rs. 99,999''')
              
    c3=int(input('''Enter your choice of featured phone
or Enter 0 to go back to home page '''))
    print("  ")
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    
    if(c3==1):
          Items.insert(c+1, "Dell Inspirion 13 5000")
          price.insert( c+1,"Rs. 65,999")
          Tp = Tp + 65999
          c=c+1
    if(c3==2):
          Items.insert(c+1, "Macbook pro")
          price.insert( c+1,"Rs. 1,65,999")
          Tp = Tp + 165999
          c=c+1
    if(c3==3):
          Items.insert(c+1, "Microsoft Surface")
          price.insert( c+1,"Rs. 99,999")
          Tp = Tp + 99999
          c=c+1
    if(c3==0):
           Page_0( )
    gg = input("Do you want to continue shopping for Items [y/n] : ")
    if(gg=="y"):
        Page_0( )
    elif(gg=="n"):
        Billing( ) 


def Page_1g4( ) :
    global c
    global Tp
    global Items
    global price
    print('''1. Boat Bass 320                            Rs. 10,999
2. Boat Stone 250                           Rs. 4,999
3. Boat Rockerz 510                       Rs. 1,999''')
              
    c4=int(input('''Enter your choice of featured phone
or Enter 0 to go back to home page '''))
    print("  ")
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    
    if(c4==1):
          Items.insert(c+1, "Boat Bass 320")
          price.insert( c+1,"Rs. 10,999")
          Tp = Tp + 10999
          c=c+1
    if(c4==2):
          Items.insert(c+1, "Boat Stone 250")
          price.insert( c+1,"Rs. 4,999"  )
          Tp = Tp + 4999
          c=c+1
    if(c4==3):
          Items.insert( c+1,"Boat Rockerz 510")
          price.insert( c+1,"Rs. 1,999")
          Tp = Tp + 1999
    if(c4==0):
           Page_0( )
    gg = input("Do you want to continue shopping for Items [y/n] : ")
    if(gg=="y"):
        Page_0( )
    elif(gg=="n"):
        Billing( ) 

        
def Page_2( ) :
    print('''1. Television
2. Refrigeraftor
3. Washing Machines
4. Kitchen Stoves
5. Air Conditioners ans Coolers
6. Other Kitchen Appliances''')
    pn2 = int(input("Enter Item type number from above list to view Items on the page"))
    time.sleep(2)
    print("  ")
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    if(pn2==1):
        Page_2_1( )
    if(pn2==2):
        Page_2_2( )
    if(pn2==3):
        Page_2_3( )
    if(pn2==4):
        Page_2_4( )
    if(pn2==5):
        Page_2_5( )
    if(pn2==6):
        Page_2_6( )    
    if(pn2>=7):        
        print("invalid choice")
        print(" ")
        Page_0( )


        

def Page_2_1( ) :
    global c
    global Tp
    global Items
    global price
    print('''1. LG Ole-d 47                 Rs. 74,999
2. Sony Bravia                  Rs. 135,999
3. Mi TV 70'                      Rs. 68,999''')
              
    d1=int(input('''Enter your choice of Television 
or Enter 0 to go back to home page '''))
    print("  ")
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    
    if(d1==1):
         Items.insert( c+1,"LG Ole-d 47")
         price.insert( c+1,"Rs. 74,999")
         Tp = Tp + 74999
         c=c+1
    if(d1==2):
         Items.insert( c+1,"Sony Bravia")
         price.insert(c+1, "Rs. 135999" )
         Tp = Tp + 135999
         c=c+1
    if(d1==3):
         Items.insert( c+1,"Mi TV 70' ")
         price.insert( c+1,"Rs. 68999")
         Tp = Tp + 68999
         c=c+1
    if(d1==0):
        Page_0( ) 
    gg = input("Do you want to continue shopping for Items [y/n] : ")
    if(gg=="y"):
        Page_0( )
    elif(gg=="n"):
        Billing( )     
   
      

def Page_2_2( ) :
    global c
    global Tp
    global Items
    global price
    print('''1. Whirlpool 500L                  Rs. 78999
              2. Godrej 350L                      Rs. 61099
              3. Samsung Smart                Rs. 137999''')

    gg = input("Do you want to continue shopping for Items [y/n] : ")
    if(gg=="y"):
        Page_0( )
    elif(gg=="n"):
        Billing( )      
              
    d2=int(input('''Enter your choice of Refrigerator
or Enter 0 to go back to home page '''))
    print("  ")
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    
    if(d2==1):
          Items.insert( c+1,"Whirlpool 500L")
          price.insert( c+1,"Rs. 78999")
          Tp = Tp + 78999
          c=c+1
    if(d2==2):
          Items.insert(c+1, "Godrej 350L")
          price.insert( c+1,"Rs. 61099")
          Tp = Tp + 61099
          c=c+1
    if(d2==3):
          Items.insert( c+1,"Samsung Smart")
          price.insert( c+1,"Rs. 137999")
          Tp = Tp + 137999
          c=c+1
    if(d2==0):
           Page_0( )
    gg = input("Do you want to continue shopping for Items [y/n] : ")
    if(gg=="y"):
        Page_0( )
    elif(gg=="n"):
        Billing( ) 
           

def Page_2_3( ) :
    global c
    global Tp
    global Items
    global price
    print('''1. Seimens 400                      Rs. 25999
              2. Samsung G 20                   Rs. 37099
              3. Bosch K725                        Rs. 39999''')
              
    d3=int(input('''Enter your choice of Washing Machine
or Enter 0 to go back to home page '''))
    print("  ")
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    
    if(d3==1):
          Items.insert( c+1,"Seimens 400")
          price.insert( c+1,"Rs. 65999")
          Tp = Tp + 65999
          c=c+1
    if(d3==2):
          Items.insert( c+1,"Samsung G 20")
          price.insert( c+1,"Rs. 37099" )
          Tp = Tp + 37099
          c=c+1
    if(d3==3):
          Items.insert( c+1,"Bosch K725")
          price.insert( c+1,"Rs. 39999")
          Tp = Tp + 39999
          c=c+1
    if(d3==0):
           Page_0( )
    gg = input("Do you want to continue shopping for Items [y/n] : ")
    if(gg=="y"):
        Page_0( )
    elif(gg=="n"):
        Billing( ) 


def Page_2_4( ) :
    global c
    global Tp
    global Items
    global price
    print('''1. Prestige 4 Hob             Rs. 7,999
              2. Sunflame 3                   Rs. 4,999
              3. Elica 3 s                       Rs. 5,999''')
              
    c4=int(input('''Enter your choice of Kitchen Stove
or Enter 0 to go back to home page '''))
    print("  ")
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    
    if(c4==1):
          Items.insert(c+1, "Prestige 4 Hob")
          price.insert( c+1,"Rs. 7999")
          Tp = Tp + 7999
          c=c+1
    if(c4==2):
          Items.insert( c+1,"Sunflame 3")
          price.insert( c+1,"Rs. 4999" )
          Tp = Tp + 4999
          c=c+1
    if(c4==3):
          Items.insert(c+1, "Elica 3 s")
          price.insert( c+1,"Rs. 5999")
          Tp = Tp + 5999
          c=c+1
    if(c4==0):
           Page_0( )
    gg = input("Do you want to continue shopping for Items [y/n] : ")
    if(gg=="y"):
        Page_0( )
    elif(gg=="n"):
        Billing( ) 



def Page_2_5( ) :
    global c
    global Tp
    global Items
    global price
    print('''1. Voltas 1.5 ton              Rs. 32,999
2. LG 1.5 ton                   Rs. 37,099
3. Godrej 1.5 ton             Rs. 41,999''')
              
    c3=int(input('''Enter your choice of featured phone
or Enter 0 to go back to home page '''))
    print("  ")
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    
    if(c3==1):
          Items.insert( c+1,"Voltas 1.5 ton")
          price.insert( c+1,"Rs. 32999")
          Tp = Tp + 32999
          c=c+1
    if(c3==2):
          Items.insert( c+1,"LG 1.5 ton")
          price.insert( c+1,"Rs. 37099" )
          Tp = Tp + 37099
          c=c+1
    if(c3==3):
          Items.insert(c+1, "Godrej 1.5 ton")
          price.insert( c+1,"Rs. 41999")
          Tp = Tp + 41999
          c=c+1
    if(c3==0):
           Page_0( )
    gg = input("Do you want to continue shopping for Items [y/n] : ")
    if(gg=="y"):
        Page_0( )
    elif(gg=="n"):
        Billing( ) 


def Page_2_6( ) :
    global c
    global Tp
    global Items
    global price
    print('''1. Sujata Mixer                            Rs. 2999
2. Hitech Otg + oven                   Rs. 25999
3. Sunflame tandoor                   Rs. 12999''')
              
    c4=int(input('''Enter your choice of featured phone
or Enter 0 to go back to home page '''))
    print("  ")
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    
    if(c4==1):
          Items.insert( c+1,"Sujata Mixer")
          price.insert( c+1,"Rs. 2999")
          Tp = Tp + 2999
          c=c+1
    if(c4==2):
          Items.insert(c+1, "Hitech Otg + oven")
          price.insert(c+1, "Rs. 25999" )
          Tp = Tp + 25999
          c=c+1
    if(c4==3):
          Items.insert(c+1, "Sunflame tandoor")
          price.insert( c+1,"Rs. 12999")
          Tp = Tp + 12999
          c=c+1
    if(c4==0):
           Page_0( )
    gg = input("Do you want to continue shopping for Items [y/n] : ")
    if(gg=="y"):
        Page_0( )
    elif(gg=="n"):
        Billing( ) 




def Page_3( ) :
    print('''1. Couch and Recliners
2. Dining Table
3. Bed's''')
    e=int(input('''Enter number from above to select type of furniture
or enter 0 ot return to home page'''))
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")     
         
    if(e==1):
          Page_3_1( )
    if(e==2):
          Page_3_2( )
    if(e==3):
          Page_3_3( )
    else :
        Page_0( )
        
        
          
          

def Page_3_1( ):
    global c
    global Tp
    global Items
    global price
    print('''1. The L-shaped Couch      Rs. 44,999
2. The Lazy Boy                  Rs. 98,999 
3. Sofa Grande                   Rs. 74,999''')
    e1=int(input('''Enter number from above to select type of furniture
or enter 0 ot return to home page'''))
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    if(e1==1):
          tems =Items.insert( c+1,"The L-shaped Couch")
          price.insert(c+1, "Rs. 44999")
          Tp = Tp + 44999
          c=c+1
    if(e1==2):
          Items.insert( c+1,"The Lazy Boy")
          price.insert( c+1,"Rs. 98999" )
          Tp = Tp + 98999
          c=c+1
    if(e1==3):
          Items.insert(c+1, "Sofa Grande")
          price.insert( c+1,"Rs. 74999")
          Tp = Tp + 74999
          c=c+1
    if(e1==0):
           Page_0( )
    gg = input("Do you want to continue shopping for Items [y/n] : ")
    if(gg=="y"):
        Page_0( )
    elif(gg=="n"):
        Billing( ) 
          
def Page_3_2( ):
    global c
    global Tp
    global Items
    global price
    print('''1.  Round Table 4                   Rs. 15,999
2. Convertable 4-6                  Rs. 19,999
3. 6 Grande                             Rs. 22,999''')
    e1=int(input('''Enter number from above to select type of furniture
or enter 0 ot return to home page'''))
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    if(e1==1):
          tems =Items.insert( c+1,"Round Table 4")
          price.insert(c+1, "Rs. 15999")
          Tp = Tp + 15999
          c=c+1
    if(e1==2):
          Items.insert(c+1, "Convertable 4-6")
          price.insert( c+1,"Rs. 19999" )
          Tp = Tp + 19999
          c=c+1
    if(e1==3):
          Items.insert(c+1, "6 Grande")
          price.insert( c+1,"Rs. 22999")
          Tp = Tp + 22999
          c=c+1
    gg = input("Do you want to continue shopping for Items [y/n] : ")
    if(gg=="y"):
        Page_0( )
    elif(gg=="n"):
        Billing( )

        
def Page_3_3( ):
    global c
    global Tp
    global Items
    global price
    print('''1.  Single Bed                         Rs. 20,999
2. Queen size Bed                  Rs. 30,999
3. King size bed                      Rs. 38,999''')
    e1=int(input('''Enter number from above to select type of furniture
or enter 0 ot return to home page'''))
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    if(e1==1):
          tems =Items.insert( c+1,"Single Bed")
          price.insert( c+1,"Rs. 20999")
          Tp = Tp + 20999
          c=c+1
    if(e1==2):
          Items.insert( c+1,"Queen size Bed")
          price.insert( c+1,"Rs. 30999" )
          Tp = Tp + 30999
          c=c+1
    if(e1==3):
          Items.insert( c+1,"King size bed")
          price.insert( c+1,"Rs. 38999")
          Tp = Tp + 38999
          c=c+1
    if(e1==0):
           Page_0( )
    gg = input("Do you want to continue shopping for Items [y/n] : ")
    if(gg=="y"):
        Page_0( )
    elif(gg=="n"):
        Billing( )            



def Page_4( ) :
    global c
    global Tp
    global Items
    global price
    print('''1.  Pencil( 2B)-20                   Rs. 110
              2. Sharpener-20                     Rs. 75
              3. Eraser-20                           Rs. 90
              4. Colour Pencil(48 shades)   Rs. 285
              5. Poster Paints(12 colours)   Rs. 180
              6. Shading Pencils(24)           Rs. 380 ''')
    e1=int(input('''Enter number from above to select type of furniture
or enter 0 ot return to home page'''))
    for x in range(0, 20):
        print ("=ll=" ,  end=" ")
        time.sleep(0.1)
    print(" ")
    if(e1==1):
          tems =Items.insert(c+1, "Pencil( 2B)-20")
          price.insert( c+1,"Rs. 110")
          Tp = Tp + 110
          c=c+1
    if(e1==2):
          Items.insert(c+1, "Sharpener-20")
          price.insert( c+1,"Rs. 75" )
          Tp = Tp + 75
          c=c+1
    if(e1==3):
          Items.insert( c+1,"Eraser-20")
          price.insert( c+1,"Rs. 90")
          Tp = Tp + 90
          c=c+1
    if(e1==4):
          Items.insert( c+1,"Colour Pencil(48 shades)")
          price.insert(c+1, "Rs. 285")
          Tp = Tp + 285
          c=c+1
    if(e1==5):
          Items.insert(c+1, "Poster Paints(12 colours)")
          price.insert(c+1, "Rs. 180")
          Tp = Tp + 180
          c=c+1
    if(e1==6):
          Items.insert(c+1, "Shading Pencils(24)")
          price.insert( c+1,"Rs. 380")
          Tp = Tp + 380
          c=c+1
    if(e1==0):
           Page_0( )
    gg = input("Do you want to continue shopping for Items [y/n] : ")
    if(gg=="y"):
        Page_0( )
    elif(gg=="n"):
        Billing( ) 
        
        


def Billing( ):
    global Tp
    global Items
    global price
    global c
    print("Items \t\t\t\t Price")
    for x in range(0,c):
        I = Items[x]
        p =  price[x]
        print(I, "\t\t\t\t" , p)
        
    print("\nTotal Price : " , Tp )       

def main( ):
    floyd=0
    if(floyd==0):
        Page_0( )
        floyd+=1
    
