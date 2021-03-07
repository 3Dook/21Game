# This is a class document that will help manage game state.

import os
import re
from player import Player
from menu import Menu
from game import Game
import json

class GameBoard:
    def __init__(self):
        #basic settings
        self.numOfDeck = 1
        self.numOfPlayers = 1
        self.playerArray = []
        self.showDisplay = 1
        self.startingAmount = 500
        self.autoPlay = 3 # 1 == manual, 2 == auto, 3 == custom
        self.doubleDownRule = 1 #true allows for all; False only 10 and 11
        self.menu = Menu()
        self.checkSetting()

    def checkSetting(self):
        #Use during initilization to check if there is already a file
        # else create it.
        if(os.path.exists("settings.json")):
                #found txt file, and load.
                print("Found It")
                self.loadSettings()
        else:
            #make a file and load set basic values to start
            print("Did not Find IT")
            newPlayer = Player(1, 500)
            settings_dict = {'numOfDeck': 1,
                'doubleDownRule': 1,
                'startingAmount': 500,
                'autoPlay': 3,
                'numOfPlayers': 1,
                'playerArray': [newPlayer.toJson()]
            }

            with open('settings.json', 'w') as json_file:
                json.dump(settings_dict, json_file)
                json_file.close()
    def loadSettings(self):
    #This function will load and update the board state
        with open('settings.json') as f:
            data = json.loads(f.read())
            f.close()
        
        self.numOfDeck = data['numOfDeck']
        self.startingAmount = data['startingAmount']
        self.doubleDownrule = data['doubleDownRule']
        self.numOfPlayers = data['numOfPlayers']
        self.autoPlay = data['autoPlay']
        #loop to add players
        for i in range(self.numOfPlayers):
            try:
                temp = json.loads(data['playerArray'][i])
                tempPlayer = Player(temp['controller'], temp['amount'])
                tempPlayer.bet = temp['bet']
                self.playerArray.append(tempPlayer)
            except:
                # bad data need to make a new player and add to list
                newPlayer = Player(1, 500)
                self.playerArray.append(newPlayer)
                self.updateSettings()

    def runMainMenu(self):
        l1 = "MENU"
        l2 = "[1] - PLAY GAME"
        l3 = "[2] - SETTINGS"
        l4 = "[q] - EXIT"
        lobj = [l1, l2, l3, l4]
        choice = ""
        while choice !="q":
            self.menu.displayTerminal(lobj)
            choice = input()
            if(choice=="1"):
                os.system('cls')
                self.runGame()
            elif(choice=="2"):
                self.changeSettings()
            elif(choice=="q"):
                print("Good bye thank you for playing!")
                return
    def runGame(self):
        game = Game(self.numOfDeck, self.playerArray)
        game.start()
        self.updateSettings()

    def printSettings(self):
        print(self.numOfDeck)
        print(self.numOfPlayers)
        print(self.showDisplay)
        print(self.startingAmount)
        print(self.autoPlay)
        print(self.playerArray)
        os.system('Pause')

    def updateSettings(self):
        #this function will directly rewrite all settings into document.\
        tempPlayerArray = []
        
        saveData = {
            'numOfDeck': self.numOfDeck,
            'doubleDownRule': self.doubleDownRule,
            'startingAmount': self.startingAmount,
            'autoPlay': self.autoPlay,
            'numOfPlayers': self.numOfPlayers,
            'playerArray': []
        }

        if(self.autoPlay == 3):
            for i in range(self.numOfPlayers):
                try:
                    saveData['playerArray'].append(self.playerArray[i].toJson())
                    tempPlayerArray.append(self.playerArray[i])
                except:
                    # bad data need to make a new player and add to list
                    newPlayer = Player(2, self.startingAmount)
                    tempPlayerArray.append(newPlayer)
                    saveData['playerArray'].append(newPlayer.toJson())
        else:
           for i in range(self.numOfPlayers):
                try:
                    self.playerArray[i].controller = self.autoPlay
                    saveData['playerArray'].append(self.playerArray[i].toJson())
                    tempPlayerArray.append(self.playerArray[i])
                except:
                    # bad data need to make a new player and add to list
                    newPlayer = Player(self.autoPlay, self.startingAmount)
                    saveData['playerArray'].append(newPlayer.toJson())
                    tempPlayerArray.append(self.playerArray[i])
        
        self.playerArray = tempPlayerArray
        with open('settings.json', 'w') as json_file:
            json.dump(saveData, json_file)
            json_file.close()

    def sendDisplaytoMenu(self):
        obj = []
        obj.append("SETTINGS")
        obj.append("[1] - CHANGE DECK SIZE - CURRENTLY AT " + str(self.numOfDeck))
        obj.append("[2] - CHANGE PLAYER SIZE - CURRENTLY AT " + str(self.numOfPlayers))
        obj.append("[3] - CHANGE STARTING AMOUNT - CURRENT AT " + str(self.startingAmount))
        obj.append("[4] - CHANGE AUTOPLAY - CURRENT SET AT " + str(self.autoPlay))
        obj.append("[5] - CHANGE DOUBLEDOWN RULE - CURRENT SET AT " + str(self.doubleDownRule))
        obj.append("[q] - EXIT")
        self.menu.displayTerminal(obj)

    def changeSettings(self):
        # create an object and pass it to a menu function to read out.
        #self.sendDisplaytoMenu()
        choice = ""
        while choice !="q":
            self.sendDisplaytoMenu()
            choice=input()
            os.system('cls')
            if(choice == "1"):
                obj = []
                obj.append("SETTINGS")
                obj.append("[1] - DECK SIZE - CURRENTLY AT " + str(self.numOfDeck))
                obj.append("ENTER - 'q' to return to settings screen")
                obj.append("PLEASE ENTER NEW DECK SIZE (MAX IS 10)")
                self.menu.displayTerminal(obj)
                delta = input()
                if(delta == "q" ):
                    continue
                else:
                    self.numOfDeck = int(delta) 
                    self.updateSettings()
            elif(choice =="2"):
                obj = []
                obj.append("SETTINGS")
                obj.append("[1] - PLAYER SIZE - CURRENTLY AT " + str(self.numOfPlayers))
                obj.append("ENTER - 'q' to return to settings screen")
                obj.append("PLEASE ENTER NEW PLAYER SIZE (MAX IS 6)")
                self.menu.displayTerminal(obj)
                delta = input()
                if(delta == "q" ):
                    continue
                else:
                    self.numOfPlayers = int(delta)
                    self.updateSettings()
            elif(choice =="3"):
                obj = []
                obj.append("SETTINGS")
                obj.append("[1] - PLAYER STARTING AMOUNT - CURRENTLY AT " + str(self.startingAmount))
                obj.append("ENTER - 'q' to return to settings screen")
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
                obj.append("ENTER - 'q' to return to settings screen")
                self.menu.displayTerminal(obj)
                delta = input()
                if(delta == "q" ):
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
                obj.append("ENTER - 'q' to return to settings screen")
                self.menu.displayTerminal(obj)
                delta = input()
                if(delta == "q" ):
                    continue
                else:
                    self.doubleDownRule = delta
                    self.updateSettings()

        #menu.printConsole()
    def changePlayerControllers(self):
        choice = ""
        while (choice !="q"):
            obj = []
            obj.append("CHANGE PLAYER CONTROLS")
            obj.append("PLEASE TOGGLE PLAYER CONTROLS [ 1 - manual || 2 - AUTO]")

            i = 1
            for players in self.playerArray:
                obj.append("["+str(i)+"] Player " + str(i) + " - " + str(players.controller))
                i += 1        
            obj.append("[q] EXIT - to return to settings screen")
            self.menu.displayTerminal(obj)
            choice=input()
            if(choice != "q"):
                try:
                    if(self.playerArray[int(choice) - 1].controller == 1):
                        self.playerArray[int(choice) - 1].controller = 2
                    else:
                        self.playerArray[int(choice) - 1].controller = 1
                    self.updateSettings()
                except:
                    pass