# This document Contains Header files for our Classes
# Card = name_suit_Value
# Hand_Deck = is made up of cards
# table contains a set amount of players

import random
import os
#Define what a card is gonna be
class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

    def show(self):
        print("____" + self.name + "-" + self.suit + " = " + str(self.value))
    def getImage(self):
        return str(self.name + self.suit)


class Hand:
    def __init__(self):
        self.cardList = []
        self.count = 0
        self.total = 0
        self.bust = False
        self.win = 0
        self.lose = 0
        self.draw = 0
        self.money = 500
        self.bustCount = 0
        self.bet = 20
        self.doubleDown = 0

    def getCount(self):
        return self.count
    def getMoney(self):
        return self.money
    def getWin(self):
        return self.win
    def getLose(self):
        return self.lose
    def getDraw(self):
        return self.draw

    def results(self):
        print("Win: " + str(self.getWin()))
        print("Lost: " + str(self.getLose()))
        print("draw: " + str(self.getDraw()))
        print("Money: " + str(self.getMoney()))
        print("Times Bust: " + str(self.bustCount))
        print("Times doubleDown: " + str(self.bustCount))

    def addCard(self, newCard):
        #add the card to the array
        self.cardList.append(newCard)
        self.count += 1

    def removeCard(self, num):

        temp = self.cardList[num]
        # print(temp)
        self.cardList.remove(temp)
        self.count -= 1
        return temp
    
    def showAll(self):
        if self.cardList:
            # print(self.cardList)
            image =[]
            for cards in self.cardList:
                image.append(cards.getImage())
            print(image, end="")
            print(" = " + str(self.calculateHand()))
        else:
            print("empty list")

    def makeDeck(self, num):
        #This right here makes a deck based on the number provided
        #print("HERE WORK AT MAKEDECK IN CLASS HAND")

        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

        #use to make a number of decks
        for k in range(num):
            for suit in suits:
                for i in range(13):
                    #edits for Name and Value go here
                    makeName = i
                    makeName += 1
                    newName = str(makeName)
                    # newValue = i
                    #newCard = Card(newName, suit, newValue)
                    newCard = Card(newName, suit, newName)
                    if makeName == 1:
                        newCard.value = 11

                    if makeName > 10:
                        newCard.value = 10
                    #basically add
                    #self.cardList.append(newCard)
                    #self.count += 1
                    self.addCard(newCard)
    def showFake(self):
        image = []
        image.append(self.cardList[1].getImage())
        image.append("??")
        print(image, end=" = ")
        print(str(self.cardList[1].value))

    def makeFakeDeck(self, num):
        print("HERE WORK AT MAKEDECK IN CLASS HAND")

        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

        #use to make a number of decks
        for k in range(num):
            for suit in suits:
                for i in range(13):
                    #edits for Name and Value go here
                    makeName = 0
                    makeName += 1
                    newName = str(makeName)
                    # newValue = i
                    #newCard = Card(newName, suit, newValue)
                    newCard = Card(newName, suit, newName)
                    if makeName == 1:
                        newCard.value = 11

                    if makeName > 10:
                        newCard.value = 10
                    #basically add
                    #self.cardList.append(newCard)
                    #self.count += 1
                    self.addCard(newCard)
    def dealCard(self):
        return self.removeCard(random.randint(0, self.count - 1))
    
    def payout(self, bool):
        #will pay out according to current bet

        if bool == True:
            #win.
            self.money += self.bet
        else:
            self.money -= self.bet

    def showHand(self, flag):
        self.showAll()
        if(flag == 0):
            print("HERE IS YOUR CURRENT HAND")
            print("OPTION:")
            print("[1] - HIT")
            print("[2] - Double Down")
            print("[3] - Pass")
            print("[4] - Split * NOT IMPLEMENTED")
        else:
            print("HERE IS YOUR CURRENT HAND")
            print("OPTION:")
            print("[1] - HIT")
            print("[2] - Pass")

    def playHand(self, deck):
        self.showHand(0)
        choice = input()
        #PLAY HAND DOESN'T RESET the stuff below it 
        while choice == "1":
            self.addCard(deck.dealCard())
            self.showAll()
            if self.calculateHand() < 22:
               self.showHand(1)
               choice = input()
            else:
                print("WHOOPS SOMEONE BUSTED")
                choice = "2"

        if choice == "2":
            self.addCard(deck.dealCard())
            if self.calculateHand() > 21:
                print("WHOOPS SOMEONE BUSTED")
    def playAi(self, num, deck):

        #3 personalities
        #1 - hit on 15
        #2 - hit on 16


        if num == 9999:
        #if dealer.cardList[1].value 
        #dealer's AI
            if self.calculateHand() == 17 and self.containAce():
                #hit on soft 17
                self.addCard(deck.dealCard())
            while self.calculateHand() < 17:
                self.addCard(deck.dealCard())
                if self.calculateHand() >= 22:
                    print("WHOOPS SOMEONE BUSTED")
                    break
        elif num == 1:
            #if dealer.cardList[1].value 
            while self.calculateHand() < 16:
                if (self.calculateHand() == 11 or self.calculateHand() == 10) and len(self.cardList) <= 2:
                    #double down
                    self.bet = 2*self.bet
                    self.addCard(deck.dealCard())
                    self.doubleDown += 1
                    break
                self.addCard(deck.dealCard())
                if self.calculateHand() >= 22:
                    print("WHOOPS SOMEONE BUSTED")
                    break
        elif num == 2:
            while self.calculateHand() < 17:
                if self.calculateHand() == 11 and len(self.cardList) <= 2:
                    #double down
                    self.bet = 2*self.bet
                    self.addCard(deck.dealCard())
                    self.doubleDown += 1
                    break

                self.addCard(deck.dealCard())
                if self.calculateHand() >= 22:
                    print("WHOOPS SOMEONE BUSTED")
                    break
        else:
            while self.calculateHand() < 15:
                if self.calculateHand() == 11 and len(self.cardList) <= 2:
                    #double down
                    self.bet = 2*self.bet
                    self.addCard(deck.dealCard())
                    self.doubleDown += 1
                    break
                self.addCard(deck.dealCard())
                if self.calculateHand() >= 22:
                    print("WHOOPS SOMEONE BUSTED")
                    break

    def reset(self):
        #this should remove the cards
        for i in range(len(self.cardList)):
            temp = self.dealCard()
        self.bust = False
         
    def containAce(self):
        for i in range(len(self.cardList)):
            if self.cardList[i].name == "1":
                return True
        #if you can't find an ace return false
        return False

    def calculateAce(self):
        if self.containAce():
           for i in range(len(self.cardList)):
                if self.cardList[i].name == "1" and self.total > 21:
                    #print("I will now be minus 10 because of an ace")
                    #print(str(i))
                    self.total -= 10
                    
        #print("Hello check is completed")

    def calculateHand(self):
        
        for i in range(len(self.cardList)):
            #print(self.cardList[i].value)
            self.total += int(self.cardList[i].value)

        self.calculateAce()

        if self.total > 21:
            self.bust = True

        temp = self.total
        #need to reset the total
        self.total = 0
        return temp
        
     

class GameBoard:
    def __init__(self):
       self.amountDeck = 1
       self.dealer = Hand()
       self.playerArray = []
       self.deck = Hand()
       #self.deck.makeDeck(self.amountDeck)
       self.amountPlayers = 2
       self.lineMax = 80
       self.rowMax = 10
       self.autoPlay = False
       self.gameOver = False
       self.round = 1
       self.maxRound = 1000
    def playGame(self):
        for i in range(self.amountPlayers):
            player = Hand()
            self.playerArray.append(player)
        #making Deck
        self.deck.makeDeck(self.amountDeck)
        while (self.gameOver == False):
            #Deal Cards Show Board, Allow for Play
            self.playRound()
            print("next Round?")
            next = input()
            if(next == "1"):
                continue
            else:
                self.gameOver = True
    def dealRound(self):
        #deals Player first then dealer
        for d in range(2):
            for i in range(len(self.playerArray)):
                self.playerArray[i].addCard(self.deck.dealCard())
            self.dealer.addCard(self.deck.dealCard())            
    def showBoard(self):
        os.system('cls')
        #maxRows - total Players - 1 for dealer = consistent menu
        for row in range(self.rowMax - (self.amountPlayers - 1)):
            if(row == 0):
                print("-" * 80)
                print(("PLAY GAME - ROUND " + str(self.round)).center(self.lineMax))
                self.round = self.round + 1
                print("[DEALER] - ", end="")
                self.dealer.showFake() 
                for i in range(len(self.playerArray)):
                    print("[PLAYER "+ str(i + 1) + "] - " , end="")
                    self.playerArray[i].showAll()
            print("")
        print("-" * 80)
    
    def victor(self):
        print("########################################################################")
        print("Now to tally up the score")
        for i in range(len(self.playerArray)):
            if self.playerArray[i].bust == True:
                print("Player " + str(i) + " LOST BY BUST")
                self.playerArray[i].lose += 1
                self.playerArray[i].bustCount += 1
                self.dealer.win += 1
                self.playerArray[i].payout(False)
            elif self.dealer.bust == True:
                print("Player " + str(i) + " WON BY BUST")
                self.playerArray[i].win += 1
                self.dealer.bustCount += 1
                self.dealer.lose += 1
                self.playerArray[i].payout(True)
            elif self.playerArray[i].calculateHand() > self.dealer.calculateHand():
                print("Player " + str(i) + " WON By beating the dealer")
                self.playerArray[i].win += 1
                self.dealer.lose += 1
                self.playerArray[i].payout(True)
            elif self.playerArray[i].calculateHand() == self.dealer.calculateHand():
                print("Player " + str(i) + " PUSH")
                self.playerArray[i].draw += 1
                self.dealer.draw += 1
            else:
                print("Player " + str(i) + " LOST")
                self.playerArray[i].lose += 1
                self.dealer.win += 1
                self.playerArray[i].payout(False)
            
            #reset the total hand
            self.playerArray[i].total = 0
            self.playerArray[i].bet = 20
            self.playerArray[i].reset()
        self.dealer.total = 0
        self.dealer.reset()


        if self.amountDeck == 1:
            #just one deck rest every time
            self.deck.reset()
            self.deck.makeDeck(self.amountDeck)
        #make sure the deck is still good
        if self.deck.getCount()//4 < 15:
            self.deck.reset()
            self.deck.makeDeck(self.amountDeck)

    def playRound(self):
         self.dealRound()
         for i in range(len(self.playerArray)):
            self.showBoard()
            print("[Player " + str(i + 1) + "] Turn")
            self.playerArray[i].playHand(self.deck)

         self.showBoard()
         print("[Dealer] Turn")
         self.dealer.playAi(9999, self.deck)
         self.victor()

    def roundAi(self):
        print("########################################################################")
        print("Lets play this round")

        for i in range(len(self.playerArray)):
            self.playerArray[i].playAi(self.dealer, int(i + 1),self.deck)
            print("Player " + str(i + 1) + " Turn" + "total is " + str(self.playerArray[i].calculateHand()))
        self.dealer.playAi(self.dealer, 9999,self.deck)
        print("For the Dealer Turn - Total is " + str(self.dealer.calculateHand()))
        self.victor()

    def showResults(self):
        print("########################################################################")
        print("for the final results")

        for i in range(len(self.playerArray)):
            print("results for Player " + str(i + 1))
            self.playerArray[i].results()

        print("RESULTS FOR THE DEALER")
        self.dealer.results()

    def display(self):
        os.system('cls')
        for row in range(self.rowMax - 2):
            if(row == 0):
                print("-" * 80)
                print(("MENU").center(self.lineMax))
                print("[1] - Play game")
                print("[2] - Settings")
                print("[3] - Exit")
            print("")
        print("-" * 80)
    def displaySetting(self):
        #adding this while loop to allow users to stay in setting mode till there is a break
        settingInput = " "
        while settingInput !="4":
                    
                    os.system('cls')
                    for row in range(self.rowMax - 2):
                        if(row == 0):
                            print("-" * 80)
                            print(("SETTINGS").center(self.lineMax))
                            print("[1] - Change Deck size - Currently at " + str(self.amountDeck))
                            print("[2] - Change Player size - Currently at " + str(self.amountPlayers))
                            print("[3] - Change autoPlay - Currently set as " + str(self.autoPlay))
                            print("[4] - EXIT")
                        print("")
                    print("-" * 80)

                    choice =" "
                    while choice!="4":
                        choice=input()
                        if(choice =="1"):
                            os.system('cls')
                            for row in range(self.rowMax - 2):
                                if(row == 0):
                                    print("-" * 80)
                                    print(("SETTINGS").center(self.lineMax))
                                    print("[1] - Deck size - Currently at " + str(self.amountDeck))
                                    print("ENTER - 'EXIT' to return to main screen")
                                    print("Please enter new Deck size (MAX IS 10)")
                                print("")
                            print("-" * 80)
                            delta = input()
                            if(delta == "EXIT" ):
                                break
                            else:
                                self.amountDeck = int(delta) 
                                break
                        elif(choice =="2"):
                            os.system('cls')
                            for row in range(self.rowMax - 2):
                                if(row == 0):
                                    print("-" * 80)
                                    print(("SETTINGS").center(self.lineMax))
                                    print("[1] - Player size - Currently at " + str(self.amountPlayers))
                                    print("ENTER - 'EXIT' to return to main screen")
                                    print("Please enter new Player size (MAX IS 6)")
                                print("")
                            print("-" * 80)
                            delta = input()
                            if(delta == "EXIT" ):
                                break
                            else:
                                self.amountPlayers = int(delta)
                                break
                        elif(choice =="3"):
                            os.system('cls')
                            for row in range(self.rowMax - 2):
                                if(row == 0):
                                    print("-" * 80)
                                    print(("SETTINGS").center(self.lineMax))
                                    print("[1] - Auto Play - Currently set at " + str(self.autoPlay))
                                    print("ENTER - 'EXIT' to return to main screen")
                                    print("Please enter 1 to set AutoPlay to YES")
                                print("")
                            print("-" * 80)

                            delta = input()
                            if(delta == "EXIT" ):
                                break
                            elif(delta =="1"):
                                self.autoPlay = True
                                break
                            else:
                                break
                        elif(choice=="4"):
                           settingInput = "4"