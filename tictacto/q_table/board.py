class Board:

    def __init__(self):
        self.marks = 0
    
    def reset(self):
        self.marks = 0

    def state(self):
        return self.marks

    def getXY(self, posX, posY):
        if self.marks & 2 ** (posX + 3 * posY):
            return 1
        elif (self.marks >> 9) & 2 ** (posX + 3 * posY):
            return -1
        return 0

    def setXY(self, oOrx, posX, posY):
        if 0 > posX or posX > 2:
            raise Exception('setXY(self, oOrx, posX, posY): posX should be integer between 0 to 2.')
        if 0 > posY or posY > 2:
            raise Exception('setXY(self, oOrx, posX, posY): posY should be integer between 0 to 2.')
        if oOrx != 0 and oOrx != 1:
            raise Exception('setXY(self, oOrx, posX, posY): oOrx should be 0 or 1')
        
        if not self.getXY(posX, posY):
            self.marks |= 2 ** (posX + posY * 3 + 9 * (oOrx))
            return True
        return False
 
    def checkWinner(self):
        row_states = [7, 56, 448, 73, 146, 292, 273, 84]
        for row_state in row_states:
            if self.marks & row_state == row_state:
                return 1
            elif (self.marks >> 9) & row_state == row_state:
                return -1
        if (self.marks | (self.marks >> 9)) & 511 == 511:
            return 0.5
        return 0
    
    def render(self):
        for y in range(0, 3):
            for x in range(0, 3):
                state = self.getXY(x, y)
                if state == 1:
                    print("O", end=" ")
                elif state == -1:
                    print("X", end=" ")
                else:
                    print("-", end=" ")
            print()
        print()

if __name__ == '__main__':
    board = Board()
    done = False
    turn = True
    while not done:
        board.render()

        if turn:
            x, y = map(int, input("O TURN: ").split())
            board.setXY(0, x, y)
        else:
            x, y = map(int, input("X TURN: ").split())
            board.setXY(1, x, y)

        turn = not turn
        done = board.checkWinner()
        
    board.render()
    if done == 1:
        print("WINNER: O")
    elif done == -1:
        print("WINNER: X")
    else:
        print("???")

