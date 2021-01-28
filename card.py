import random
#Define what a card is gonna be
class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

    def show(self):
        print(self.name + self.suit + " = " + str(self.value))
    def getImage(self):
        return (self.name + self.suit)
    
class Hand:
    def __init__(self):
        self.list = []
    
    def add(self, card):
        self.list.append(card)
    def remove(self):
        return self.list.pop()
    def clear(self):
        self.list = []
    def shuffle(self):
        random.shuffle(self.list)
    def makeDeck(self, num):
        #returns a collection of card (a 52 card deck) based on provided number
        #suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        suits = ["\u2665", "\u2666", "\u2660", "\u2663"]

        #return suits
                #use to make a number of decks
        temp = []
        for k in range(num):
            for suit in suits:
                for i in range(13):
                    #edits for Name and Value go here
                    newName = str(i + 1)
                    value = i + 1
                    if value > 10:
                        value = 10
                    if(newName == "1"):
                        newName = "A"
                        value = 11
                    elif(newName == "11"):
                        newName = "J"
                    elif(newName == "12"):
                        newName = "Q"
                    elif(newName == "13"):
                        newName = "K"


                    newCard = Card(newName, suit, value)
                    temp.append(newCard)
        return temp
    def showHand(self):
        print(self.list)
        temp = []
        for card in self.list:
            temp.append(card.getImage())
        return temp
