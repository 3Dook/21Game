from handDeck import *
import os


#TODO
#Make Display [11/20/2019]
#make sure single user game play works
##Make sure 1v1
##Make sure 1V1VXAuto
#make sure AutoPlay Works


game = GameBoard()
choice = " "
while choice != "3":

    game.display()
    choice = input()
    game.display()

    if(choice=="1"):
        game.playGame()
        #game.showBoard()
    elif(choice=="2"):
        game.displaySetting()
        #game.display()
    elif(choice=="3"):
        print("Good Bye")
        break
