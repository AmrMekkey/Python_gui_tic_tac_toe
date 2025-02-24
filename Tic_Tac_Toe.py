from customtkinter import *
from tkinter import messagebox


root = CTk()
root.title('Tic Tac Toe')
root.geometry('400x400+400+150')
root.minsize(300,300)
main_frame = CTkFrame(root,fg_color='black',corner_radius=15)
main_frame.pack(expand=True,fill='both',padx=5,pady=5)

current_player = 'X'
board = [['' for _ in range(3)] for _ in range(3)]

def check_win():
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] != '') or (board[0][i] == board[1][i] == board[2][i] != ''):
            return True
    if (board[0][0] == board[1][1] == board[2][2] != '') or (board[0][2] == board[1][1] == board[2][0] != ''):
        return True
    return False

def check_draw():
    for row in board:
        if '' in row:
            return False
    return True

def on_click(row,col):
    global current_player
    if board[row][col] == '':
        board[row][col] = current_player
        buttons[row][col].configure(text=current_player, state='disabled', 
                                    fg_color = 'red' if current_player == 'X' else 'blue', border_width=0)
        if check_win():
            messagebox.showinfo('Game Over',f'Player {current_player} Wins :)')
            reset_board()
        elif check_draw():
            messagebox.showinfo('Game Over','It`s a draw!')
            reset_board()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def reset_board():
    global current_player, board
    current_player = 'X'
    board = [['' for _ in range(3)] for _ in range(3)]
    for r in range(3):
        for c in range(3):
            buttons[r][c].configure(text='',state= 'normal',fg_color='transparent',
                                    border_width=2,hover_color='#875cf5')



buttons = [[None for _ in range(3)] for _ in range(3) ]
for row in range(3):
    for col in range(3):
        button = CTkButton(main_frame,text='',fg_color='transparent',border_color='#875cf5',
                           hover_color='#875cf5',corner_radius=12,width= 100, height=100,
                           border_width=2, font=('helvatica',22),command=lambda r=row, 
                           c=col: on_click(r, c) )
        button.grid(row = row, column = col, padx=5,pady=5)
        buttons[row][col] = button


for i in range(3):
    main_frame.rowconfigure(i,weight=1)
    main_frame.columnconfigure(i,weight=1)



root.mainloop()
