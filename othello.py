## SAIDEEP GUPTA 81128174
## ICS 32
## PROJECT 5
## LAB SEC. 14
## THE WIDTH OF A CIRCLE (PART 2)


### EXCEPTION CLASSES (RAISED WHENEVER REQUIRED BY GAME LOGIC)

class InvalidOthelloGameMove(Exception):
    '''Raised whenever a player attempts to make an invalid move'''
    pass

class GameBoardLocationUnEmpty(Exception):
    '''Raised when a player tries to put disk at an unempty location'''
    pass

class NoValidMovesLeft(Exception):
    '''Raised when a player has no valid moves left on the game board'''
    pass

class OthelloGameOver(Exception):
    '''Raised when both the players have no valid moves left and the game
    is over'''
    pass


### CLASS FOR GAME LOGIC

class PlayOthello:

    def __init__(self, num_row, num_col, top_left, first_player,
                 win_condition):
        '''Initializes all the attributes of the class'''

        self._board_row = self._require_valid_row_number(num_row)
        self._board_col = self._require_valid_col_number(num_col)
        self._top_left = self._require_valid_player(top_left)
        self._player = self._require_valid_player(first_player)
        self._win_condition = self._require_valid_win_condition(win_condition)

        self._white = ' W '
        self._black = ' B '
        self._NONE = ' . '
        
        self._board = self.new_board()


    def new_board(self) -> [[str]]:
        '''Constructs and returns a new game board for the game Othello'''

        board = []

        for row in range(self._board_row):
            board.append([])
            for col in range(self._board_col):
                board[-1].append(self._NONE)


        if self._top_left == 'W':
            
            board[(self._board_row - 2)//2][(self._board_col - 2)//2] \
                                   = self._white
            board[(self._board_row - 2)//2 + 1][(self._board_col - 2)//2 + 1] \
                                   = self._white
            board[(self._board_row - 2)//2][(self._board_col - 2)//2 + 1] \
                                   = self._black
            board[(self._board_row - 2)//2 + 1][(self._board_col - 2)//2] \
                                   = self._black
            
        else:
            
            board[(self._board_row - 2)//2][(self._board_col - 2)//2] \
                                   = self._black
            board[(self._board_row - 2)//2 + 1][(self._board_col - 2)//2 + 1] \
                                   = self._black
            board[(self._board_row - 2)//2][(self._board_col - 2)//2 + 1] \
                                   = self._white
            board[(self._board_row - 2)//2 + 1][(self._board_col - 2)//2] \
                                   = self._white
            
        return board



    def get_tile_position(self, row: int, col: int) -> str:
        '''Returns the tile at the row and column number in the game board'''

        return (self._board[row][col])
    


    def drop_piece(self, row: int, col: int) -> None:
        '''Takes a row and column, checks whether the player's move is valid
        at that location and if it is inserts the player's tile at that
        location and flips the corresponding tiles. If the move is invalid
        it raises an error'''

        flip = []
        
        flip.extend(self.check_and_flip(row, col))

        self._board[row - 1][col - 1] = ' ' + self._player + ' '

        for index in flip:
            self._board[index[0]][index[1]] = ' ' + self._player + ' '


        self._player = self._opposite_player()


    def check_all_board(self) -> None:
        '''Checks whether any valid moves are left or not, for both the
        players and raises errors appropriately'''
        
        if self.check_all_valid() == []:
            self._player = self._opposite_player()
            
            if self.check_all_valid() == []:
                raise OthelloGameOver
            
            else:
                raise NoValidMovesLeft
        


    def check_all_valid(self) -> list:
        '''Checks whether a player has any valid moves left on the game
        board, by calling the method check_and_flip on every empty location
        on the game board, and depending upon the result appropriately
        raise errors or returns a list of all valid moves'''
        
        flip = []

        for row in range(self._board_row):
            for col in range(self._board_col):

                if self._board[row][col] == self._NONE:

                    try:
                        flip.extend(self.check_and_flip(row + 1, col + 1))
                    except:
                        continue

        return flip
            
    

    def check_and_flip(self, row: int, col: int) -> list:
        '''Checks whether the move, that a player is trying to make, is
        valid or not, by calling the method _flip 8 times, thereby
        checking the validity of the move in all 8 directions'''

        if self._board[row-1][col-1] == self._NONE:

            flip = []

            flip.extend(self._flip(row, col, 0, 1))
            flip.extend(self._flip(row, col, 1, 1))
            flip.extend(self._flip(row, col, 1, 0))
            flip.extend(self._flip(row, col, 1, -1))
            flip.extend(self._flip(row, col, 0, -1))
            flip.extend(self._flip(row, col, -1, -1))
            flip.extend(self._flip(row, col, -1, 0))
            flip.extend(self._flip(row, col, -1, 1))


            if len(flip) == 0:
                raise InvalidOthelloGameMove
        
            return flip
    
        else:
            raise GameBoardLocationUnEmpty


        
    def _flip(self, row: int, col: int, rowdelta: int, coldelta: int) -> list:
        '''Checks whether the move that a player is trying to make is valid
        but only in one direction, depending upon the values of rowdelta and
        cosdelta, that it gets'''

        row = row - 1
        col = col - 1

        opp = self._opposite_player()

        flip = []

        while True:

            row = row + rowdelta
            col = col + coldelta

            if -1 < row < self._board_row and -1 < col < self._board_col:

                if self._board[row][col].strip() == opp:
                    flip.append([row, col])
                elif self._board[row][col].strip() == self._player:
                    break
                else:
                    flip = []
                    break

            else:
                flip = []
                break

        return flip



    def winner_othello(self) -> str:
        '''Determines and returns the winner of the game depending upon
        the winning condition as desired by the user'''

        no_black_tiles = self.count_tiles()[0]
        no_white_tiles = self.count_tiles()[1]

        winner = ''

        if self._win_condition.upper() == 'MAX' :
            if no_black_tiles > no_white_tiles:
                winner = 'B'
            elif no_white_tiles > no_black_tiles:
                winner = 'W'

        else:
            if no_black_tiles < no_white_tiles:
                winner = 'B'
            elif no_white_tiles < no_black_tiles:
                winner = 'W'

        return winner
    


    def count_tiles(self) -> list:
        '''Counts and returns the number of tiles of each player on the game
        board at a specific instant'''

        black = 0
        white = 0

        for row in range(self._board_row):
            for col in range(self._board_col):
                if self._board[row][col].strip() == 'W':
                    white += 1
                elif self._board[row][col].strip() == 'B':
                    black += 1

        return [black, white]
        

    def _opposite_player(self) -> str:
        '''Returns the opposite player to the input'''

        if self._player == 'W':
            return 'B'
        return 'W'



    ### FUNCTIONS / METHODS TO CHECK FOR ERRONEOUS INPUT ###


    def _require_valid_row_number(self, row: int) -> int:
        '''Checks whether the inputted row number is valid or not'''

        if type(row) != int or not self._is_valid_row_number(row):
            raise ValueError("row number must be an even integer between \
4 and 16")

        return row

    def _require_valid_col_number(self, col: int) -> int:
        '''Checks whether the inputted column number is valid or not'''

        if type(col) != int or not self._is_valid_col_number(col):
            raise ValueError("column number must be an even integer between \
4 and 16")

        return col

    def _require_valid_player(self, player: str) -> str:
        '''Checks whether the inputted player is valid or not'''

        if (type(player) != str) or (player not in ['W', 'B']):
            raise ValueError("player needs to be of string type with \
value 'W' or 'B'")

        return player

    def _require_valid_win_condition(self, win_condition: int) -> int:
        '''Checks whether the inputted winning condition is valid or not'''
        
        if (type(win_condition) != str) or (win_condition.upper() not in \
                                            ['MAX', 'MIN']):
            raise ValueError("win condition needs to be of str type with \
value MAX or MIN")

        return win_condition
                             
    
    def _is_valid_row_number(self, row: int) -> bool:
        '''This function checks whether the row is a valid number or not;
        the row needs to be an even integer between 4 and 16'''

        return row % 2 == 0 and 4 <= row <= 16

    def _is_valid_col_number(self, col: int) -> bool:
        '''This function checks whether the column is a valid number or not;
        the column needs to be an even integer between 4 and 16'''

        return col % 2 == 0 and 4 <= col <= 16

    
        
    
        
