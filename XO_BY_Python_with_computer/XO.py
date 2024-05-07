from tkinter import *
import random

window = Tk()
window.title("X vs O")

label_state = Label(window, text=("Your turn👀"), font=('consolas', 40))
label_state.pack(side="top")


def next_turn(row, col):
    global player
    if cells[row][col]["text"] == "" and not check_winner():
        cells[row][col]["text"] = player
        if not check_winner():
            if player == players[0]:  # If human player's turn
                player = players[1]  # Switch to computer's turn
                label_state.config(text=("Computer's turn👀"))
                computer_move()  # Let computer make a move after human's move
            elif player == players[1]:  # If computer's turn
                player = players[0]  # Switch back to human player's turn
                label_state.config(text=("Your turn👀"))

def computer_move():
    global player
    if not check_winner():
        empty_cells = [(r, c) for r in range(3) for c in range(3) if cells[r][c]["text"] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            cells[row][col]["text"] = players[1]  # Computer plays as "O"
            player = players[0]  # Switch back to human player's turn
            label_state.config(text=("Your turn👀"))
            check_winner()

def check_winner():
    global player
    for row in range(3):
        if cells[row][0]['text'] == cells[row][1]['text'] == cells[row][2]['text'] != "":
            highlight_winner(row, 0, row, 1, row, 2)
            update_winner(cells[row][0]['text'])
            return True
        
    for col in range(3):
        if cells[0][col]['text'] == cells[1][col]['text'] == cells[2][col]['text'] != "":
            highlight_winner(0, col, 1, col, 2, col)
            update_winner(cells[0][col]['text'])
            return True
        
    if cells[0][0]['text'] == cells[1][1]['text'] == cells[2][2]['text'] != "":
        highlight_winner(0, 0, 1, 1, 2, 2)
        update_winner(cells[0][0]['text'])
        return True
    elif cells[0][2]['text'] == cells[1][1]['text'] == cells[2][0]['text'] != "":
        highlight_winner(0, 2, 1, 1, 2, 0)
        update_winner(cells[0][2]['text'])
        return True
        
    if not check_empty_spaces():
        update_winner("Tie")
        return True
    else:
        return False 

def highlight_winner(r1, c1, r2, c2, r3, c3):
    cells[r1][c1].config(bg="cyan")
    cells[r2][c2].config(bg="cyan")
    cells[r3][c3].config(bg="cyan")

def check_empty_spaces():
    for row in range(3):
        for col in range(3):
            if cells[row][col]['text'] == "":
                return True
    return False

def start_new_game():
    global player
    player = random.choice(players)
    label_state.config(text=("Your turn👀"))

    for row in range(3):
        for col in range(3):
            cells[row][col].config(text="", bg="#f0f0f0")

def update_winner(winner):
    if winner == "X":
        player_wins[0] += 1
        label_player_wins.config(text="You Wins: " + str(player_wins[0]))
        label_state['text'] = "You Wins!🔥"
        label_state.pack(side="top")
    elif winner == "O":
        player_wins[1] += 1
        label_computer_wins.config(text="Computer Wins: " + str(player_wins[1]))
        label_state['text'] = "Computer Wins😎🥱"
        label_state.pack(side="top")
    elif winner == "Tie":
        player_wins[2] += 1
        label_tie.config(text="Ties: " + str(player_wins[2]))
        label_state['text'] = "Tie, No Winner🤭"
        label_state.pack(side="top")
        # Change background color of cells to red
        for row in range(3):
            for col in range(3):
                cells[row][col].config(bg="red")



players = ['X', 'O']  # Fixed the order to start with "X"
player = random.choice(players)

player_wins = [0, 0, 0]  # [player, computer, tie]

cells = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


label_player_wins = Label(window, text="You: 0", font=('consolas', 16))
label_player_wins.pack(side="top")

label_computer_wins = Label(window, text="Computer: 0", font=('consolas', 16))
label_computer_wins.pack(side="top")

label_tie = Label(window, text="Ties: 0", font=('consolas', 16))
label_tie.pack(side="top")

restart_btn = Button(window, text="Restart", font=("consolas", 20), command=start_new_game)
restart_btn.pack(side="top")

btns_frame = Frame(window)
btns_frame.pack()

for row in range(3):
    for col in range(3):
        cells[row][col] = Button(btns_frame, text="", font=("consolas", 50), width=4, height=1,
                                 command=lambda row=row, col=col: next_turn(row, col))
        cells[row][col].grid(row=row, column=col)

window.mainloop()
