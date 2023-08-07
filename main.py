import time
import numpy as np
import sys

def delayprint(str):
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)



class Pokemon:
    def __init__(self,name,type,moves, EVs,bars, health = "||||||||||||||||||||||||||||" ):
        self.name = name
        self.type = type
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        
        self.health = health
        self.bars = bars


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
            if self.type ==k:
                #Both are same types
                if opponent.type ==k:
                    self.attack *= 0.5
                    self.defense *= 2
                    opponent.attack *= 0.5
                    opponent.defense *= 2
                    str1 = "Its not very affective"
                    str2 = "Its not very affective"

                #Opponent has type advantage
                if opponent.type == Pok_types[(i+1)%3]:
                    self.attack *= 0.5
                    self.defense *= 0.5
                    opponent.attack *= 2
                    opponent.defense *= 2
                    str1 = "Its not very affective"
                    str2 = "It is super affective"

                #Our pokemon is stronger
                if opponent.type ==  Pok_types[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    opponent.attack *= 0
                    opponent.defense *= 0
                    str1 = "It is super affective"
                    str2 = "It is super affective"



        while(self.bars > 0) and (opponent.bars > 0):
            print(f"{self.name}\t\t Health - \t{self.health}")
            print(f"{opponent.name}\t\t Health - \t{opponent.health}\n")

            print(f"Go {self.name}!")
            for i,x in enumerate(self.moves):
                print(f"{i+1}.{x}")
            index = int(input("Pick a move number: "))    
            delayprint(f"{self.name} used move {self.moves[index-1]}!")
            time.sleep(1)
            delayprint(str1)

            #Determine damage
            opponent.bars -=self.attack
            opponent.health = ""

            for j in range(int(opponent.bars+.1*opponent.defense)):
                opponent.health +="|"

            time.sleep(1) 
            print(f"\n{self.name}\t\t Health - \t{self.health}")
            print(f"\n{opponent.name}\t\t Health - \t{opponent.health}\n")
            time.sleep(1) 

            if opponent.bars <=0:
                delayprint("\n" + opponent.name + "has fainted")
                break


            print(f"Go {opponent.name}!")
            for i,x in enumerate(opponent.moves):
                print(f"{i+1}. {x}")


            index = int(input("Pick a move number: "))    
            delayprint(f"{opponent.name} used move {opponent.moves[index-1]}!")
            time.sleep(1)
            delayprint(str2)

            #Determine damage
            self.bars -=self.attack
            self.health = ""

            for j in range(int(self.bars+.1*self.defense)):
                self.health +="|"

            time.sleep(1) 
            print(f"{opponent.name}\t\t Health - \t{opponent.health}")
            print(f"{self.name}\t\t Health - \t{self.health}\n")
            time.sleep(1) 

            if self.bars <=0:
                delayprint("\n" + self.name + "has fainted")
                break




        money = np.random.choice(5000)
        delayprint(f"Opponent paid you {money}Rs")



if __name__ == '__main__':
    Charmander = Pokemon("Charmander","Fire",['Fire Punch','Ember'], {'ATTACK':52, 'DEFENSE':43}, 39)  
    Squirtle = Pokemon("Squirtle","Water",['Water gun','Bubble'], {'ATTACK':48, 'DEFENSE':65},44)  
    Bulbasaur = Pokemon("Bulbasaur","Grass",['Razor leaf','Vine whip'], {'ATTACK':49, 'DEFENSE':49},45)  



    pokemon_list = [Charmander,Squirtle,Bulbasaur]
    inp1 = int(input("Player 1 pick a pokemon number -1)Charmander 2)Squirtle 3)Bulbasaur"))
    inp2 = int(input("Player 2 pick a pokemon number -1)Charmander 2)Squirtle 3)Bulbasaur"))

    pokemon_list[inp1-1].fight(pokemon_list[inp2-1])