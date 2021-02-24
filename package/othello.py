import numpy as np

class Player:
    
    def __init__(self, turn, name):
        self.turn = turn
        self.name = name
    
    def set_disc(self):
        input_str = input().split(',')
        return input_str[0], input_str[1]
    
    def say_my_turn(self):
        print(f'============== {self.name} turn ==============')
        
    
class Board:
    
    borad = np.array([['-' for i in range(8)] for j in range(8)])
    disc1 = '@'
    disc2 = '*'
    
    def __init__(self):
        self.borad[3,3] = self.disc1
        self.borad[3,4] = self.disc2
        self.borad[4,3] = self.disc2
        self.borad[4,4] = self.disc1
    
    @property
    def settable_coordinate(self):
        pass
    
    def show_board(self):
        print(self.borad)

    def show_board_settable(self):
        pass
        
    def set_disc(self):
        pass
        
    def reverse_disc(self):
        pass
    


def execute(board: Board, player1: Player, player2: Player):
    while(True):
    
        for player in [player1, player2]:
            player.say_my_turn()
            player.set_disc()
            board.show_board()
            
        break
    
    
if __name__ == '__main__':

    execute(Board(), 
            Player('先行', 'Shota'), 
            Player('後行', 'Takashi'))
