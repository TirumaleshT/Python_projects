def game_map(game, player = 0, row =0, column = 0, just_display = False):
    if not just_display:
            game[row][column] = player
    print("   0  1  2")
    for index, row in enumerate(game):
        print(index, row)
    return game


def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
    
    #Horizontal
    for row in game:
        if all_same(row):
            print("Player {0} is the Winner horizontally".format(row[0]))
            return True
      
    #veritcal
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[0])
        if all_same(check):
            print("Player {0} is the Winner vertically".format(check[0]))
            return True
            
    #Diagonal
    diag = []
    for i in range(len(game)):
        diag.append(game[i][i])
    if all_same(diag):
        print("player {0} is the winner diagonally (\)".format(diag[0]))
        return True
    
    diag = []
    for col, row in enumerate(reversed(range(len(game)))):
        diag.append(game[row][col])
    if all_same(diag):
        print("player {0} is the winner diagonally (\)".format(diag[0]))
        return True
        

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
players = [1, 2]
iterations = 5
current_players = []
x = 1
for i in range(iterations):
    current_players.append(x)
    x += 1
    current_players.append(x)
    x = 1
    play = True
while play:
    for iternation, current_player in enumerate(current_players):
        print("player{0} turn".format(current_player))
        row_choice = int(input("Enter your row choice: "))
        col_choice = int(input("Enter your column choice: "))
        game = game_map(game, current_player, row_choice, col_choice)
        if win(game):
            again = input("wanna play again:")
            if again.lower() == 'y':
                play = True
                game = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
            else:
                print("Bye!!")
                play = False