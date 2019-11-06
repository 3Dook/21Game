# This document Contains Header files for our Classes
# Card = name_suit_Value
# Hand_Deck = is made up of cards
# table contains a set amount of players

import random

#Define what a card is gonna be
class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

    def show(self):
        print("____" + self.name + "-" + self.suit + " = " + str(self.value))


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
            for cards in self.cardList:
                cards.show()
            
            print("The Total is ... " + str(self.calculateHand()))
        else:
            print("empty list")

    def makeDeck(self, num):
        #This right here makes a deck based on the number provided
        print("HERE WORK AT MAKEDECK IN CLASS HAND")

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
        print("__????????????????__")
        self.cardList[1].show()
        print("The total is ... " + str(self.cardList[1].value))

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

    def playHand(self, deck):
        print("HERE IS YOUR CURRENT HAND")
        self.showAll()
        print("Do you want to Hit, double down or Pass? HIT == 1, double down == 2")
        choice = input()

        if choice == "2":
            self.addCard(deck.dealCard())
            self.showAll()
            if self.calculateHand() > 22:
                print("WHOOPS SOMEONE BUSTED")

        while choice == "1":
            self.addCard(deck.dealCard())
            self.showAll()
            if self.calculateHand() < 22:
               print("Do you want to Hit or Pass? HIT == 1")
               choice = input()
            else:
                print("WHOOPS SOMEONE BUSTED")
                choice = "2"
    def playAi(self, dealer, num, deck):

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
       self.deck.makeDeck(self.amountDeck)

    def addPlay(self):
        print("how many players?")
        howMany = input()
        for i in range(int(howMany)):
            player = Hand()
            self.playerArray.append(player)

    def dealRound(self):
        self.dealer.addCard(self.deck.dealCard())
        self.dealer.addCard(self.deck.dealCard())

        for i in range(len(self.playerArray)):
            self.playerArray[i].addCard(self.deck.dealCard())
            self.playerArray[i].addCard(self.deck.dealCard())
    
    def showBoard(self):
        print("########################################################################")
        print("NOW SHOWING THE BOARD")
        print("########################################################################")
        print("DEALER")
        self.dealer.showFake() 
        print("########################################################################")
        for i in range(len(self.playerArray)):
            print("PLAYER - " + str(i))
            self.playerArray[i].showAll()
            print("########################################################################")
    
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
         print("########################################################################")
         print("Lets play this round")

         for i in range(len(self.playerArray)):
            print("Player " + str(i + 1) + " Turn")
            self.playerArray[i].playHand(self.deck)

         print("For the Dealer")
         self.dealer.playHand(self.deck)
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