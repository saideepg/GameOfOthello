## SAIDEEP GUPTA 81128174
## ICS 32
## PROJECT 5
## LAB SEC. 14
## THE WIDTH OF A CIRCLE (PART 2)

import tkinter

## CLASS TO ACCEPT THE USER INPUT BY DISPLAYING A MODAL DIALOG BOX.
## THIS IS CALLED IN THE OTHELLO_GUI MODULE

class OthelloInputDialog:

    def __init__(self):
        '''Sets up the various widgets for the dialog box which accepts the
        user input by calling the following methods'''

        self._make_dialog_window()

        self._make_welcome_label()

        self._make_options_label()

        self._make_row_input()

        self._make_col_input()

        self._make_first_player_input()

        self._make_top_left_input()

        self._make_win_condition_input()

        self._make_buttons()

        self._make_grid_configure()

        self._make_variables()
        

    def _make_dialog_window(self) -> None:
        '''Makes the dialog window to place the widgets in'''

        self._dialog_window = tkinter.Tk()

        self._dialog_window.title('Options')

    def _make_welcome_label(self) -> None:
        '''Makes the welcome label'''

        welcome_label = tkinter.Label(
            master = self._dialog_window,
            text = 'WELCOME TO OTHELLO',
            font = ('Helvetica', 25, 'bold', 'italic'),
            background = 'yellow',)

        welcome_label.grid(
            row = 0, column = 0, padx = 10, pady = 10, columnspan = 2,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

    def _make_options_label(self) -> None:
        '''Makes the optionslabel'''
        
        options_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Choose Your Options', background = 'green',
            font = ('Helvetica', 20, 'bold'))

        options_label.grid(
            row = 1, column = 0, padx = 5, pady = 5, columnspan = 2,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

    def _make_row_input(self) -> None:
        '''Makes the label and the option menu to get the user input for the
        no of rows'''
        
        no_of_rows_label = tkinter.Label(
            master = self._dialog_window,
            text = 'How Many ROWS?',
            font = ('Helvetica', 20))

        no_of_rows_label.grid(
            row = 2, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W)

        no_of_rows = (4, 6, 8, 10, 12, 14, 16)
        self._rows = tkinter.StringVar()
        self._rows.set(no_of_rows[0])

        self._rows_optionmenu = tkinter.OptionMenu(
            self._dialog_window, self._rows, *no_of_rows)

        self._rows_optionmenu.grid(
            row = 2, column = 1, padx = 5, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

    def _make_col_input(self) -> None:
        '''Makes the label and the option menu to get the user input for the
        no of columns'''
        
        no_of_cols_label = tkinter.Label(
            master = self._dialog_window,
            text = 'How Many COLUMNS?',
            font = ('Helvetica', 20))

        no_of_cols_label.grid(
            row = 3, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W)
    
        no_of_cols = (4, 6, 8, 10, 12, 14, 16)
        self._cols = tkinter.IntVar()
        self._cols.set(no_of_cols[0])

        self._cols_optionmenu = tkinter.OptionMenu(
            self._dialog_window, self._cols, *no_of_cols)

        self._cols_optionmenu.grid(
            row = 3, column = 1, padx = 5, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

    def _make_first_player_input(self) -> None:
        '''Makes the label and the option menu to get the user input for the
        first player'''
        
        first_player_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Who Goes FIRST?',
            font = ('Helvetica', 20))

        first_player_label.grid(
            row = 4, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W)

        first_player = ('WHITE', 'BLACK')
        self._first = tkinter.StringVar()
        self._first.set(first_player[0])

        self._first_player_optionmenu = tkinter.OptionMenu(
            self._dialog_window, self._first, *first_player)

        self._first_player_optionmenu.grid(
            row = 4, column = 1, padx = 5, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

    def _make_top_left_input(self) -> None:
        '''Makes the label and the option menu to get the user input for the
        tile in the top left quadruple'''

        top_left_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Top Left Quadruple?',
            font = ('Helvetica', 20))

        top_left_label.grid(
            row = 5, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W)

        top_left = ('WHITE', 'BLACK')
        self._top = tkinter.StringVar()
        self._top.set(top_left[0])

        self._top_left_optionmenu = tkinter.OptionMenu(
            self._dialog_window, self._top, *top_left)

        self._top_left_optionmenu.grid(
            row = 5, column = 1, padx = 5, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        

    def _make_win_condition_input(self) -> None:
        '''Makes the label and the option menu to get the user input for the
        winning condition'''

        win_condition_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Who WINS?',
            font = ('Helvetica', 20))

        win_condition_label.grid(
            row = 6, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W)

        win_condition = ('MAX', 'MIN')
        self._win = tkinter.StringVar()
        self._win.set(win_condition[0])

        self._win_condition_optionmenu = tkinter.OptionMenu(
            self._dialog_window, self._win, *win_condition)

        self._win_condition_optionmenu.grid(
            row = 6, column = 1, padx = 5, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        

    def _make_buttons(self) -> None:
        '''Makes the frame as well as the two buttons to be placed inside
        the frame in order to start the game or cancel it'''

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 7, column = 0, padx = 5, pady = 5, columnspan = 2,
            sticky = tkinter.S + tkinter.E)

        start_button = tkinter.Button(
            master = button_frame,
            text = 'START', font = ('Helvetica', 20),
            command = self._on_start_button)

        start_button.grid(row = 0, column = 0, padx = 5, pady = 5)


        cancel_button = tkinter.Button(
            master = button_frame,
            text = 'CANCEL', font = ('Helvetica', 20),
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 5, pady = 5)
    

    def _make_grid_configure(self) -> None:
        '''Configures the various widgets in the grid'''

        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(1, weight = 1)
        self._dialog_window.rowconfigure(2, weight = 1)
        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.rowconfigure(4, weight = 1)
        self._dialog_window.rowconfigure(5, weight = 1)
        self._dialog_window.rowconfigure(6, weight = 1)
        self._dialog_window.rowconfigure(7, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)
    

    def _make_variables(self) -> None:
        '''Makes the variables to hold the user input'''

        self._start_clicked = False
        self._no_of_rows = 0
        self._no_of_cols = 0
        self._first_player = ''
        self._top_left = ''
        self._win_condition = ''
        

    def show(self) -> None:
        '''This method starts the modal dialog window to accept the user
        input for Othello'''

        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def was_start_clicked(self) -> bool:
        '''This method returns a boolean value depending upon whether the
        start button was clicked or not'''
        return self._start_clicked

    def get_no_of_rows(self) -> int:
        '''This method returns the number of rows that the user selected
        from the option menu of number of rows'''
        return self._no_of_rows

    def get_no_of_cols(self) -> int:
        '''This method returns the number of columns that the user selected
        from the option menu of number of columns'''
        return self._no_of_cols

    def get_first_player(self) -> str:
        '''This method returns the value of first player as selected by the
        user from the option menu of first player'''
        return self._first_player

    def get_top_left(self) -> str:
        '''This method returns the value of tile in top left quadruple as
        selected by the user from the option menu of top left'''
        return self._top_left

    def get_win_condition(self):
        '''This method returns the value of winning condition as selected
        by the user from the option menu of win condition'''
        return self._win_condition
    

    def _on_start_button(self) -> None:
        '''This method sets the start_clicked variable to True and
        appropriately sets the values of rows, columns, first player, top
        left and win condition to the appropriate variable. This even
        destroys the modal dialog box'''
        
        self._start_clicked = True
        
        self._no_of_rows = int(self._rows.get())
        self._no_of_cols = int(self._cols.get())
        self._first_player = self._first.get()
        self._top_left = self._top.get()
        self._win_condition = self._win.get()

        self._dialog_window.destroy()

    def _on_cancel_button(self) -> None:
        '''This method destroys the modal dialog box when the cancel button
        is clicked'''
        self._dialog_window.destroy()


## CLASS TO ASK THE USER IF HE WANTS TO RESTART THE GAME OF OTHELLO BY
## DISPLAYING A MODAL DIALOG BOX. THIS CLASS IS CALLED IN THE OTHELLO_GUI
## MODULE

class RestartDialog:

    def __init__(self):
        '''Sets up the various widgets by calling the following methods'''

        self._make_dialog_window()

        self._make_restart_label()

        self._make_buttons()

        self._make_grid_configure()

        self._make_variable()
        

    def _make_dialog_window(self) -> None:
        '''Makes the dialog window to place the widgets in'''
        
        self._dialog_window = tkinter.Toplevel()

    def _make_restart_label(self) -> None:
        '''Makes the restart label'''
        
        restart_label = tkinter.Label(
            master = self._dialog_window,
            text = 'WANT TO RESTART GAME?',
            background = 'yellow',
            font = ('Helvetica', 25, 'bold'))

        restart_label.grid(
            row = 0, column = 0, padx = 10, pady = 10, columnspan = 2,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

    def _make_buttons(self) -> None:
        '''Makes the frame and the two buttons to place inside the
        frame for the user to select whether he wants to restart the
        game or quit'''
        
        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 1, column = 0, padx = 10, pady = 10, columnspan = 2,
            sticky = tkinter.N + tkinter.S)

        yes_button = tkinter.Button(
            master = button_frame,
            text = 'YES', font = ('Helvetica', 20),
            command = self._on_yes_clicked)

        yes_button.grid(
            row = 0, column = 0, padx = 10, pady = 10)

        no_button = tkinter.Button(
            master = button_frame,
            text = 'NO', font = ('Helvetica', 20),
            command = self._on_no_clicked)

        no_button.grid(
            row = 0, column = 1, padx = 10, pady = 10)

    def _make_grid_configure(self) -> None:
        '''Configures the window for the grid layout'''
        
        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(1, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)

    def _make_variable(self) -> None:
        '''Makes the variable to see whether the yes button was clicked'''
        
        self._yes_clicked = False


    def show(self) -> None:
        '''This method starts the modal dialog box to ask the user whether
        they want to restart the game or not'''

        self._dialog_window.grab_set()
        self._dialog_window.wait_window()


    def was_yes_clicked(self) -> bool:
        '''This method returns the boolean value of whether the yes button
        was clicked or not'''
        return self._yes_clicked

    def _on_yes_clicked(self) -> None:
        '''This method sets the value of the variable yes_clicked to True if
        the yes button was clicked. This method even destroys the modal
        dialog box'''
        self._yes_clicked = True

        self._dialog_window.destroy()

    def _on_no_clicked(self) -> None:
        '''This method destroys the modal dialog box when the no button is
        pressed'''
        self._dialog_window.destroy()




    

        
    
        



        
