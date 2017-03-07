#P-uppgift: 122 Game of Life and DEATH - Prototyp
#Författare: Buster Hultgren Wärn
#Senast uppdaterad: 2017-03-03

#Program som simulerar John Conways (antar att det är John Conway) "Game of Life".
#Först läser programmet av en fil med den första generationen celler, och skapar upp cellerna som objekt.
#Programmet simulerar följande generation celler genom att läsa av de nuvarande och applicera spelets regler på dem.


#Klass för varje cell som kommer att skapas.
#x: cellens x-kordinat
#y: cellens y-kordinat
#neighbourds: en lista av cellens grannar som antingen är levande eller döda
#alive: värde på ifall cellen lever eller är död
import copy

class cell:

    #Skapar en ny cell.
    def __init__(self, x, y, status):
        self.x = x
        self.y = y
        self.neighbors = 8 * ["dead"]
        self.alive = status

    #Används i felsökning, printar essentiell information kring objektet
    def __repr__(self):
        return("x: " + str(self.x) + " y: " + str(self.y) + " - " + str(self.alive))
    
    #Samlar fakta kring cellens grannar, ifall de lever eller är döda.
    def neighboorhood(self, matrix, testing = False):
        checkCell = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
            ]
        i = 0
        while i < len(checkCell):
            yValue = self.y + checkCell[i][0]
            xValue = self.x + checkCell[i][1]
            if yValue > 0 and yValue < len(matrix.cells) and xValue > 0 and xValue < len(matrix.cells):
                self.neighbors[i] = matrix.cells[yValue][xValue].alive
            else:
                self.neighbors[i] = "dead"
            i += 1

    #Kollar ifall cellen överlever tills nästa generation.
    def isAlive(self):
        aliveCells = 0
        for cell in self.neighbors:
            if cell == "alive":
                aliveCells += 1
        if self.alive == "alive":
            if aliveCells < 2:
                return "dead"
            elif aliveCells < 4:
                return "alive"
            else:
                return "dead"
        else:
            if aliveCells == 3:
                return "alive"
            else:
                return "dead"


#Klass för spelplanen / matrisen.
#xCell: hur många celler matrisen håller i x-ledet.
#yCell: hur många celler matrisen håller i y-ledet.
#cells: lista med nuvarande celler.
#newCells: lista med nästa generations celler.
class matrix:

    #Skapar spelplanen.
    def __init__(self, xCell, yCell):
        self.xCell = xCell
        self.yCell = yCell
        self.cells = [[None] * xCell for _ in range(yCell)]
        self.newCells = [[None] * xCell for _ in range(yCell)]
    
    #Används i felsökning för att printa levande celler i spelplanen. 
    def __repr__(self):
        i = 0
        for y in self.cells:
            for x in self.cells[i]:
                if x.alive == "alive":
                    print(x)
            i += 1
        return("Bazinga!")
    
    #Printar ut cellerna så att användaren kan se.
    def write(self):
        i = 0
        for y in self.cells:
            print(i, end=" ")
            for x in self.cells[i]:
                if x.alive == "alive":
                    print("X", end=" ")
                else:
                    print("-", end=" ")
            i += 1
            print("\n")

#Fyller upp spelplanen med döda celler.
def initDeadCells(matrix, array):
    x = 0
    y = 0
    while y < matrix.yCell:
        while x < matrix.xCell:
            if array == 0:
                matrix.cells[y][x] = cell(x, y, "dead")
            else:
                matrix.newCells[y][x] = cell(x, y, "dead")
            x += 1
        
        x = 0
        y += 1
    #obj.newCells = list(obj.cells)

#Läser av nuvarande generations celler och bestämmer hur nästa generation kommer att se ut.
def newGen(matrix):
    i = 0
    
    for y in matrix.cells:
        for cell in matrix.cells[i]:
            if cell.alive == "alive":
                cell.neighboorhood(matrix, True)
            else:
                cell.neighboorhood(matrix)
            matrix.newCells[i][cell.x].alive = cell.isAlive()
        i += 1
    
    matrix.cells = copy.deepcopy(matrix.newCells)
    matrix.write()

#Hämtar användarens filnman.
def getFileName():
    return input("What is the name of your file called with your starting cells (for example: 'cells.txt')\n")

#Läser in filen med kordinater för den första generationen celler.
def readFile(matrix, filename):
    with open(filename, "r") as file:
        for line in file:
            row = [int(cordinate) + 1 for cordinate in line.split()]
            matrix.cells[row[1]][row[0]] = cell(row[0], row[1], "alive")

#Printar ut instruktioner till användaren.
def startGame():
    print("GAME OF LIFE AND DEATH \n\nFor rules about this game, research John Conway's 'Game of Life'\n")
    print("You need to insert a txt file with the cordinates for starting cells in the same folder that you run this program from. The file should have this format:\n \nx y\nx y\nx y\n")
    print("Note that the cordinates can be max 15 for both y and x. Your entered cells will be displayed below")
    print("Your commands are: 'H' - for help, 'Q' - for quitting and blank for viewing the next generation")

#Printar instruktioner till användaren ifall dem glöms bort.
def help():
    print("Rules and information for this game: https://en.wikipedia.org/wiki/Conway's_Game_of_Life")
    print("Your commands are: 'H' - for help, 'Q' - for quitting and blank for viewing the next generation")
    print("You need to insert a txt file with the cordinates for starting cells in the same folder that you run this program from. The file should have this format:\n \nx y\nx y\nx y\n")

#Hämtar användarens nästa drag i ett input.
def userMove():
    return input("For viewing the next generation; enter blank, for quiting; enter Q, for help; enter H\n").upper()
    

#Huvudprogram
def main():
    startGame()
    filename = getFileName()
    
    matrix1 = matrix(17, 17)
    initDeadCells(matrix1, 0)
    initDeadCells(matrix1, 1)
    readFile(matrix1, filename)
    matrix1.write()

    userAnswer = userMove()

    while userAnswer != "Q":
        if userAnswer == "":
            initDeadCells(matrix1, 1)
            newGen(matrix1)
        elif userAnswer == "H":
            help()
        else:
            print("unknown command, please try again")
        userAnswer = userMove()
    print("Good bye!")

main()
