from handDeck import *
import os


#TODO
#Make Display [11/20/2019]
#make sure single user game play works
##Make sure 1v1
##Make sure 1V1VXAuto
#make sure AutoPlay Works
#make sure if dealer reveals an ace to stop and check board for play
#there an issue with hiting first then passing second, makes them hit twice.



game = GameBoard()
choice = " "
while choice != "3":

    game.display()
    choice = input()
    game.display()

    if(choice=="1"):
        game.playGame()
        game.resetBoard()
        #game.showBoard()
    elif(choice=="2"):
        game.displaySetting()
        #game.display()
    elif(choice=="3"):
        print("Good Bye")
        break
