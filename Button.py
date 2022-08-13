import tkinter as tk

class Button:
    def __init__(self, mine, number, dirtPhoto, grassPhoto, grassFlagPhoto, bombPhoto, minesweeper,bombNEPhoto,badFlag,i,n, bombText):
        self.mine = mine
        self.number = number
        self.dirtPhoto = dirtPhoto
        self.grassPhoto = grassPhoto
        self.grassFlagPhoto = grassFlagPhoto
        self.bombPhoto = bombPhoto
        self.minesweeper = minesweeper
        self.bombNEPhoto = bombNEPhoto
        self.badFlag = badFlag
        self.Flag = False
        self.i = i
        self.n = n
        self.bombText = bombText

    def assignNumber(self):
        if self.minesweeper.playerArray[self.i][self.n] != -1:
            self.button["image"] = self.dirtPhoto
            if self.number == 0:
                return
            elif self.number == 1:
                self.button["fg"]="BLUE"
            elif self.number == 2:
                self.button["fg"]="GREEN"
            elif self.number == 3:
                self.button["fg"]="RED"
            elif self.number == 4:
                self.button["fg"]="blue4"
            elif self.number == 5:
                self.button["fg"]="red4"
            elif self.number == 6:
                self.button["fg"]="cyan3"
            elif self.number == 7:
                self.button["fg"]="purple4"
            elif self.number == 8:
                self.button["fg"]="grey70"
            self.button["text"] = str(self.number)

    def pressButton(self):
        if self.minesweeper.array[self.i][self.n] < 0:
            for i in range(len(self.boardArray)):
                for n in range(len(self.boardArray)):
                    if self.boardArray[i][n].Flag and self.minesweeper.array[i][n] >= 0:
                        self.boardArray[i][n].button["image"] = self.badFlag
                    if self.minesweeper.playerArray[i][n] == -1:
                        self.boardArray[i][n].button["state"] = tk.DISABLED
                    if self.minesweeper.array[i][n] < 0 and not self.boardArray[i][n].Flag:
                        self.boardArray[i][n].button["image"] = self.bombNEPhoto

            self.button["image"] = self.bombPhoto
            return


        self.minesweeper.userInput(self.i,self.n)
        for i in range(len(self.boardArray)):
            for n in range(len(self.boardArray)):
                if self.minesweeper.playerArray[i][n] != -1:
                    self.boardArray[i][n].assignNumber()

    def assignBoard(self, boardArray):
        self.boardArray = boardArray
    def middleClick(self, event):
        if self.Flag:
            self.Flag = False
            self.bombText["text"] = int(self.bombText["text"]) + 1
            self.button["image"] = self.grassPhoto
        else:
            self.button["image"] = self.grassFlagPhoto
            self.Flag = True
            self.bombText["text"] = int(self.bombText["text"]) - 1

    def createButton(self, location):
        self.button = tk.Button(location, fg = "BLACK", text=" ", bg="BLACK", height = 1, width = 1,
                                compound = "center", relief = "groove", command=self.pressButton
                                , image=self.grassPhoto, font = ("Courier",15))
        self.button.bind('<Button-2>', self.middleClick)

