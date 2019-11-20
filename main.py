from handDeck import *
from Menu import *



#variables

game = GameBoard()
print("########################################################################")
print("########################################################################")
print("Do you want to play? 1 == yes")
choice = input()

if choice == "1":
    game.addPlay()

while choice == "1":
   game.dealRound()
   game.showBoard()

   print("########################################################################")
   print("########################################################################")  

   #game.playRound()
   print("how many rounds?")
   num = input()
   for i in range(int(num)):
       game.roundAi()

   print("########################################################################")
   print("########################################################################")
   print("Do you wanna play another Round?")
   choice = input()

game.showResults()


