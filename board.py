# This is a class document that will help manage game state.

import os
import re
from player import Player
from menu import Menu
from game import Game

class GameBoard:
    def __init__(self):
        #basic settings
        self.numOfDeck = 1
        self.numOfPlayers = 1
        self.playerArray = []
        self.showDisplay = 1
        self.startingAmount = 500
        self.autoPlay = 1 # 1 == manual, 2 == auto, 3 == custom
        self.doubleDown = 1 #true allows for all False only 10 and 11
        self.menu = Menu()
        self.checkSetting()

    def checkSetting(self):
        #this function will only get called once during the initalization.
        #If it is unable to find a setting.txt it will create one it self.
        if(os.path.exists("settings.txt")):
            #found txt file, and load.
            print("Found It")
            self.loadSettings()
        else:
            #make a file and load set basic values to start
            print("Did not Find IT")
            settings = open("settings.txt", "w+")
            settings.write("deckSize: 1\n")
            settings.write("playerSize: 1\n")
            settings.write("Display: 1\n")
            settings.write("StartingAmount: 500\n")
            settings.write("autoPlay: 3\n")
            settings.write("doubleDown: 1\n")
            settings.write("player1: 1\n")

            settings.close()
    def loadSettings(self):
        #this function will read settings from textfile and load game settings.
        settings = open("settings.txt", "r")
        content = settings.readlines()
        #saving settings into gameboard.
        temp = re.findall("\d+", content[0])
        self.numOfDeck = int(temp[0])
        temp = re.findall("\d+", content[1])
        self.numOfPlayers = int(temp[0])
        temp = re.findall("\d+", content[2])
        self.showDisplay = int(temp[0])
        temp = re.findall("\d+", content[3])
        self.startingAmount = int(temp[0])
        temp = re.findall("\d+", content[4])
        self.autoPlay = int(temp[0])
        temp = re.findall("\d+", content[5])
        self.doubleDown=int(temp[0])

        if(self.autoPlay == 3):
            for i in range(self.numOfPlayers): 
                temp = re.findall("\d+", content[i + 6])
                tempPlayer = Player(int(temp[1]), self.startingAmount)
                self.playerArray.append(tempPlayer)
        else:
            for i in range(self.numOfPlayers): 
                tempPlayer = Player(self.autoPlay, self.startingAmount)
                self.playerArray.append(tempPlayer)
        settings.close()
    
    def runMainMenu(self):
        l1 = "MENU"
        l2 = "[1] - PLAY GAME"
        l3 = "[2] - SETTINGS"
        l4 = "[3] - EXIT"
        lobj = [l1, l2, l3, l4]
        choice = ""
        while choice !="3":
            self.menu.displayTerminal(lobj)
            choice = input()
            if(choice=="1"):
                os.system('cls')
                self.runGame()
            elif(choice=="2"):
                self.changeSettings()
            elif(choice=="3"):
                print("Good bye thank you for playing!")
                return
    def runGame(self):
        game = Game(self.numOfDeck, self.playerArray)
        game.start()

    def printSettings(self):
        print(self.numOfDeck)
        print(self.numOfPlayers)
        print(self.showDisplay)
        print(self.startingAmount)
        print(self.autoPlay)
        print(self.playerArray)

    def updateSettings(self):
        #this function will directly rewrite all settings into document.
        self.playerControl = []
        settings = open("settings.txt", "w")
        settings.write("deckSize: " + str(self.numOfDeck) + "\n")
        settings.write("playerSize: " + str(self.numOfPlayers) + "\n")
        if(self.showDisplay == 1):
            settings.write("Display: 1\n")
        else:
            settings.write("Display: 2\n")
        settings.write("StartingAmount: " + str(self.startingAmount) + "\n")
        settings.write("autoPlay: " + str(self.autoPlay) + "\n")
        
        settings.write("doubleDown: " + str(self.doubleDown) + "\n")
        #by default set everything to manual regardless.
        tempArray = []
        for i in range(self.numOfPlayers):
            #if(self.playerArray[i]):
            if(self.autoPlay == 3):
                try:
                    temp = self.playerArray[i]
                    settings.write("Player "+ str(i + 1) + ": " + str(temp.controller) + "\n")
                    temp.amount = self.startingAmount
                    tempArray.append(temp)
                except:
                    #no players make some
                    temp = Player(self.autoPlay, self.startingAmount)
                    settings.write("Player "+ str(i+1) + ": " + str(temp.controller) + "\n")
                    tempArray.append(temp)
            else:
                #no players make some
                temp = Player(self.autoPlay, self.startingAmount)
                settings.write("Player "+ str(i+1) + ": " + str(temp.controller) + "\n")
                tempArray.append(temp)
        
        self.playerArray = []
        self.playerArray = tempArray
    
        settings.close()
    def sendDisplaytoMenu(self):
        obj = []
        obj.append("SETTINGS")
        obj.append("[1] - CHANGE DECK SIZE - CURRENTLY AT " + str(self.numOfDeck))
        obj.append("[2] - CHANGE PLAYER SIZE - CURRENTLY AT " + str(self.numOfPlayers))
        obj.append("[3] - CHANGE STARTING AMOUNT - CURRENT AT " + str(self.startingAmount))
        obj.append("[4] - CHANGE AUTOPLAY - CURRENT SET AT " + str(self.autoPlay))
        obj.append("[5] - CHANGE DOUBLEDOWN RULE - CURRENT SET AT " + str(self.doubleDown))
        obj.append("[6] - EXIT")
        self.menu.displayTerminal(obj)

    def changeSettings(self):
        # create an object and pass it to a menu function to read out.
        #self.sendDisplaytoMenu()
        choice = ""
        while choice !="6":
            self.sendDisplaytoMenu()
            choice=input()
            os.system('cls')
            if(choice == "1"):
                obj = []
                obj.append("SETTINGS")
                obj.append("[1] - DECK SIZE - CURRENTLY AT " + str(self.numOfDeck))
                obj.append("ENTER - 'exit' to return to settings screen")
                obj.append("PLEASE ENTER NEW DECK SIZE (MAX IS 10)")
                self.menu.displayTerminal(obj)
                delta = input()
                if(delta == "exit" ):
                    continue
                else:
                    self.numOfDeck = int(delta) 
                    self.updateSettings()
            elif(choice =="2"):
                obj = []
                obj.append("SETTINGS")
                obj.append("[1] - PLAYER SIZE - CURRENTLY AT " + str(self.numOfPlayers))
                obj.append("ENTER - 'exit' to return to settings screen")
                obj.append("PLEASE ENTER NEW PLAYER SIZE (MAX IS 6)")
                self.menu.displayTerminal(obj)
                delta = input()
                if(delta == "exit" ):
                    continue
                else:
                    self.numOfPlayers = int(delta)
                    self.updateSettings()
            elif(choice =="3"):
                obj = []
                obj.append("SETTINGS")
                obj.append("[1] - PLAYER STARTING AMOUNT - CURRENTLY AT " + str(self.startingAmount))
                obj.append("ENTER - 'exit' to return to settings screen")
                obj.append("PLEASE ENTER NEW STARTING AMOUNT")
                self.menu.displayTerminal(obj)
                delta = input()
                if(delta == "exit" ):
                    continue
                else:
                    self.startingAmount = int(delta)
                    self.updateSettings()
            elif(choice =="4"):
                obj = []
                obj.append("SETTINGS")
                obj.append("[1] - AUTOPLAY - CURRENTLY SET AT " + str(self.autoPlay))
                obj.append(" * * * 1 = MANUAL || 2 = ALL AUTO || 3 = CUSTOM {CHANGE AND UPDATE INDIVIDUALLY")
                obj.append("ENTER - 'exit' to return to settings screen")
                self.menu.displayTerminal(obj)
                delta = input()
                if(delta == "exit" ):
                    continue
                elif(delta == "3"):
                    self.autoPlay = int(delta)
                    self.changePlayerControllers()
                else:
                    self.autoPlay = int(delta)
                    self.updateSettings()
                    #need to make a function to change players
            elif(choice =="5"):
                obj = []
                obj.append("SETTINGS")
                obj.append("[1] - TOGGLE DOUBLEDOWN RULE - CURRENTLY AT " + str(self.startingAmount))
                obj.append(" 1 - allows any double on any hand || 2 - allows only on 10 or 11")
                obj.append("ENTER - 'exit' to return to settings screen")
                self.menu.displayTerminal(obj)
                delta = input()
                if(delta == "exit" ):
                    continue
                else:
                    self.doubleDown = delta
                    self.updateSettings()

        #menu.printConsole()
    def changePlayerControllers(self):
        choice = ""
        while (choice !="7"):
            obj = []
            obj.append("CHANGE PLAYER CONTROLS")
            obj.append("PLEASE TOGGLE PLAYER CONTROLS [ 1 - manual || 2 - AUTO]")
            obj.append(" 1 - allows any double on any hand || 2 - allows only on 10 or 11")

            i = 1
            for players in self.playerArray:
                obj.append("["+str(i)+"] Player " + str(i) + " - " + str(players.controller))
                i += 1        
            obj.append("[7] EXIT - to return to settings screen")
            self.menu.displayTerminal(obj)
            choice=input()
            if(int(choice) != 7):
                try:
                    if(self.playerArray[int(choice) - 1].controller == 1):
                        self.playerArray[int(choice) - 1].controller = 2
                    else:
                        self.playerArray[int(choice) - 1].controller = 1
                    self.updateSettings()
                except:
                    pass