import random
print("computer turn: snake(s) water(w) or gun(g)?")
randno =random.randint(1,3)
if randno ==1 :
    comp ='s'
elif randno == 2:
    comp ='w'
elif randno == 3:
    comp ='g'

you =input("your turn: snake(s) water(w) or gun(g)?")

if comp =='s':
    if you == 'w':
        print("computer win")
    elif you == 'g':
        print("computer loss")
    else:
        print("no one can win")
elif comp =='w':
    if you == 'g':
        print("computer win")
    elif you == 's':
        print("computer loss")
    else:
        print("no one can win")
else:
    if you == 's':
        print("computer win")
    elif you == 'w':
        print("computer loss")
    else:
        print("no one can win")

print(comp)