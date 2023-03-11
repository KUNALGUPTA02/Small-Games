
import random

#first computer choose random no. 

print("computer choose random no.")
randno =random.randint(1,100)
c= None 
i=1
while c!= randno :
    #then user choose no.
    c=int(input("user choose no. : "))
    if randno > c :
        print ("choose more greater  no. ")
    elif randno < c :
        print ("choose more lesser no. ")
    else :
        print("your guessed in attempts\n", i)
    i=i+1
    



    
