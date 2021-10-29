import turtle

try:
    print('''I can draw the following Shapes for you :
1. Rectangle
2. Square
3. Circle
4. Equilateral Triangle
5. Rainbow Helix''')
    k = int(input("Enter a choice : "))
    t = turtle.Turtle( ) 
    if(k==1):
        t.forward(30)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(40)
        t.right(90)
    elif(k==2):
        for i in range(1,5):
            t.forward(30)
            t.right(90)
    elif(k==3):
        for i in range(360):
            t.forward(1)
            t.right(1)
    elif(k==4):
        t.left(60)
        t.forward(30)
        t.left(60)
        t.forward(30)
        t.left(60)
        t.forward(30)
    elif(k==5):
        import Helix



except:
    print("")
