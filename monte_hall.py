# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 08:43:04 2019

@author: Dimpoo
"""

import random

doors = [0]*3
goatdoor = [0]*2
swap = 0
not_swap = 0
willing=True

while willing:
    x = random.randint(0,2)

    for i in range(0,3):
        if(i==x):
            doors[x] = "BMW"
        else:
            goatdoor.append(i)
            doors[i] = "Goat"

    print(x)
    choice = int(input("Enter your choice: "))
    open_door = random.choice(goatdoor)

    while(open_door == choice):
        open_door = random.choice(goatdoor)
    
    ch = input("Do you want to swap? (Y/N)")
    if(ch=='Y' or ch=='y'):
        if(doors[choice]=='Goat'):
            print("Player wins")
            swap = swap+1
        else:
            print("Player lost")
    else:
        if(doors[choice]=='Goat'):
            print("Player lost")
        else:
            print("Player wins")
            not_swap = not_swap + 1
    ch_game = int(input("Enter 1 to continue and 0 to quit: "))
    if(ch_game==1):
        continue
    else:
        break
        
print("wins with swaping: ",swap)
print("Wins without swaping: ",not_swap)