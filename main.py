import tkinter as tk
from tkinter import messagebox
from minesweeper import Minesweeper
from Button import Button

def gameWindows(boardSize, bombSize):


    window = tk.Tk()
    window.title("Minesweeper by Andrew Diep")
    grassPhoto = tk.PhotoImage(file='grass.png')
    dirtPhoto = tk.PhotoImage(file='dirt.png')
    grassFlagPhoto = tk.PhotoImage(file='grassFlag.png')
    bombPhoto = tk.PhotoImage(file='bomb.png')
    bombNEPhoto = tk.PhotoImage(file='bombNE.png')
    badFlag = tk.PhotoImage(file='badFlag.png')
    window.option_add("*font", "Courier 14")
    window.configure(bg="grey20")
    window.resizable(False, False)
    boardArray = [[None]*boardSize for _ in range(boardSize)]

    def menu():
        window.destroy()
        userInput()

    def restart():
        window.destroy()
        gameWindows(boardSize, bombSize)

    sideMenu = tk.Label(window, width = 30, height = 50, bg="grey27")
    sideMenu.grid_propagate(0)
    bombText = tk.Label(sideMenu, text = f'{bombSize}', bg = "grey19", fg = "RED", font = ("Courier", 50))
    bombText.place(relx = 0.5, anchor=tk.CENTER, y = 40)
    tk.Label(sideMenu, text=f"Press [Middle Button] \nto flag a spot \n \n \n Size: {boardSize}x{boardSize} \n \n Bombs: {bombSize}", bg = "grey27" ,fg="WHITE", font=("Courier", 15)).place(relx = 0.5, anchor=tk.CENTER, y = 150)
    tk.Button(sideMenu, text="Restart", command=restart).place(relx=0.5, anchor=tk.CENTER, y=250)
    tk.Button(sideMenu,text = "Menu", command = menu).place(relx = 0.5, anchor=tk.CENTER, y = 280)
    tk.Button(sideMenu,text = "Exit", command = window.destroy).place(relx = 0.5, anchor=tk.CENTER, y = 310)
    gameFrame = tk.Label(window, bg="grey20")
    sideMenu.pack(side = tk.LEFT)


    board = Minesweeper(boardSize,int(bombSize))


    for i in range(boardSize):
        for n in range(boardSize):
            cell = Button(False, board.array[i][n], dirtPhoto, grassPhoto, grassFlagPhoto, bombPhoto, board,bombNEPhoto, badFlag,i,n, bombText)
            cell.createButton(gameFrame)
            cell.button.grid(row=i,column=n)
            boardArray[i][n] = cell
    for i in range(boardSize):
        for n in range(boardSize):
            boardArray[i][n].assignBoard(boardArray)

    gameFrame.pack(side = tk.RIGHT)

    window.mainloop()

def userInput():
    user = tk.Tk()
    user.title("Minesweeper by Andrew Diep")
    def changeLabel(event):
        size = textInput.get()
        cLabel['text'] = f'Size: {size}x{size}'
    user.configure(bg="grey20")
    user.geometry('300x350')
    user.resizable(False, False)
    l = tk.Label(user, text = "Minesweeper", bg = "grey20", fg = "WHITE",font=("Courier", 30))
    l.place(relx=0.5,anchor=tk.CENTER, y=30)
    l = tk.Label(user, text="By Andrew Diep", bg="grey20", fg="WHITE", font=("Ariel", 20))
    l.place(relx=0.5, anchor=tk.CENTER, y=60)

    l = tk.Label(user, text="What is the size of the minefield?\n Maximum size = 30 x 30", bg="grey20", fg="WHITE", font=("Courier", 14))
    l.place(relx=0.5, anchor=tk.CENTER, y=90)

    cLabel = tk.Label(user, text="Size: _ x _", bg="grey20", fg="WHITE", font=("Courier", 14))
    cLabel.place(relx=0.5, anchor=tk.CENTER, y=120)
    textInput = tk.Entry(bg="grey80", fg="BLACK", width = 3)
    textInput.place(relx=0.5, anchor=tk.CENTER, y=150)
    textInput.bind("<KeyRelease>", changeLabel)

    def changeBLabel(event):
        size = textMines.get()
        bLabel['text'] = f'Size: {size}'
    l = tk.Label(user, text = "How many mines?", bg = "grey20", fg = "WHITE",font=("Courier", 14))
    l.place(relx=0.5, anchor=tk.CENTER, y=210)
    bLabel = tk.Label(user, text="Size: _", bg="grey20", fg="WHITE", font=("Courier", 14))
    bLabel.place(relx=0.5, anchor=tk.CENTER, y=230)
    textMines = tk.Entry(user, bg="grey80", fg="BLACK", width = 3)
    textMines.place(relx = 0.5, anchor=tk.CENTER, y = 260)
    textMines.bind("<KeyRelease>", changeBLabel)

    def playGame():
        mapSize = str(textInput.get())
        bombSize = str(textMines.get())
        if not mapSize.isdigit() or not bombSize.isdigit():
            messagebox.showerror("Data Type Error", "Please enter an Integer")
            return
        if int(mapSize)*int(mapSize) <= int(bombSize):
            messagebox.showerror("Size Error","Bomb size is too big")
            return
        if int(mapSize) < 5:
            messagebox.showerror("Size Error", "Please enter a bigger size for the map")
            return
        if int(mapSize) > 30:
            messagebox.showerror("Size Error", "Please enter a smaller size for the map")
            return
        user.destroy()
        gameWindows(int(mapSize), bombSize)

    buttonPlay = tk.Button(user, bg = "grey10", fg = "BLACK", text="Play!", command = playGame)
    buttonPlay.place(relx = 0.5, anchor=tk.CENTER, y = 300)
    user.mainloop()
#gameWindows(30,150)
userInput()
