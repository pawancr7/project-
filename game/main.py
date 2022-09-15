import random
# random is a module it take random number


def gamewin(comp, you):
    if comp == you:
        return None
  # computer selecting and player selecting
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        if you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        if you == 'w':
            return True


print("Comp turn : snake(s)  water(w) or gun(g) ?")

randno = random.randint(1, 3)

if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'

you = input("player 2 turn : snake(s)  water(w) or gun(g) ?")

a = gamewin(comp, you)

if a == None:
    print('the game is a tie ')
elif a:
    print('you win ')
else:
    print('you lose!')
