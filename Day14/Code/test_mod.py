import random

x = random.randint(0,100)

c = 0
while True:
    y = int(input("Number:"))
    if c < 7: 
        if x == y:
            c +=1
            print("Congratulations",c,'times')
            break
        elif x > y:
            c +=1
            print("<")
        
        else:
            c +=1
            print(">")
    else:
        print("Game over, %d times" % c)
        break
    

        


