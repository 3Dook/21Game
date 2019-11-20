





class Menu:
        def __init__(self):
           self.title = "TITLE HOLDER"
           self.description = "Description Holder"
           self.rules = "RULES HOLDER"
           self.lineMax = 60
           self.Holder = 1
        def printLine(self, line):
            #use along with display to print a number to a line
            


        def display(self):
            print('*' * self.lineMax)
            str1 = (' ' * self.lineMax)
            line = list(str1)
            line[0] = "*"
            line[self.lineMax-1] = "*"

            
            for y in range(20):

                if( y == 1):
                    tit = self.title
                    newTit = tit.center(self.lineMax)
                    newTit = list(newTit)
                    newTit[0] = '*'
                    newTit[self.lineMax - 1] = '*'
                    newTit = "".join(newTit)
                    print(newTit)

                for i in range(self.lineMax):
                    print(line[i], end="")
                print("")
            print('*' * self.lineMax)   


menu = Menu()
menu.title = "Hello There"
menu.display()
