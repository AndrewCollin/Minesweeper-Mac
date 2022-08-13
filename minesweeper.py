import random
class Minesweeper:
    array = []
    copyArray = []
    playerArray = []
    size = 0

    def __init__(s, a):
        s.copyArray = a
        s.size = len(a)
        s.MinesweeperPrepare()
        s.playerArray = [[-1]*s.size for _ in range(s.size)]

    def __init__(s,size,bomb):
        s.copyArray = s.randomGen(size,size,bomb)
        s.size = len(s.copyArray)
        s.MinesweeperPrepare()
        s.playerArray = [[-1] * s.size for _ in range(s.size)]

    def randomGen(s,x,y,total):
        randArray = [[False] * x for _ in range(x)]
        r = random
        for i in range(total):
            numX = r.randint(0, x-1)
            numY = r.randint(0, y-1)
            if (randArray[numX][numY]):
                i-=1
                continue
            randArray[numX][numY] = True
        return randArray


    def userInput(s, i, n):
        if i == -1 or i == s.size or n == s.size or n == -1:
            return
        if s.playerArray[i][n] != -1:
            return
        if s.array[i][n] > 0:
            s.playerArray[i][n] = s.array[i][n]
            return
        if s.array[i][n] < 0:
            print("Didn't catch that error")
            return
        s.playerArray[i][n] = s.array[i][n]
        s.userInput(i+1, n)
        s.userInput(i+1, n+1)
        s.userInput(i+1, n-1)
        s.userInput(i, n+1)
        s.userInput(i, n-1)
        s.userInput(i-1, n)
        s.userInput(i-1, n+1)
        s.userInput(i-1, n-1)
        return


    def defineBoard(s):
        for i in range(s.size):
            for n in range(s.size):
                if s.array[i][n] < 0:
                    nI, pI, nN, pN = 1,1,1,1
                    if i == 0:
                        nI = 0
                    if i == s.size - 1:
                        pI = 0
                    if n == 0:
                        nN = 0
                    if n == s.size - 1:
                        pN = 0

                    s.array[i + pI][n] += pI
                    s.array[i + pI][n + pN] += pI * pN
                    s.array[i + pI][n - nN] += pI * nN
                    s.array[i][n + pN] += pN
                    s.array[i][n - nN] += nN
                    s.array[i - nI][n] += nI
                    s.array[i - nI][n + pN] += nI * pN
                    s.array[i - nI][n - nN] += nI * nN

    def MinesweeperPrepare(s):
        s.array = [[0]*s.size for x in range(s.size)]
        for i in range(s.size):
            for n in range(s.size):
                if s.copyArray[i][n]:
                    s.array[i][n] = -9
        s.defineBoard()



    def printBoard(s, array):
        size = len(array)
        for x in range(size):
            print()
            for n in range(size):
                if array[x][n] < 0:
                    print("E" + " ", end="")
                else:
                    print(str(array[x][n]) + " ", end="")
