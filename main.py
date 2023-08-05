import time
import numpy as np
import sys

def delayprint(str):
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)



class Pokemon:
    def __init__(self,name,types,moves, EVs, speed, health = "|||||||||||||||||||"):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['Attack']
        self.defense = EVs['Defense']
        self.speed = speed
        self.bars = 20


def fight(self, opponent):

    #Printing info
    print("----Pokemon Battle----")
    print(f"\n{self.name}")
    print("Type - ", self.type)
    print("Attack - ", self.attack)
    print("defense - ", self.defense)
    print("Level - ", 5)
    print("\nVS")
    print(f"\n{opponent.name}")
    print("Type - ", opponent.type)
    print("Attack - ", opponent.attack)
    print("defense - ", opponent.defense)
    print("Level - ", 5)


    time.sleep(2)



    #Type advantages
    Pok_types = ["Fire", "Water", "Grass"]

    for i,k in enumerate(Pok_types):
        if self.types ==k:
            #Both are same types
            if opponent.types ==k:
                self.attack *= 0.5
                self.defense *= 2
                opponent.attack *= 0.5
                opponent.defense *= 2
                str1 = "Its not very affective"
                str2 = "Its not very affective"

            #Opponent has type advantage
            if opponent.types == Pok_types[(i+1)%3]:
                self.attack *= 0.5
                self.defense *= 0.5
                opponent.attack *= 2
                opponent.defense *= 2
                str1 = "Its not very affective"
                str2 = "It is super affective"

            #Our pokemon is stronger
            if opponent.types ==  Pok_types[(i+2)%3]:
                self.attack *= 2
                self.defense *= 2
                opponent.attack *= 0
                opponent.defense *= 0
                str1 = "It is super affective"
                str2 = "It is super affective"



    while(self.bars > 0) and (opponent.bars > 0):
        print(f"{self.name}\t\t Health - \t{self.health}")
        print(f"{opponent.name}\t\t Health - \t{opponent.health}")
