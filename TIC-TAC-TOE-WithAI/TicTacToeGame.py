import random

random.seed(1)
import math

class TicTacToeGame:

    def __init__(self):
        cells = "_________"
        self.area = [[*cells[i:i + 3]] for i in range(0, len(cells), 3)]
        self.x_turn = len([x for x in cells if x == "X"]) <= len([x for x in cells if x == "O"])

        # print(self.area)

    def user_turn(self):
        while True:
            xy = [int(x) for x in input("Enter coordinates:").split(" ") if x.isdigit()]
            if len(xy) != 2:
                print("You should enter numbers!")
            else:
                x, y = xy
                if min(x, y) < 1 or max(x, y) > 3:
                    print("Coordinates should be from 1 to 3!")
                elif self.area[-y][x - 1] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    return x, y

    def start(self):
        # self.print_cells()
        while True:
            cmd = input("Input command:")
            actual = 'start easy user medium hard'.split()
            com = cmd.split()
            if len(com) == 3:
                for word in com:
                    if word in actual:
                        pass
                    elif word == 'exit':
                        return
                    else:
                        print('Bad parameters!')
                        break
                break
            else:print('Bad parameters!')
            #
            # if cmd in ['start hard user','start hard hard','start user hard','start easy medium','start medium easy','start medium medium','start easy easy', 'start medium user', 'start user user', 'start user medium','start user easy','start easy user']:
            #     break
            # elif cmd == 'exit':return
            # else:
            #     print('Bad parameters!')
        self.print_cells()
        #com = cmd.split()
        calls = {'easy':self.ezaimove,'hard':self.hardmove,'medium':self.ai_move_easy,'user':self.user_move}
        while True:
            calls[com[1]]()
            self.print_cells()
            if self.winwin(): break
            calls[com[2]]()
            self.print_cells()
            if self.winwin(): break

    def winwin(self):
        win = self.is_game_over()
        if win:
            if win == 'Draw':
                print('Draw')
                return True
            else:
                print(f"{win} wins")
                return True
        return None

    def is_game_over(self):
        if "_" in [cell for row in self.area for cell in row]:
            winner = self.check_winner()
            if winner:
                #print(f"{winner} wins")
                return winner
        else:
            winner = self.check_winner()
            if winner:
                #print(f"{winner} wins")
                return winner
            else:
                #print("Draw")
                return 'Draw'
        return False

    def user_move(self):
        x, y = self.user_turn()
        self.move(-y, x - 1)

    def move(self, y, x):
        self.area[y][x] = "X" if self.x_turn else "O"
        self.x_turn = not self.x_turn

    def ai_move_easy(self):
        move = list()
        aival = "X" if self.x_turn else "O"
        bestscore = -math.inf
        cells = [cell for row in self.area for cell in row]
        print('Making move level "hard"')
        for i in range(3):
            for j in range(3):
                if self.area[i][j] == "_":
                    self.area[i][j] = aival
                    score = self.minimax(self.area,0, False,aival)
                    self.area[i][j] = "_"
                    if (score > bestscore):
                        bestscore = score
                        move = [i, j]
        self.area[move[0]][move[1]] = aival
        self.x_turn = not self.x_turn
    def hardmove(self):
        move = list()
        aival = "X" if self.x_turn else "O"
        bestscore = -math.inf
        cells = [cell for row in self.area for cell in row]
        print('Making move level "medium"')
        for i in range(3):
            for j in range(3):
                if self.area[i][j] == "_":
                    self.area[i][j] = aival
                    score = self.minimax(self.area,0, False,aival)
                    self.area[i][j] = "_"
                    if (score > bestscore):
                        bestscore = score
                        move = [i, j]
        self.area[move[0]][move[1]] = aival
        self.x_turn = not self.x_turn
    def ezaimove(self):
        aival = "X" if self.x_turn else "O"
        print('Making move level "easy"')
        cells = [cell for row in self.area for cell in row]
        coord = random.choice([i for i, cell in enumerate(cells) if cell == "_"])
        cells[coord] = "X" if self.x_turn else "O"
        self.x_turn = not self.x_turn
        self.area = [[*cells[i:i + 3]] for i in range(0, len(cells), 3)]

    def getscore(self,aival,uval,result):
        if result == aival : return 10
        elif result == uval : return -10
        else : return 0

    def minimax(self,area,depth,ismax,aival):
        uval = 'X' if aival=='O' else "O"
        result = self.is_game_over()
        score = []
        if result :
            return self.getscore(aival,uval,result)
        if ismax:
            for i in range(3):
                for j in range(3):
                    if area[i][j] == "_":
                        area[i][j] = aival
                        score .append( self.minimax(area,depth+1, False,aival))
                        area[i][j] = "_"
        else:
            for i in range(3):
                for j in range(3):
                    if area[i][j] == "_":
                        area[i][j] = uval
                        score .append( self.minimax(area,depth+1, True,aival))
                        area[i][j] = "_"
        return max(score) if ismax else min(score)
    def check_winner(self):
        row1 = "".join(self.area[0])
        row2 = "".join(self.area[1])
        row3 = "".join(self.area[2])
        col1 = "".join([self.area[0][0], self.area[1][0], self.area[2][0]])
        col2 = "".join([self.area[0][1], self.area[1][1], self.area[2][2]])
        col3 = "".join([self.area[0][2], self.area[1][2], self.area[2][2]])
        diagonal1 = "".join([self.area[0][0], self.area[1][1], self.area[2][2]])
        diagonal2 = "".join([self.area[0][2], self.area[1][1], self.area[2][0]])
        winner_positions = [row1, row2, row3, col1, col2, col3, diagonal1, diagonal2]
        if "XXX" in winner_positions:
            return "X"
        elif "OOO" in winner_positions:
            return "O"
        return None

    def print_cells(self):
        print('---------')
        print(f"| {' '.join(self.area[0]).replace('_', ' ')} |")
        print(f"| {' '.join(self.area[1]).replace('_', ' ')} |")
        print(f"| {' '.join(self.area[2]).replace('_', ' ')} |")
        print('---------')


game = TicTacToeGame()
game.start()