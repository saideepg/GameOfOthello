## SAIDEEP GUPTA 81128174
## ICS 32
## PROJECT 5
## LAB SEC. 14
## THE WIDTH OF A CIRCLE (PART 2)

import tkinter
import othello_input
import othello
import random
import point
import sys


## CLASS TO PLAY OTHELLO. THIS CLASS CONTAINS THE VARIOUS WIDGETS AND
## METHODS NECESSARY TO DISPLAY THE OTHELLO GUI. THIS CLASS INTERACTS
## WITH THE GAME LOGIC AS WELL AS THE OTHELLO_INPUT MODULES AND CALLS THE
## APPROPRIATE METHODS AND VARIABLES IN ORDER TO MAKE THE GAME RUN SMOOTHLY

class OthelloGUI:

    def __init__(self):
        '''Initializes the various widgets of the application, as well as
        accepts user inputs by calling other classes, by making calls to
        the following methods'''

        self._make_input_dialog()

        self._make_root_window()

        self._make_canvas()

        self._make_canvas_bind_events()

        self._make_welcome_label()

        self._make_player_label()

        self._make_move_label()

        self._make_score_labels()

        self._make_quit_button()

        self._configure_grid()

        
    def start(self) -> None:
        '''This method starts the game of othello and puts the application
        into the mainloop'''
        self._root_window.mainloop()

    def _make_root_window(self) -> None:
        '''Makes the root window for the application and sets the title of
        window'''

        self._root_window = tkinter.Tk()
        self._root_window.title('GAME OF OTHELLO')
        

    def _make_input_dialog(self) -> None:
        '''Makes an object of class OthelloInputDialog and calls the
        appropriate methods to accept user input in the form of a modal
        dialog box. Further calls a mathod to make a new game state of
        the game'''

        input_dialog = othello_input.OthelloInputDialog()
        input_dialog.show()

        if input_dialog.was_start_clicked():
            
            rows = input_dialog.get_no_of_rows()
            cols = input_dialog.get_no_of_cols()
            
            first = input_dialog.get_first_player()
            if first == 'WHITE':
                first = 'W'
            else:
                first = 'B'
                
            top_left = input_dialog.get_top_left()
            if top_left == 'WHITE':
                top_left = 'W'
            else:
                top_left = 'B'
                
            win = input_dialog.get_win_condition()

        else:
            sys.exit(1)

        self._make_new_game_state(rows, cols, top_left, first, win)


    def _make_new_game_state(self, rows: int, cols: int, top_left: str,
                             first: str, win: str) -> None:
        '''Makes an object of the class PlayOthello thereby making a new
        game state'''
        
        self._state = othello.PlayOthello(rows, cols, top_left, first, win)


    def _make_canvas(self) -> None:
        '''Makes the canvas'''
        
        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = 500, height = 500,
            background = 'green')

        self._canvas.grid(
            row = 2, column = 1, padx = 10, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

    def _make_canvas_bind_events(self) -> None:
        '''Binds events to the canvas'''

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_button_clicked)

        
    def _make_welcome_label(self) -> None:
        '''Makes a welcome label in the root window'''

        label_welcome = tkinter.Label(
            master = self._root_window, text = 'OTHELLO', underline = 7,
            background = 'yellow', font = ('Helvetics', 30, 'bold'))

        label_welcome.grid(
            row = 0, column = 1, padx = 10, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

    def _make_player_label(self) -> None:
        '''Makes a new label in the root window the player whose turn it is
        will be displayed'''

        self._player = tkinter.StringVar()

        self._label_player = tkinter.Label(
            master = self._root_window, textvariable = self._player,
            background = 'magenta', font = ('Helvetica', 25, 'italic', 'bold'))

        self._label_player.grid(
            row = 1, column = 1, padx = 10, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        

    def _make_move_label(self) -> None:
        '''Makes a new label in the root window. This label is basically my
        way ( or the game's way) of interacting with the user by displaying
        appropriate messages when required'''

        self._move = tkinter.StringVar()
        
        self._label_move = tkinter.Label(
            master = self._root_window, textvariable = self._move,
            background = 'cyan', font = ('Helvetica', 20))

        self._label_move.grid(
            row = 3, column = 1, padx = 10, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        

    def _make_score_labels(self) -> None:
        '''Makes two new labels in the root window to display the current
        scores of both the players'''

        self._black_tiles = tkinter.StringVar()
        self._white_tiles = tkinter.StringVar()

        self._label_black_tiles = tkinter.Label(
            master = self._root_window, textvariable = self._black_tiles,
            background = 'red', font = ('Helvetica', 30))
        
        self._label_black_tiles.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W,
            rowspan = 5)

        self._label_white_tiles = tkinter.Label(
            master = self._root_window, textvariable = self._white_tiles,
            background = 'red', font = ('Helvetica', 30))

        self._label_white_tiles.grid(
            row = 0, column = 2, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W,
            rowspan = 5)


    def _make_quit_button(self) -> None:
        '''Makes a new button in the root window. This button can be pressed
        any time by the user to quit or restart the game'''
        
        self._quit_button = tkinter.Button(
            master = self._root_window, text = 'QUIT / RESTART',
            font = ('Helvetica', 20, 'bold'), background = 'black',
            command = self._quit)

        self._quit_button.grid(
            row = 4, column = 1, padx = 5, pady = 5, 
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        

    def _configure_grid(self) -> None:
        '''Configures the layout of the various widgets on the grid'''
        
        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.rowconfigure(1, weight = 0)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.rowconfigure(3, weight = 0)
        self._root_window.rowconfigure(4, weight = 0)
        self._root_window.columnconfigure(0, weight = 0)
        self._root_window.columnconfigure(1, weight = 1)
        self._root_window.columnconfigure(2, weight = 0)
        

    def _quit(self) -> None:
        '''This method is called by the quit button. This method starts the
        the restart dialog box, asking the user whether they want to restart
        or not. On the basis of the choice, does the appropriate thibg'''
        dialog = othello_input.RestartDialog()
        dialog.show()

        self._root_window.destroy()

        if dialog.was_yes_clicked():
            OthelloGUI().start()

        else:
            
            sys.exit(1)
        

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''This method draws the current state of the othello game board
        whenever the window is resized'''

        self._player.set('Player ' + self._state._player)

        self._black_tiles.set(' BLACK : \n' + \
                                    str(self._state.count_tiles()[0]))
        self._white_tiles.set(' WHITE : \n' + \
                                    str(self._state.count_tiles()[1]))
        
        self._draw_othello_board()
        

    def _on_button_clicked(self, event: tkinter.Event) -> None:
        '''This method is called whenever there is a click on the game board.
        Basically this method is the key stone of the GUI. This method
        appropriately determines in what row and column the click was made
        and then interacts with the game logic, checking the validity of the
        move made as well as handling all the errors raised by the game
        logic including game over, invalid move, or no valid moves left'''

        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        click_point = point.from_pixel(event.x, event.y,
                                       canvas_width, canvas_height)


        x, y = click_point.frac()

        row_click = int(y * self._state._board_row)
        col_click = int(x * self._state._board_col)
            

        try:

            self._state.drop_piece(row_click + 1, col_click + 1)
            rand_num = random.randrange(3)

            if rand_num == 0:
                self._move.set('GOOD JOB')
            elif rand_num == 1:
                self._move.set('EXCELLENT MOVE')
            else:
                self._move.set('NICE WORK')
                

        except othello.InvalidOthelloGameMove:
            self._move.set('INVALID MOVE. NO POSSIBLE FLIPS')
            

        except othello.GameBoardLocationUnEmpty:
            self._move.set('INVALID MOVE. LOCATION UNEMPTY')
            

        self._draw_othello_board()

        self._player.set('PLAYER ' + self._state._player)

        self._black_tiles.set(' BLACK : \n' + \
                                    str(self._state.count_tiles()[0]))
        self._white_tiles.set(' WHITE : \n' + \
                                    str(self._state.count_tiles()[1]))

        try:

            self._state.check_all_board()

        except othello.OthelloGameOver:
            self._move.set('GAME OVER. NO VALID MOVES. PRESS QUIT')
            winner = self._state.winner_othello()
            if winner == 'W':
                self._player.set('CONGRATS. WINNER IS PLAYER WHITE')
            elif winner == 'B':
                self._player.set('CONGRATS. WINNER IS PLAYER BLACK')
            else:
                self._player.set('SORRY. NO ONE WON. GAME DRAW')
                             
        except othello.NoValidMovesLeft:
            self._player.set('PLAYER ' + self._state._player)
            self._move.set('TURN REVERT. NO VALID MOVES FOR PLAYER ' \
                           + self._state._opposite_player())


    def _draw_othello_board(self) -> None:
        '''This method draws the Othello Game Board by calling other
        methods'''

        self._width_tile = 1 / self._state._board_col
        self._height_tile = 1 / self._state._board_row

        self._canvas.delete(tkinter.ALL)
        
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        
        self._draw_horizontal_lines(canvas_width, canvas_height)
        self._draw_vertical_lines(canvas_width, canvas_height)
        self._draw_all_tiles(canvas_width, canvas_height)


    def _draw_horizontal_lines(self, canvas_width, canvas_height) -> None:
        '''This method draws the horizontal lines on the canvas'''
        
        for i in range(self._state._board_row + 1):

            point_left = point.from_frac(0, i * self._height_tile)
            point_right = point.from_frac(canvas_width, i * self._height_tile)

            x1, y1 = point_left.pixel(canvas_width, canvas_height)
            x2, y2 = point_right.pixel(canvas_width, canvas_height)
            
            self._canvas.create_line(x1, y1, x2, y2)
            

    def _draw_vertical_lines(self, canvas_width, canvas_height) -> None:
        '''This method draws the vertical lines on the canvas'''
        
        for j in range(self._state._board_col + 1):

            point_top = point.from_frac(j * self._width_tile, 0)
            point_bottom = point.from_frac(j * self._width_tile, canvas_height)

            x1, y1 = point_top.pixel(canvas_width, canvas_height)
            x2, y2 = point_bottom.pixel(canvas_width, canvas_height)

            self._canvas.create_line(x1, y1, x2, y2)


    def _draw_all_tiles(self, canvas_width, canvas_height) -> None:
        '''This method interacts with the game logic and draws all the tiles,
        black or white, wherever the current game state has them'''    
        
        for row in range(self._state._board_row):
            for col in range(self._state._board_col):

                top_left_point = point.from_frac(
                    (col * self._width_tile) + 0.01,
                    (row * self._height_tile) + 0.01)
                
                bottom_right_point = point.from_frac(
                    ((col + 1) * self._width_tile) - 0.01,
                    ((row + 1) * self._height_tile) - 0.01)

                x1, y1 = top_left_point.pixel(canvas_width, canvas_height)
                x2, y2 = bottom_right_point.pixel(
                    canvas_width, canvas_height)
                
                if self._state.get_tile_position(row, col).strip() == 'B':
                    self._canvas.create_oval(
                        x1, y1, x2, y2, fill = 'black')

                elif self._state.get_tile_position(row, col).strip() == 'W':
                    self._canvas.create_oval(
                        x1, y1, x2, y2, fill = 'white', outline = 'white')

                    
## THIS FINALLY EXECUTES AND STARTS THE APPLICATION                    

if __name__ == '__main__':

    OthelloGUI().start()
