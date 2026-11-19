#Class

class tic_tac_toe:
    def __init__(self):
        self.B = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
        self.player = 1

    def get_open_spots(self):
        return [[r,c] for r in range(3) for c in range(3)
                if self.B[r][c]==0]

    def is_valid_move(self,r,c):
        if 0<=r<=2 and 0<=c<=2 and self.B[r][c]==0:
            return True
        print('not a valid move')
        return False

    def make_move(self,r,c):
        if self.is_valid_move(r,c):
            self.B[r][c] = self.player
            self.player = (self.player+2)%2 + 1

    def check_for_winner(self):
        for c in range(3):
            if self.B[0][c]==self.B[1][c]==self.B[2][c]!=0:
                return self.B[0][c]
        for r in range(3):
            if self.B[r][0]==self.B[r][1]==self.B[r][2]!=0:
                return self.B[r][0]
        if self.B[0][0]==self.B[1][1]==self.B[2][2]!=0:
            return self.B[0][0]
        if self.B[2][0]==self.B[1][1]==self.B[0][2]!=0:
            return self.B[2][0]
        if self.get_open_spots()==[]:
            return 0
        return -1

def print_board():
    chars = ['-','X','O']
    for r in range(3):
        for c in range(3):
            print(chars[game.B[r][c]], end=' ')
        print()

#Game Code

y = int(input('Start? yes(1)  '))
scoreboard = {'Player 1':0,
              'Player 2':0,
              'Draws':0}

while y == 1:
    game = tic_tac_toe()
    while game.check_for_winner()==-1:
        print_board()
        r,c = eval(input('Enter spot, player ' + str(game.player) + ': '))
        game.make_move(r,c)

    print_board()

#Score

    x = game.check_for_winner()
    if x==0:
        print("It's a draw.")
        scoreboard['Draws']+=1
    else:
        print('Player', x, 'wins!')
        if x==1:
            scoreboard['Player 1']+=1
        if x==2:
            scoreboard['Player 2']+=1
    print()

    y = int(input('Wanna continue? yes(1)  '))
    print()

#Final Scores

for player, score in scoreboard.items():
    print(player,':',score)
if scoreboard['Player 1']>scoreboard['Player 2']:
    print()
    print('Player 1 wins')
elif scoreboard['Player 1']<scoreboard['Player 2']:
    print()
    print('Player 2 wins')
else:
    print()
    print('it\'s a draw')
input()