from menu import Menu
from player import Player
from card import *
import random

class Game:
    def __init__(self, decks, players):
        self.numOfDeck = decks
        self.players = players
        self.roundCount = 1
        self.roundMax = 1000
        self.gameOver = False
        self.dealer = Player(2, 999999)
        temp = Hand()
        self.deck = temp.makeDeck(decks)
        self.discardPile = []
        #random.shuffle(self.deck)
        self.menu = Menu()
        self.startingBet = 50

    
    
    def startBet(self):
        #iterate through each and update their betting
        choice=""
        while choice !="7":
            obj = []
            obj.append("BETTING PHASE - ROUND " + str(self.roundCount))
            obj.append("PLEASE ENTER PLAYER NUMBER TO CHANGE - AUTO PLAYER CAN't BE CHANGED")
            i = 1
            for players in self.players:
                if(players.controller == 1):
                    obj.append("["+str(i)+"] Player " + str(i) + " - " + str(players.controller) + " BET AMT " + str([players.bet]))
                else:
                    obj.append("[*LOCKED* AUTO] Player " + str(i) + " - " + str(players.controller) + " BET AMT " + str([players.bet]))
                i += 1        
            obj.append("[7] continue || READY")
            self.menu.displayTerminal(obj)
            choice = input()
            try:
                if(self.players[int(choice) - 1].controller == 1):
                    obj = []
                    obj.append("BETTING PHASE - ROUND " + str(self.roundCount))
                    obj.append("PLEASE ENTER BETTING AMOUNT FOR PLAYER " + choice)
                    obj.append("PLAYER " + choice + " - CURRENT BANK AMOUNT IS " + str(self.players[int(choice) - 1].amount))
                    obj.append("PLEASE DO NOT BET OVER PLAYER'S BANK (HOW CAN ONE BET MORE THAN ONE HAVE?")
                    self.menu.displayTerminal(obj)
                    bet = input()
                    if(int(bet) <= self.players[int(choice) - 1].amount):
                        #good
                        self.players[int(choice) - 1].bet = int(bet)
                    else:
                        print("UNABLE TO CHANGE BET AMOUNT")
                        print("PLEASE ENTER ANY KEY to return to BETTING MENU")
                        input()

                else:
                    print("UNABLE TO CHANGE BETTING DUE TO LOCKED AUTO")
                    print("PLEASE ENTER ANY KEY to return to BETTING MENU")
                    input()
            except:
                pass
    def playerOptions(self, player):
        #Print Menu and options
        obj = []
        obj.append("21 GAME - ROUND " + str(self.roundCount))
        obj.append("DEALER {} = {} {}".format(self.dealer.showDealer(), self.dealer.bust, "??"))
        i = 1
        for playerHand in self.players:
            if playerHand.additionalHand:
                obj.append("{}PLAYER {} ADDTIONAL_HAND $[{}] BET[{}] - {} = {} {}".format(playerHand.current, playerHand.name, playerHand.amount, playerHand.bet, playerHand.showHand(), playerHand.bust, playerHand.value()))
            else:
                obj.append("{}PLAYER {} $[{}] BET[{}] - {} = {} {}".format(playerHand.current, playerHand.name, playerHand.amount, playerHand.bet, playerHand.showHand(), playerHand.bust, playerHand.value()))
            i += 1
        obj.append("**********************************")
        if player.additionalHand:
            obj.append("PLAYER {} ADDITIONAL HAND - TURN ".format(player.name))
        else:
            obj.append("PLAYER {} - TURN ".format(player.name))
        #THEN PLAYERS WILL PLAY
        obj.append("PLAYER {} HAND - {} = {}".format(player.name, player.showHand(), player.value()))
        obj.append("OPTION:")
        obj.append("[1] - PASS")
        obj.append("[2] - HIT")
        if(player.checkDouble()):
            obj.append("[3] - DOUBLEDOWN")
        else:
            obj.append("[3] - DOUBLE - LOCKED")
        if(player.checkSplit()):
            obj.append("[4] - SPLIT")
        else:
            obj.append("[4] - SPLIT - LOCKED")
        #obj.append(self.handOption)
        self.menu.displayTerminal(obj)

    def actionHit(self, player):
        player.add(self.deck.pop())

    def actionDouble(self, player):
        player.add(self.deck.pop())
        player.bet *= 2
        player.turnOver = True

    def actionSplit(self, player, index):
        # we need to create a new player and then insert them into the order list after
        temp = Player(1, player.amount)
        temp.name = str(index)
        temp.additionalHand = True
        # add new card to player's hand and remove old one.
        temp.add(player.remove())
        #player.add(self.deck.pop())
        newCard = Card("K", "H", 10)
        player.add(newCard)

        #if the player is an additional hand we need to fix the index or else
        # the player the order will be mess up
        tempIndex = index
        if player.additionalHand:
            tempIndex = self.players.index(player) + 1 #iterate it up

        self.players.insert(tempIndex, temp)
        
    def isNatural(self):
        flag = False
        if self.dealer.value() == 21:
            flag = True
            self.dealer.natural = True
        
        for player in self.players:
            if player.value() == 21:
                flag = True
                player.natural = True

        return flag

    def autoPlay(self, player, hitTill):
        # this is unique function that will return either, 1, 2, 3, 4 based
        # on a specific hittill rule. Essentially for dealer play. and potential
        # AI specifc plays. CURRENTLY SET AS DEALER MUST STAND AT 17

        if hitTill == 9999:
            #soft 17
            if player.checkAce():
                #add the card, to break out of the soft 17 rule
                player.add(self.deck.pop())
            
            while player.value() < 17:
                player.add(self.deck.pop())
        else:
            while player.value() < hitTill:
                player.add(self.deck.pop())

        if(player.value() > 21):
            player.bust = "BUST*"

    def round(self):
        #Deal Cards
        for i in range(2):
            for player in self.players:
                player.add(self.deck.pop())
            self.dealer.add(self.deck.pop())


        if self.isNatural():
            if self.dealer.natural:
                #results
                self.results()
                print("PRESS [1] TO CONTINUE or ANY OTHER KEY TO EXIT GAME... ", end="")
                choice = input()
                if choice != "1":
                    self.gameOver = True
                return


        #MENU
        for player in self.players:
            if player.natural:
                #automatic payout
                continue

            if (player.controller == 1):
                player.current = ">>>"
                if len(player.hand.list) < 2:
                    #this is for split hand
                    player.add(self.deck.pop())

                while not player.turnOver:
                    self.playerOptions(player)
                    choice = input()
                    if choice == "1":
                        player.turnOver = True
                    elif choice == "2":
                        self.actionHit(player)
                    elif choice == "3" and player.checkDouble():
                        self.actionDouble(player)
                    elif choice == "4" and player.checkSplit():
                        self.actionSplit(player, int(player.name))
                    else:
                        #catch the rest
                        player.turnOver = True

                    if player.value() > 21:
                        player.turnOver = True
                        player.bust = "*BUST*"
            else:
                self.autoPlay(player, 17) #always hit below 17
            player.turnOver = False
            player.current = ""
        #dealers turn
        self.autoPlay(self.dealer, 9999) #9999 dealer's number to do additional action
        #results
        self.results()
        print("PRESS [1] TO CONTINUE or ANY OTHER KEY TO EXIT GAME... ", end="")
        choice = input()
        if choice != "1":
            self.gameOver = True

    def results(self):
        # print out board and full results
        obj = []
        obj.append("21 GAME - ROUND " + str(self.roundCount))
        obj.append("DEALER {} = {} {}".format(self.dealer.showHand(), self.dealer.bust, self.dealer.value()))
        i = 1
        for playerHand in self.players:
            if playerHand.additionalHand:
                obj.append("PLAYER {} {} BET[{}] - {} = {} {}".format(playerHand.name, "**ADD_HAND", playerHand.bet, playerHand.showHand(), playerHand.bust, playerHand.value()))
            else:
                obj.append("PLAYER {} $[{}] BET[{}] - {} = {} {}".format(playerHand.name, playerHand.amount, playerHand.bet, playerHand.showHand(), playerHand.bust, playerHand.value()))
            i += 1
        obj.append("**********************************")
        # NEED TO RESET PLAYERS
        

        for index, player in enumerate(self.players):
            resultString = ""
            bet = 0
            if player.natural and not self.dealer.natural:
                # if they had a natural 21 and dealer did not, then reset
                player.natural = False
                self.dealer.natural = False
                bet = player.bet + player.bet//2
                resultString = "PLAYER {} - NATURAL BLACK JACK VICTORY || PLAYER WON${}".format(player.name, bet)
            elif self.dealer.natural and not player.natural:
                # dealer got natural and player did not
                bet = player.bet * -1
                resultString = "PLAYER {} - LOST BY DEALER NATURAL || PLAYER LOST${}".format(player.name, bet)
            elif(player.value() > 21):
                #bust no win || no matter what
                bet = player.bet * -1
                resultString = "PLAYER {} - LOST BY BUST || PLAYER LOST ${}".format(player.name, bet)
            elif(self.dealer.value() > 21):
                bet = player.bet 
                resultString = "PLAYER {} - WON BY DEALER BUST || PLAYER WON ${}".format(player.name,bet)
            elif(player.value() > self.dealer.value()):
                bet = player.bet
                resultString = "PLAYER {} - WON BY BEATING DEALER || PLAYER WON ${}".format(player.name, bet)
            elif(player.value() < self.dealer.value()):
                bet = player.bet * -1
                resultString = "PLAYER {} - LOST BY LOSING TO DEALER || PLAYER LOST ${}".format(player.name, bet)
            elif(player.value() == self.dealer.value()):
                #push
                resultString = "PLAYER {} - PUSH || NO CHANGE".format(player.name)

            if player.additionalHand == True:
                resultString = "ADDTIONAL HAND " + resultString
                player = self.players[index - 1]
                k = 2
                while player.additionalHand == True:
                    #player has multiple keep iterating backwards
                    player = self.players[index - k]
                    k += 1

            
            player.amount += bet
            obj.append(resultString)
            player.bust = ""
        self.dealer.bust = ""
        self.menu.displayTerminal(obj)

    def isAdditional(self):
        for player in self.players:
            if player.additionalHand == True:
                return True
        
        return False
    def cleanUp(self):
        #remove all players hand and doubleCheck.
        #print(self.deck)
        self.dealer.natural = False
        for player in self.players:
            player.natural = False
            player.bet = self.startingBet
            while player.hand.list: 
                self.discardPile.append(player.hand.remove())
        
        temp = []
        for player in self.players:
            #remove any additonal hand from the list
            if player.additionalHand:
                temp.append(player)
        for each in temp:
            self.players.remove(each)

        while self.dealer.hand.list:
            self.discardPile.append(self.dealer.hand.remove())

        #Check the deck size, if its  single deck then add discard back to deck and reshuffle
        # else shuffle deck at random number
        if self.numOfDeck == 1 or len(self.deck)//4 < 20:
            #reset and reshuffle when deck is only one, or really low
            self.deck = self.deck + self.discardPile
            self.discardPile = []
            random.shuffle(self.deck)
            random.shuffle(self.deck)
            random.shuffle(self.deck)

    def backTest(self):
        obj = []
        obj.append("THIS IS BACK TEST TO MAKE SURE STUFF IS WORKING")
        obj.append("THE ORIGINAL DECK SIZE OF CARDS IS - {}".format(self.numOfDeck * 52))
        obj.append("THE DECK SIZE OF CARDS IS AT - {}".format(len(self.deck)))
        obj.append("THE TRASH PILE OF CARDS IS AT - {}".format(len(self.discardPile)))
        self.menu.displayTerminal(obj)
    def start(self):
        #make deck, and make dealer
        #randomize the deck once before and only when the cards run low
        random.shuffle(self.deck)
        random.shuffle(self.deck)
        random.shuffle(self.deck)
        random.shuffle(self.deck)

        k = 1
        for player in self.players:
            player.name = str(k)
            k += 1

        while not self.gameOver:
            # start with betting iterate through each player to check if manual then iterate and setting up betting phase for each.
            self.startBet()
            self.round()
            self.cleanUp()
            #self.backTest()
            #iterate through each players actions.
            self.roundCount += 1     

