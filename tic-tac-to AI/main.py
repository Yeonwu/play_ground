class Board:

    def __init__(self):
        self.marks = [0, 0]

    def getXY(self, oOrx, posX, posY):
        return bool(self.marks[oOrx] & 2 ** (8 - posX - 3 * posY))

    def setXY(self, oOrx, posX, posY):
        if 0 > posX or posX > 2:
            raise Exception('setXY(self, oOrx, posX, posY): posX should be integer between 0 to 2.')
        if 0 > posY or posY > 2:
            raise Exception('setXY(self, oOrx, posX, posY): posY should be integer between 0 to 2.')
        if oOrx != 0 and oOrx != 1:
            raise Exception('setXY(self, oOrx, posX, posY): oOrx should be 0 or 1')
        
        if not(self.getXY(0, posX, posY) and self.getXY(1, posX, posY)):
            self.marks[oOrx] |= 2 ** (posX + posY * 3)
            return True
        return False

    def checkEnd(self):
        pass
    
    def printBoard(self):
        for y in range(0, 3):
            for x in range(0, 3):
                if self.getXY(0, x, y):
                    print("O", end=" ")
                elif self.getXY(1, x, y):
                    print("X", end=" ")
                else:
                    print("-", end=" ")
            print()
        print()


if __name__ == "__main__":
    board = Board()
    board.printBoard()
    board.setXY(0, 1, 1)
    board.printBoard()