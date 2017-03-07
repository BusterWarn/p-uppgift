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
        return
    
    #Används i felsökning, printar essentiell information kring objektet
    def __repr__(self):
        return
    
    #Samlar fakta kring cellens grannar, ifall de lever eller är döda.
    def neighboorhood(self, matrix, testing = False):
        return

    #Kollar ifall cellen överlever tills nästa generation.
    def isAlive(self):
        return


#Klass för spelplanen / matrisen.
#xCell: hur många celler matrisen håller i x-ledet.
#yCell: hur många celler matrisen håller i y-ledet.
#cells: lista med nuvarande celler.
#newCells: lista med nästa generations celler.
class matrix:

    #Skapar spelplanen.
    def __init__(self, xCell, yCell):
        return
    
    #Används i felsökning för att printa levande celler i spelplanen. 
    def __repr__(self):
        return
    
    #Printar ut cellerna så att användaren kan se.
    def write(self):
        return

#Fyller upp spelplanen med döda celler.
def initDeadCells(matrix, array):
    return

#Läser av nuvarande generations celler och bestämmer hur nästa generation kommer att se ut.
def newGen(matrix):
    return

#Hämtar användarens filnman.
def getFileName():
    return

#Läser in filen med kordinater för den första generationen celler.
def readFile(matrix, filename):
    return

#Printar ut instruktioner till användaren.
def startGame():
    return

#Printar instruktioner till användaren ifall dem glöms bort.
def help():
    return

#Hämtar användarens nästa drag i ett input.
def userMove():
    return
    

#Huvudprogram
def main():
    return
