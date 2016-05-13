from tpge import *

MAX_TURNS = 10
NUM_OF_TURNS = 0
WHOSE_TURN = 'null'
Cell = 'null'
TOP_LEFT = 0
TOP_MIDDLE = 1
TOP_RIGHT = 2
MIDDLE_LEFT = 3
MIDDLE_MIDDLE = 4
MIDDLE_RIGHT = 5
BOTTOM_LEFT = 6
BOTTOM_MIDDLE = 7
BOTTOM_RIGHT = 8

def initial_state():
    """
    initial_state : State
    Returns the initial state of the game which is the list 
    [[X cells], [O cells]].
    """
    return [[],[]]

def successor_state(S, P):
    """
    successor_state : State x Point -> State
    If S is a state and P is a Point, then successor_state(S,P) is the State
    obtained by clicking on P in S.
    """

    TURN = NUM_OF_TURNS
    Cell = 'null'
    
    if in_top_left_cell(P):
        Cell = TOP_LEFT
    elif in_top_middle_cell(P):
        Cell = TOP_MIDDLE
    elif in_top_right_cell(P):
        Cell = TOP_RIGHT
    elif in_middle_left_cell(P):
        Cell = MIDDLE_LEFT
    elif in_middle_middle_cell(P):
        Cell = MIDDLE_MIDDLE
    elif in_middle_right_cell(P):
        Cell = MIDDLE_RIGHT
    elif in_bottom_left_cell(P):
        Cell = BOTTOM_LEFT
    elif in_bottom_middle_cell(P):
        Cell = BOTTOM_MIDDLE
    elif in_bottom_right_cell(P):
        Cell = BOTTOM_RIGHT

    if TURN % 2 == 0:
        S[0].append(Cell)
    else:
        S[1].append(Cell)

    TURN += TURN
    return S

def game_over(State):
    """
    game_over : State -> Boolean
    If S is a State, then game_over(S) is True if and only if the maximum
    number of turns has been reached in S.
    """
    return NUM_OF_TURNS == MAX_TURNS

def images(S):
    """
    images : State -> Image List
    If S is a State, then images(S) is the list of Images that need to be
    drawn to the screen in order to present the state S to the user. For
    this game the images that need to be drawn are the background and
    the contents of the cells.
    """
    return background() + contents(S)

def game_title():
    """
    game_title : String
    Returns the name of the game which is "TPGE DEMO".
    """
    return "Tic Tac Toe"

def background():
    """
    background : Image List
    Returns the Image List needed to display the background for the game.
    """
    LEFT_BORDER = (170, 400, 170, 100)
    MIDDLE_RIGHT_BORDER = (370, 400, 370, 100)
    MIDDLE_LEFT_BORDER = (270, 400, 270, 100)
    RIGHT_BORDER = (470, 400, 470, 100)
    TOP_BORDER = (170, 400, 470, 400)
    MIDDLE_TOP_BORDER = (170, 300, 470, 300)
    MIDDLE_BOTTOM_BORDER = (170, 200, 470, 200)
    BOTTOM_BORDER = (170, 100, 470, 100)
    return [LEFT_BORDER, MIDDLE_LEFT_BORDER, MIDDLE_RIGHT_BORDER, RIGHT_BORDER, TOP_BORDER, MIDDLE_TOP_BORDER, MIDDLE_BOTTOM_BORDER, BOTTOM_BORDER]

def contents(S):
    """
    contents : State -> Image List
    If S is a state, then contents(S) is the list of Images needed to
    draw the contents of the cells in S.
    """
    NUM_OF_TURNS = 0
    TURN = NUM_OF_TURNS
    TicTacToeContents = []
    if TURN % 2 == 0:
        WHOSE_TURN == 'X'
        TicTacToeContents.append(["X's turn",300,500,15])

        if Cell == TOP_LEFT:
            TicTacToeContents.append([170,400,270,300])
            TicTacToeContents.append([270,400,170,300])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == TOP_MIDDLE:
            TicTacToeContents.append([270,400,370,300])
            TicTacToeContents.append([370,400,270,300])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == TOP_RIGHT:
            TicTacToeContents.append([370,400,470,300])
            TicTacToeContents.append([470,400,370,300])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == MIDDLE_LEFT:
            TicTacToeContents.append([170,300,270,200])
            TicTacToeContents.append([270,300,170,200])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == MIDDLE_MIDDLE:
            TicTacToeContents.append([270,300,370,200])
            TicTacToeContents.append([370,300,270,200])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == MIDDLE_RIGHT:
            TicTacToeContents.append([370,300,470,200])
            TicTacToeContents.append([470,300,370,200])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == BOTTOM_LEFT:
            TicTacToeContents.append([170,200,270,100])
            TicTacToeContents.append([270,200,170,100])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == BOTTOM_MIDDLE:
            TicTacToeContents.append([270,200,370,100])
            TicTacToeContents.append([370,200,270,100])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == BOTTOM_RIGHT:
            TicTacToeContents.append([370,200,470,100])
            TicTacToeContents.append([470,200,370,100])
            NUM_OF_TURNS += NUM_OF_TURNS
            
    elif TURN % 2 == 1:
        WHOSE_TURN == 'O'
        TicTacToeContents.append(["O's turn",300,500,15])

        if Cell == TOP_LEFT:
            TicTacToeContents.append([220,350,20])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == TOP_MIDDLE:
            TicTacToeContents.append([320,350,20])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == TOP_RIGHT:
            TicTacToeContents.append([420,350,20])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == MIDDLE_LEFT:
            TicTacToeContents.append([220,250,20])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == MIDDLE_MIDDLE:
            TicTacToeContents.append([320,250,20])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == MIDDLE_RIGHT:
            TicTacToeContents.append([420,250,20])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == BOTTOM_LEFT:
            TicTacToeContents.append([220,150,20])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == BOTTOM_MIDDLE:
            TicTacToeContents.append([320,150,20])
            NUM_OF_TURNS += NUM_OF_TURNS
        if Cell == BOTTOM_RIGHT: 
            TicTacToeContents.append([420,150,20])
            NUM_OF_TURNS += NUM_OF_TURNS

    print (TicTacToeContents)
    return TicTacToeContents

def in_top_left_cell(P):
    """
    in_left_cell : Point -> Boolean
    If P is a point, then in_top_left_cell(P) is True if and only if P
    is within the top left cell.
    """
    (X,Y) = P
    return 170 <= X <= 270 and 400 <= Y <= 300

def in_top_middle_cell(P):
    """
    in_top_middle_cell : Point -> Boolean
    If P is a point, then in_top_middle_cell(P) is True if and only if P
    is within the top middle cell.
    """
    (X,Y) = P
    return 270 <= X <= 370 and 400 <= Y <= 300

def in_top_right_cell(P):
    """
    in_top_right_cell : Point -> Boolean
    If P is a point, then in_top_right_cell(P) is True if and only if P
    is within the top right cell.
    """
    (X,Y) = P
    return 370 <= X <= 470 and 400 <= Y <= 300

def in_middle_left_cell(P):
    """
    in_middle_left_cell : Point -> Boolean
    If P is a point, then in_middle_left_cell(P) is True if and only if P
    is within the middle left cell.
    """
    (X,Y) = P
    return 170 <= X <= 270 and 300 <= Y <= 200

def in_middle_middle_cell(P):
    """
    in_middle_middle_cell : Point -> Boolean
    If P is a point, then in_middle_middle_cell(P) is True if and only if P
    is within the center cell.
    """
    (X,Y) = P
    return 270 <= X <= 370 and 300 <= Y <= 200

def in_middle_right_cell(P):
    """
    in_middle_right_cell : Point -> Boolean
    If P is a point, then in_middle_right_cell(P) is True if and only if P
    is within the middle right cell.
    """
    (X,Y) = P
    return 370 <= X <= 470 and 300 <= Y <= 200

def in_bottom_left_cell(P):
    """
    in_bottom_left_cell : Point -> Boolean
    If P is a point, then in_bottom_left_cell(P) is True if and only if P
    is within the bottom left cell.
    """
    (X,Y) = P
    return 170 <= X <= 270 and 200 <= Y <= 100

def in_bottom_middle_cell(P):
    """
    in_bottom_middle_cell : Point -> Boolean
    If P is a point, then in_bottom_middle_cell(P) is True if and only if P
    is within the bottom middle cell.
    """
    (X,Y) = P
    return 270 <= X <= 370 and 200 <= Y <= 100

def in_bottom_right_cell(P):
    """
    in_bottom_right_cell : Point -> Boolean
    If P is a point, then in_bottom_right_cell(P) is True if and only if P
    is within the bottom right cell.
    """
    (X,Y) = P
    return 370 <= X <= 470 and 200 <= Y <= 100

if __name__ == "__main__":
    run_game(game_title, initial_state, successor_state, game_over, images)

