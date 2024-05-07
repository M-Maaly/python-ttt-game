from tkinter import *
import random

# Initialize the Tkinter window
window = Tk()
window.title("X vs O")

# Label to indicate whose turn it is
label_state = Label(window, text=("Your turn👀"), font=('consolas', 40))
label_state.pack(side="top")

# Function to handle the next turn
def next_turn(row, col):
    global player
    # Check if the cell is empty and no winner has been determined yet
    if cells[row][col]["text"] == "" and not check_winner():
        # Set the player's symbol in the selected cell
        cells[row][col]["text"] = player
        # If the game is not over, switch to the other player's turn
        if not check_winner():
            if player == players[0]:  # If human player's turn
                player = players[1]  # Switch to computer's turn
                label_state.config(text=("Computer's turn👀"))
                computer_move()  # Let computer make a move after human's move
            elif player == players[1]:  # If computer's turn
                player = players[0]  # Switch back to human player's turn
                label_state.config(text=("Your turn👀"))

# Function to handle the computer's move
def computer_move():
    global player
    # If the game is not over
    if not check_winner():
        # Get a list of empty cells
        empty_cells = [(r, c) for r in range(3) for c in range(3) if cells[r][c]["text"] == ""]
        if empty_cells:
            # Randomly select an empty cell and set it to the computer's symbol
            row, col = random.choice(empty_cells)
            cells[row][col]["text"] = players[1]  # Computer plays as "O"
            player = players[0]  # Switch back to human player's turn
            label_state.config(text=("Your turn👀"))
            check_winner()

# Function to check if there's a winner or if the game is tied
def check_winner():
    global player
    # Check rows and columns for a winning combination
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
        
    # Check diagonals for a winning combination
    if cells[0][0]['text'] == cells[1][1]['text'] == cells[2][2]['text'] != "":
        highlight_winner(0, 0, 1, 1, 2, 2)
        update_winner(cells[0][0]['text'])
        return True
    elif cells[0][2]['text'] == cells[1][1]['text'] == cells[2][0]['text'] != "":
        highlight_winner(0, 2, 1, 1, 2, 0)
        update_winner(cells[0][2]['text'])
        return True
        
    # If all cells are filled and no winner, it's a tie
    if not check_empty_spaces():
        update_winner("Tie")
        return True
    else:
        return False 

# Function to highlight the winning combination
def highlight_winner(r1, c1, r2, c2, r3, c3):
    cells[r1][c1].config(bg="cyan")
    cells[r2][c2].config(bg="cyan")
    cells[r3][c3].config(bg="cyan")

# Function to check if there are any empty spaces left
def check_empty_spaces():
    for row in range(3):
        for col in range(3):
            if cells[row][col]['text'] == "":
                return True
    return False

# Function to start a new game
def start_new_game():
    global player
    player = random.choice(players)
    label_state.config(text=("Your turn👀"))

    # Reset all cells and labels
    for row in range(3):
        for col in range(3):
            cells[row][col].config(text="", bg="#f0f0f0")

# Function to update the winner and display the result
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

# Initialize players and game variables
players = ['X', 'O']  # Fixed the order to start with "X"
player = random.choice(players)

player_wins = [0, 0, 0]  # [player, computer, tie]

# Create a 3x3 grid of buttons representing the game cells
cells = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Labels to display game statistics
label_player_wins = Label(window, text="You: 0", font=('consolas', 16))
label_player_wins.pack(side="top")

label_computer_wins = Label(window, text="Computer: 0", font=('consolas', 16))
label_computer_wins.pack(side="top")

label_tie = Label(window, text="Ties: 0", font=('consolas', 16))
label_tie.pack(side="top")

# Button to restart the game
restart_btn = Button(window, text="Restart", font=("consolas", 20), command=start_new_game)
restart_btn.pack(side="top")

# Frame to contain the game cells
btns_frame = Frame(window)
btns_frame.pack()

# Create game cells as buttons
for row in range(3):
    for col in range(3):
        cells[row][col] = Button(btns_frame, text="", font=("consolas", 50), width=4, height=1,
                                 command=lambda row=row, col=col: next_turn(row, col))
        cells[row][col].grid(row=row, column=col)

# Start the Tkinter event loop
window.mainloop()
