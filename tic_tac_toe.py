import math

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
empty_cells = [(i,j)for i in range(3) for j in range(3)]
rows = 3
cols = 3

def evaluate(board, empty_cells):
    #checking rows
    for i in range(rows):
        if(board[i][0] == board[i][1] == board[i][2]  == 'X'):
            return 1
        
        elif(board[i][0] == board[i][1]  == board[i][2]  == 'O'):
            return -1
        
    #checking cols
    for i in range(cols):
        if(board[0][i] == board[1][i]  == board[2][i]  == 'X'):
            return 1
        
        elif(board[0][i] == board[1][i]  == board[2][i]  == 'O'):
            return -1
        
    #checking diagonals 
    if( board[0][0] == board[1][1]  == board[2][2] == 'X'):
        return 1
    
    elif(board[0][0] == board[1][1] == board[2][2] == 'O'):
        return -1
    
    if( board[2][0] == board[1][1]  == board[0][2] == 'X'):
        return 1
    
    elif(board[2][0] == board[1][1]  == board[0][2] == 'O'):
        return -1
        
    if(len(empty_cells) == 0) :
        return 0
    
    return None

def Minimax (board, depth, is_maximizing, empty_cells):
    score = evaluate(board, empty_cells)
    
    if score !=  None:
        if(score == 1):
            return score   # prioritizing faster wins 
        else:
            return score  # delaying losses or ties 
        
    if len(empty_cells) == 0:
        return 0
        
    
    if is_maximizing :
        best_score = -math.inf
        for (i,j) in empty_cells:
            board[i][j] = 'X' # making a temp move to check game tree
            temp_empty_cells = empty_cells[:]
            temp_empty_cells.remove((i,j))
            best_score = max(best_score, Minimax(board, depth + 1, False, temp_empty_cells))
            board[i][j] = ' ' # undoing the temp move once evaluation is done 
        
        return best_score
        
    else: # same logic just pov of minimizing player so we take min() instead of ,ax()
        best_score = math.inf
        for(i,j) in empty_cells:
            board[i][j] = 'O'
            temp_empty_cells = empty_cells[:]
            temp_empty_cells.remove((i,j))
            best_score = min(best_score, Minimax(board, depth + 1, True, temp_empty_cells))
            board[i][j] = ' '
        
        return best_score
        
def find_best_move(board, empty_cells):
    best_score = -math.inf
    best_move = None

    for (i, j) in empty_cells:
        board[i][j] = 'X'  # temp move to calculate utility
        new_empty_cells = empty_cells[:]
        new_empty_cells.remove((i, j))
        move_score = Minimax(board, 0, False, new_empty_cells)  # recursively calculate the best move using  Minimax
        board[i][j] = ' '  # Undo move

        if move_score > best_score:
            best_score = move_score
            best_move = (i, j)

    return best_move

AI_turn = 1

while True:

        # Print board
        for row in board:
            print('|'.join(row))
        print()

        # Check if game is over
        score = evaluate(board, empty_cells)
        if score is not None:
            if score == 1:
                print("AI (X) wins!")
            elif score == -1:
                print("You (O) win!")
            else:
                print("It's a tie!")
            break
        


        # AI (X) move

        if AI_turn:
            if empty_cells:
                ai_move = find_best_move(board, empty_cells)
                board[ai_move[0]][ai_move[1]] = 'X'
                empty_cells.remove(ai_move)
                AI_turn -= 1
                continue


        # Human (O) move
       
        human_move = tuple(map(int, input("Enter your move (row col): ").split()))
        if human_move in empty_cells:
            board[human_move[0]][human_move[1]] = 'O'
            empty_cells.remove(human_move)
            AI_turn += 1
        else:
            print("Invalid move, try again!")


            
            
        
        