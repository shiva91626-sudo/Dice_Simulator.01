import random
def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input('enter the number of sides:'))
print('first roll:', roll_dice(sides))
print('second roll:', roll_dice(sides))      
print('third roll:', roll_dice(sides))
print('fourth roll:', roll_dice(sides))