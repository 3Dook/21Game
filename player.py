# Player Class
from card import *
import json

class Player:
    def __init__(self, control, amount):
        self.controller = control
        self.amount = amount
        self.bet = 50
        self.hand = Hand()
        self.turnOver = False
        self.bust = ""
        self.natural = False
        self.name = ""
        self.current = ""
        self.additionalHand = False

    def toJson(self):
        playerDict = {
            "controller": self.controller,
            "amount": self.amount,
            "bet": self.bet
        }
        return json.dumps(playerDict)

    def showHand(self):
        temp = []
        for card in self.hand.list:
            temp.append(card.getImage())
        obj ="{}".format(temp)
        return obj
    
    def showDealer(self):
        temp = "['{}', '??']".format(self.hand.list[0].getImage())
        return temp

    def add(self, card):
        self.hand.list.append(card)

    def remove(self):
        return self.hand.list.pop()
         
    def value(self):
        total = 0

        flag = False
        for card in self.hand.list:
            if(card.value == 11):
                flag = True 
            total += card.value
        #check for ace
        if(flag):
            if(total > 21):
                for i in range(len(self.hand.list)):
                    if self.hand.list[i].name == "A" and total > 21:
                        total -= 10
        return total
    def turn(self):
        return True
    def checkDouble(self):
        flag = False
        if len(self.hand.list) == 2:
            flag = True
        return flag
    def checkSplit(self):
        flag = False
        if len(self.hand.list) == 2:
            if(self.hand.list[0].name == self.hand.list[1].name):
                flag = True
        return flag
    def checkAce(self):
        flag = False
        for card in self.hand.list:
            if card.name == "A":
                flag = True
        return flag
    def cleanHand(self):
        for card in self.hand.list:
            self.hand.list.pop()