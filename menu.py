import os

class Menu:
    def __init__(self):
        size = os.get_terminal_size()
        self.row = size[1]
        self.column = size[0]
        self.buffer = 20 
    def displayTerminal(self, obj):
        os.system("cls")
        flag = True
        print("*" * self.column)
        for row in range(self.row - self.buffer):
            if(row == 0):
                for lines in obj:
                    if(flag):
                        print("=", end="")
                        print(lines.center(self.column))
                        flag = False
                    else:
                        print("= " + lines)
            print("=")
        print("*" * self.column)



