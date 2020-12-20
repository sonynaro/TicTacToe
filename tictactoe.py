# Tic Tac Toe by Sony Narozna

import random           # imports the random module in order to call the randint() function

def createBoard(board): # This function prints the board along with the strings.
    
    print('   |   |')                                             # This is index 0.
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])   # This is a string
    print('   |   |')                                             # This is a string.
    print('-----------')                                          # This is a string.
    print('   |   |')                                             # This is a string.
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])   # This is a string.
    print('   |   |')                                             # This is a string
    print('-----------')                                          # This is a string.
    print('   |   |')                                             # This is a string.
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])   # This is a string.
    print('   |   |')                                             # This is a string.
    # This board is represented by list of 10 strings.


def choosePlayerLetter():                                         # Player may choose whether he or she wishes to be a letter "X" or letter "O".
                                                                    
     # Returns a list with the player’s letter as the 1st item, and the AI agents's letter as 2nd.

     letter = ''

     while not (letter == 'X' or letter == 'O'):

         print('Would you like to be X or O?')

         letter = input().upper()

  # the first element in the list is the player’s letter, the second is the AI agent's letter.

     if letter == 'X':

         return ['X', 'O']

     else:

         return ['O', 'X']


def whoBeginsFirst():

     # Randomly chooses the player(user) who begins first.

     if random.randint(0, 1) == 0:

         return 'computer'

     else:

         return 'player'


def playAgain():

     # This function returns True if and only if the player wants to play again, otherwise it returns False.

     print('Would you like to play again? (yes or no)')

     return input().lower().startswith('y')


def initiateMove(board, letter, move):

     board[move] = letter


def check_if_Winner(board, letter):

     # function returns True if a player has won, given a board and a player’s letter.
     return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
     (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle position
     (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom position
     (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side position
     (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle position
     (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side position
     (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal positions
     (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal positions

def getBoardCopy(board):

     # Make a duplicate of the board list and return it the duplicate.

     dupeBoard = []



     for i in board:

         dupeBoard.append(i)



     return dupeBoard



def isSpaceFree(board, move):

     # Return true if the passed move is free on the passed board.

     return board[move] == ' '



def getPlayerMove(board):

     # Let the player type in their move.

     move = ' '

     while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):

         print('What is your next move? (1-9)')

         move = input()

     return int(move)



def chooseRandomMoveFromList(board, movesList):

     # Returns a valid move from the passed list on the passed board.

     # Returns None if there is no valid move.

     possibleMoves = []

     for i in movesList:

         if isSpaceFree(board, i):

             possibleMoves.append(i)



     if len(possibleMoves) != 0:

         return random.choice(possibleMoves)

     else:

         return None



def getComputerMove(board, computerLetter):

     # Given a board and the computer's letter, determine where to move and return that move.

     if computerLetter == 'X':

         playerLetter = 'O'

     else:

         playerLetter = 'X'



     # Here is our algorithm for our Tic Tac Toe AI:

     # First, check if we can win in the next move

     for i in range(1, 10):

         copy = getBoardCopy(board)

         if isSpaceFree(copy, i):

             initiateMove(copy, computerLetter, i)

             if check_if_Winner(copy, computerLetter):

                 return i



     # Check if the player could win on their next move, and block them.

     for i in range(1, 10):

         copy = getBoardCopy(board)

         if isSpaceFree(copy, i):

             initiateMove(copy, playerLetter, i)

             if check_if_Winner(copy, playerLetter):

                 return i



     # Try to take one of the corners, if they are free.

     move = chooseRandomMoveFromList(board, [1, 3, 7, 9])

     if move != None:

         return move



     # Try to take the center, if it is free.

     if isSpaceFree(board, 5):

         return 5



     # Move on one of the sides.

     return chooseRandomMoveFromList(board, [2, 4, 6, 8])



def isBoardFull(board):

     # Return True if every space on the board has been taken. Otherwise return False.

     for i in range(1, 10):

         if isSpaceFree(board, i):

             return False

     return True


print('Welcome to Tic Tac Toe Game!')


while True:

     # Reset the board

     theBoard = [' '] * 10

     playerLetter, computerLetter = choosePlayerLetter()

     turn = whoBeginsFirst()

     print('The ' + turn + ' will begin first.')

     gameIsPlaying = True



     while gameIsPlaying:

         if turn == 'player':

             # Player’s turn.

             createBoard(theBoard)

             move = getPlayerMove(theBoard)

             initiateMove(theBoard, playerLetter, move)



             if check_if_Winner(theBoard, playerLetter):

                 createBoard(theBoard)

                 print('Excellent! You are the winner!')

                 gameIsPlaying = False

             else:

                 if isBoardFull(theBoard):

                     createBoard(theBoard)

                     print('This game is a tie!')

                     break

                 else:

                     turn = 'computer'



         else:

             # Computer’s turn.

             move = getComputerMove(theBoard, computerLetter)

             initiateMove(theBoard, computerLetter, move)



             if check_if_Winner(theBoard, computerLetter):

                 createBoard(theBoard)

                 print('The computer has won! You lose.')

                 gameIsPlaying = False

             else:

                 if isBoardFull(theBoard):

                     createBoard(theBoard)

                     print('The game is a tie!')

                     break

                 else:

                     turn = 'player'



     if not playAgain():

         break

        