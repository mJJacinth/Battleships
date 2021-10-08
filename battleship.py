"""
Battleship Project
Name:
Roll No:
"""

from warnings import resetwarnings
import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random
import math

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    
    data["rows"]=10
    data["columns"]=10
    data["boardsize"]=500
    data["cellsize"]=data["boardsize"]/data["rows"]
    data["computerboard"]=emptyGrid(data["rows"],data["columns"])
    data["userboard"]=emptyGrid(data["rows"],data["columns"])
    #data["userboard"]=test.testGrid()
    data["numShips"]=5
    addShips(data["computerboard"],data["numShips"])
    data["tempships"]=[]
    data["numberoftempships"]=0
    data["winner"]=None
    data["maxnumofturns"]=50
    data["currentnumofturns"]=0
    return


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data, compCanvas,data["computerboard"],False)
    drawGrid(data, userCanvas, data["userboard"],True)
    drawShip(data,userCanvas,data["tempships"])
    # drawGameOver(data,compCanvas)
    drawGameOver(data,userCanvas)
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    if data["winner"]==None:
        cell=getClickedCell(data,event)
        if board == "user":
            clickUserBoard(data,cell[0],cell[1])
        elif board=="comp":
            if (data["numShips"])==5:
                # cell=getClickedCell(data,event)
                runGameTurn(data,cell[0],cell[1])
    return


#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols): 
    Grid1 = [] 
    for r in range(rows): 
        Grid1.append([]) 
        for c in range(cols):
            Grid1[r].append(EMPTY_UNCLICKED)
    return Grid1


   


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    rows=random.randint(1,8) 
    columns=random.randint(1,8) 
    j=random.randint(0,1) 
    if j==0: 
        ship=[[rows-1,columns],[rows,columns],[rows+1,columns]] 
    else:
        ship=[[rows,columns-1],[rows,columns],[rows,columns+1]] 
    return ship

    


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for r in range(0,3): 
        if grid[ship[r][0]][ship[r][1]]==EMPTY_UNCLICKED: 
            pass
        else: 
            return False 
    return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    count=0 
    while(count<numShips): 
        ship=createShip() 
        outcome=checkShip(grid,ship) 
        if(outcome==True): 
            i=0
            while (i<3): 
                grid[ship[i][0]][ship[i][1]]=SHIP_UNCLICKED 
                i=i+1
            count = count+ 1 
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):#drawgrid
    for row in range(data["rows"]):
        for cols in range(data["columns"]):
            if grid[row][cols]==SHIP_UNCLICKED:
                canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],data["cellsize"]+cols*data["cellsize"], row*data["cellsize"]+data["cellsize"], fill="yellow")
            elif grid[row][cols]==EMPTY_UNCLICKED:
                canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],data["cellsize"]+cols*data["cellsize"], row*data["cellsize"]+data["cellsize"], fill="blue")
            elif grid[row][cols]==SHIP_CLICKED:
                canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],data["cellsize"]+cols*data["cellsize"], row*data["cellsize"]+data["cellsize"], fill="red")
            elif grid[row][cols]==EMPTY_CLICKED:
                canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],data["cellsize"]+cols*data["cellsize"], row*data["cellsize"]+data["cellsize"], fill="white")
            if showShips==False:
                if grid[row][cols]==SHIP_UNCLICKED:
                     canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],data["cellsize"]+cols*data["cellsize"], row*data["cellsize"]+data["cellsize"], fill="blue")
            

    return


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''

def isVertical(ship):
    if ship[0][1]==ship[1][1]==ship[2][1]:
        sorted_ship =sorted(ship)
        if sorted_ship[0][0]+1== sorted_ship[1][0] and sorted_ship[1][0]+1==sorted_ship[2][0]:
           return True
    return False
   


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    if ship[0][0]==ship[1][0]==ship[2][0]:
        sorted_ship=sorted(ship)
        if sorted_ship[0][1]+1== sorted_ship[1][1] and sorted_ship[1][1]+1==sorted_ship[2][1]:
            return True
    return False


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    row=math.floor(event.y/data["cellsize"])
    col=math.floor(event.x/data["cellsize"])
    return [row,col]



'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for i in range(len(ship)):
        canvas.create_rectangle(ship[i][1]*data["cellsize"],ship[i][0]*data["cellsize"],ship[i][1]*data["cellsize"]+data["cellsize"],ship[i][0]*data["cellsize"]+data["cellsize"],fill="white")
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if len(ship)==3:
        if checkShip(grid,ship):
            if isVertical(ship):
                return True
            elif isHorizontal(ship):
                return True
    return False


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if shipIsValid(data["userboard"],data["tempships"]):
        for i in data["tempships"]:
            data["userboard"][i[0]][i[1]]=SHIP_UNCLICKED
        data["numberoftempships"]=data["numberoftempships"]+1
    else:
        print("SHIP IS NOT VALID")
    data["tempships"]=[]
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["numberoftempships"]==5:
        return
    if [row,col] in data["tempships"]:
        return
    data["tempships"].append([row,col])
    if (len(data["tempships"]))==3:
        placeShip(data)
    if data["numberoftempships"]==5:
        print("start the game")
    
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if board[row][col]==SHIP_UNCLICKED:
        board[row][col]=SHIP_CLICKED
    if board[row][col]==EMPTY_UNCLICKED:
        board[row][col]=EMPTY_CLICKED
    if isGameOver(board)== True:
        data["winner"]=player
        return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    if data["computerboard"][row][col]== SHIP_CLICKED or data["computerboard"][row][col]==EMPTY_CLICKED:

        return
    else:
        updateBoard(data,data["computerboard"],row,col,"user")
    result=getComputerGuess(data["userboard"])
    updateBoard(data,data["userboard"],result[0],result[1],"comp")
    data["currentnumofturns"]= data["currentnumofturns"]+1
    if data["currentnumofturns"]==data["maxnumofturns"]:
        data["winner"]="draw"
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):

    while True:
        rows=random.randint(0,9) 
        columns=random.randint(0,9) 
        if board[rows][columns]==SHIP_UNCLICKED or board[rows][columns]==EMPTY_UNCLICKED:
            return [rows,columns]
    return


'''board
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for i in range(0,10):
        for c in range(0,10):
            if board[i][c] == SHIP_UNCLICKED:
                return False
    return True


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if data["winner"]=="user":
        canvas.create_text(250,250, text="CONGRATULATIONS", fill="grey", font=('Helvetica 25 bold'))
    elif data["winner"]=="comp": 
        canvas.create_text(250,250, text="YOU LOST", fill="grey", font=('Helvetica 25 bold'))
    elif data["winner"]=="draw":
        canvas.create_text(250,250, text="OUT OF MOVES", fill="grey", font=('Helvetica 25 bold'))
    return



### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
    #test.testIsGameOver()