
"""
Tic Tac Toe Game using Turtle Graphics
Developed by Melkamu Gebre 
"""
import turtle

# Set up the turtle screen
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Tic Tac Toe By Melkamu Gebre")
screen.setworldcoordinates(-5, -5, 5, 5)
screen.bgcolor('deep sky blue')
screen.tracer(0, 0)
turtle.hideturtle()

# Function to draw the tic tac toe table
def table():
    t.pencolor('indigo')
    t.pensize(5)
    t.up()
    t.goto(-3, -1)
    t.seth(0)
    t.down()
    t.fd(6)
    t.up()
    t.goto(-3, 1)
    t.seth(0)
    t.down()
    t.fd(6)
    t.up()
    t.goto(-1, -3)
    t.seth(90)
    t.down()
    t.fd(6)
    t.up()
    t.goto(1, -3)
    t.seth(90)
    t.down()
    t.fd(6)

# Function to draw the 'O' shape
def player_o(x, y):
    t.up()
    t.goto(x, y - 0.75)
    t.seth(0)
    t.color('black')
    t.down()
    t.circle(0.75, steps=100)

# Function to draw the 'X' shape
def player_x(x, y):
    t.color('white')
    t.up()
    t.goto(x - 0.75, y - 0.75)
    t.down()
    t.goto(x + 0.75, y + 0.75)
    t.up()
    t.goto(x - 0.75, y + 0.75)
    t.down()
    t.goto(x + 0.75, y - 0.75)

# Function to draw the pieces on the board
def piece(a, b, c):
    if c == 0:
        return
    x, y = 2 * (b - 1), -2 * (a - 1)
    if c == 1:
        player_x(x, y)
    else:
        player_o(x, y)

# Function to draw the entire game board
def draw(b):
    table()
    for i in range(3):
        for j in range(3):
            piece(i, j, b[i][j])
    screen.update()

# Function to determine the winner or if there's a tie
def tic_game(b):
    if b[0][0] > 0 and b[0][0] == b[0][1] and b[0][1] == b[0][2]:
        return b[0][0]
    if b[1][0] > 0 and b[1][0] == b[1][1] and b[1][1] == b[1][2]:
        return b[1][0]
    if b[2][0] > 0 and b[2][0] == b[2][1] and b[2][1] == b[2][2]:
        return b[2][0]
    if b[0][0] > 0 and b[0][0] == b[1][0] and b[1][0] == b[2][0]:
        return b[0][0]
    if b[0][1] > 0 and b[0][1] == b[1][1] and b[1][1] == b[2][1]:
        return b[0][1]
    if b[0][2] > 0 and b[0][2] == b[1][2] and b[1][2] == b[2][2]:
        return b[0][2]
    if b[0][0] > 0 and b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        return b[0][0]
    if b[2][0] > 0 and b[2][0] == b[1][1] and b[1][1] == b[0][2]:
        return b[2][0]
    p = 0
    for i in range(3):
        for j in range(3):
            p += (1 if b[i][j] > 0 else 0)
    if p == 9:
        return 3
    else:
        return 0

# Function to handle player's moves
def play(x, y):
    global turn
    i = 3 - int(y + 5) // 2
    j = int(x + 5) // 2 - 1
    if i > 2 or j > 2 or i < 0 or j < 0 or b[i][j] != 0:
        return
    if turn == 'x':
        b[i][j], turn = 1, 'o'
    else:
        b[i][j], turn = 2, 'x'
    draw(b)
    r = tic_game(b)
    if r == 1:
        if screen.textinput("Congratulations!", "Player X won! Play again? (Y/N)").lower() == 'y':
            reset_game()
        else:
            screen.bye()
    elif r == 2:
        if screen.textinput("Congratulations!", "Player O won! Play again? (Y/N)").lower() == 'y':
            reset_game()
        else:
            screen.bye()
    elif r == 3:
        if screen.textinput("The game ended", "Tie! Play again? (Y/N)").lower() == 'y':
            reset_game()
        else:
            screen.bye()

# Function to reset the game
def reset_game():
    global b, turn
    turtle.clear()  # Clear the old game board
    b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    draw(b)
    turn = 'x'

# Initial board setup
b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
draw(b)
turn = 'x'
screen.onclick(play)
turtle.mainloop()
