# -*- coding: utf-8 -*-

# Programmeringsteknik webbkurs KTH P-uppgift.
# Adam Åsbrink
# 28/2-17
# Det här programmet hanterar enklare minnesanteckningar samt sorterar dessa efter aktuellt datum.
# Programmet är uppdelat i två klasser och ett huvudprogram.
# Ena klassen beskriver en sida ur filofaxen och den andra klassen beskriver själva filofaxen. Funktioner som är oberoende av attribut läggs utanför klasserna. 
# Informationen lagras i filen "day_planner.txt".
# Varje enskild sida kommer ha detta format:
# yyyy-mm-dd: "anteckning"

#----En klass som beskriver en sida inehållandes en anteckning och ett datum----
#   year - det år som minnesanteckningen gäller för
#   month - den månad som minnesanteckningen gäller för
#   day - den dag i månaden som minnesanteckningen gäller för
#   note - anteckningen
#   sorting_variable = det attribut sidorna kommer sorteras efter i listan
class Page:
    
    # Skapar en ny sida med datum och textrad
    def __init__(self, year, month, day, note):
        self.year = year
        self.month = month
        self.day = day
        self.note = note
        self.sorting_variable = (400*int(self.year) + 31*int(self.month) + int(self.day))

    # Returnerar en sträng som beskriver sidan (innehåller datumet och textraden)
    def __str__(self):
        return self.year + "-" + self.month + "-" + self.day + ": " + self.note + "\n" 

#----------En klass som beskriver en filofax-------------------------------------------------
#   pages - en lista som innehåller samtliga sidor ur filofaxen

LINE = "---------------------------------------------------------------" 

class Day_planner():

    # Skapar ett objekt som ska beskriva en filofax
    def __init__(self, pages):
        self.pages = pages

    # En metod som bläddrar framåt till nästa sida i listan och returnerar ordningstalet i listan för utskriven sida.
    def scroll_f(self, page_number):
        if page_number == (len(self.pages)-1): # Skickar felmeddelande när användaren försöker bläddra framåt förbi den sista sidan i listan.
            print("Du befinner dig på den senaste sidan i din filofax och kan därför inte bläddra framåt.\n")
        else:
            page_number += 1
        return page_number

    # En metod som bläddrar bakåt till nästa sida i listan och returnerar ordningstalet i listan för utskriven sida.
    def scroll_b(self, page_number):
        if page_number == 0: # Skickar felmeddelande när användaren försöker bläddra bakåt förbi den första sidan i listan.
            print("Du befinner dig på den tidigaste sidan i din filofax och kan därför inte bläddra bakåt.\n")
        else:
            page_number -= 1
        return page_number

    # Lägger till skapad sida i listan "pages"
    # page - den "sida" som ska läggas till
    def add_to_list(self, page):
        self.pages.append(page)
        return self.pages
        
    # Den här metoden sorterar listan "pages" efter datum
    def sort_list(self):
        self.pages.sort(key = lambda page:page.sorting_variable)
        return self.pages

    # En metod som raderar framtagen sida
    def delete_page(self, page_number):
        print("Är du säker på att du vill radera följande sida:", self.pages[page_number], "\nAnge svar här (ja/nej):", end = " ")
        choice = input()
        if choice.upper().startswith("J"):
            self.pages.remove(self.pages[page_number])
            print("\n" + LINE)
        elif choice.upper().startswith("N"):
            print("\nSidan har inte raderats. Du förs tillbaka till huvudmenyn.\n" + LINE)
        else:
            print("\nKunde inte läsa svar. Du förs tillbaka till huvudmenyn.\n" + LINE)
        return self.pages

    # En metod som visar alla befintliga sidor i listan "pages"
    def show_pages(self):
        for line in self.pages:
            print(line)
        print(LINE)

    # En metod som visar alla befintliga sidor i listan "pages" från angiven månad.
    def show_pages_month(self, read_month):
        print()
        for page in self.pages:
            if read_month == page.month:
                print(page)
        print(LINE)

#----------Funktioner som beskriver textgränssnitt och filhantering-------------

INDENT = "    " # Indrag

# Läser in informationen från den sparade filen och från infomrationen lägger funktionen till Page-objekt till listan pages.
def read_file (filename):
    pages = list()
    with open(filename, "rU", encoding="utf-8") as file:
        for line in file:
            line_parts = line.split(",")
            pages.append(Page(line_parts[0], line_parts[1], line_parts[2], line_parts[3]))
    return pages

# Från listan pages sparar metoden årtal, månad, dag och anteckning med ett kommatecken emellan. Detta för att ge korrekt information till funktionen read_file
def save(filename, pages):
    with open(filename, "w", encoding="utf-8") as file:
        for page in pages:
            saved_page = str(page.year) + "," + str(page.month) + "," + str(page.day) + "," + str(page.note) + ",\n"
            file.write(saved_page)
            
# Skriver ut valmenyn
def menu():
    print("""Huvudmeny:
    Ange "F" för att bläddra framåt.
    Ange "B" för att bläddra bakåt.
    Ange "L" för att lägga till minnesanteckning
    Ange "T" för att ta bort framtagen sida.
    Ange "V" för att visa alla sidor.
    Ange "M" för att visa alla sidor från specifik månad.
    Ange "A" för att avsluta.
    """)

# Läser in och returnerar användarens val från valmenyn
def choose():
    choice = input("Vad vill du göra? ")
    print()
    return choice[0].upper()

#------Här börjar funktioner som beskriver inläsning och felhantering av år, månad, dag och anteckning------

# Läser in och returnerar minnesanteckning för skapande av ny sida/anteckning
def read_note():
    note = input(INDENT + "Ange anteckning här: ")
    return note

# Läser in och returnerar årtal för skapande av ny sida/anteckning
def read_year():
    list_of_year = list()
    number = 2005
    while number < 2026:
        list_of_year.append(str(number))
        number += 1
    variable = False
    while variable == False:
        year = input(INDENT + "Ange årtal som anteckningen gäller för här (xxxx): ")
        for number in list_of_year:
            if number == year:
                variable = True
                return year
        else:
            print("\nProgrammet tar bara emot årtal emellan 2005-2025.\n")

# Läser in och returnerar månad för skapande av ny sida/anteckning. Felhantering för värden utanför 01-12.
# param choice = En bokstav som representerar det val användaren gör i huvudmenyn.
# Eftersom att denna funktion anropas två gånger i programmet för två olika saker behöver input-texten vara olika.
def read_month(choice):
    variable = False
    while variable == False:
        if choice == "M":
            month = input(INDENT + "Ange från vilken enskild månad som sidorna ska visas (xx): ")
        else:
            month = input(INDENT + "Ange månad som anteckningen gäller för här (xx): ")
        months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        for date in months:
            if date == month:
                variable = True
                return month
        print("\nVärdet behöver vara tvåsiffrigt och emellan 01-12.\n")

# Denna funktion returnerar en lista innehållandes alla dagar (i form av nummer) för angiven månad. Denna funktion bestämmer antalet nummer i listan beroende på vilken månad som har angivits.
# param month: värdet för den månad som har angivits av användaren ex. 02 = februari
def days_in_month(month):
    if month == "02":
        days_in_month = list_of_days(28)
        return days_in_month
    elif month == "04" or month == "06" or month == "09" or month == "11":
        days_in_month = list_of_days(30)
        return days_in_month
    else:
        days_in_month = list_of_days(31)
        return days_in_month
        
# Läser in och returnerar dag i månaden för skapande av ny sida/anteckning
# days_in_month: det returnerade värdet från funktionen days_in_month()
def read_day(days_in_month):
    variable = False
    while variable == False:
        day = input(INDENT + "Ange dag i månaden som anteckningen gäller för här (xx): ")
        for d in days_in_month:
            if d == day:
                variable = True
                return day
        print("\nAngivet värde måste vara emellan 01-" + str(len(days_in_month)) + ".\n")

#---------------Kodupprepningar----------------------------------------------

# En funktion som samlar alla funktioner som krävs i skapandet av en sida
# param choice: den bokstav som representerar användarens val i huvudmenyn. Styr input-utskriften för funktionen read_month.
def create_page(choice):
    note = read_note()
    year = read_year()
    month = read_month(choice)
    days = days_in_month(month)
    day = read_day(days)
    page = Page(year, month, day, note)
    print()
    return page

# Denna funktion är en hjälpfunktion till funktionen days_in_month. Den returnerar en lista innehållandes samtliga dagar i angiven månad.
# param last_day_of_month: bestäms av funktionen days_in_month. Är värdet för den sista dagen i angiven månad.
def list_of_days(last_day_of_month):
    days_in_month = ["01", "02", "03", "04", "05", "06", "07", "08", "09"] # Eftersom att dessa värden börjar med 0 är dom svårare att lägga till via en loop
    day_in_month = 10
    while len(days_in_month) < last_day_of_month:
        days_in_month.append(str(day_in_month))
        day_in_month += 1
    return days_in_month

#--------------huvudprogrammet-----------------------------------------------

# Lägger in huvudprogrammet i en egen funktion för att undvika globala variablar
def main():
    print("Välkommen till din filofax, en räddare i vardagen!\n")
    
    FILENAME = "day_planner.txt" # FILENAME - variabel som innehåller filen "day_planner.txt"
    pages = read_file(FILENAME) # metoden read_file läser in filen till listan "pages"
    day_planner = Day_planner(pages)

    page_nr = 0
    choice = ""
    while choice != "A":
        if len(pages) == 0:
            print("Kom igång genom att skapa en anteckning!")
            page = create_page(choice)
            pages = day_planner.add_to_list(page) # Den uppdaterade listan sparas i variabeln "pages"
        print(pages[page_nr])
        menu()
        choice = choose()
        if choice == "F": 
            page_nr = day_planner.scroll_f(page_nr) # Det nya listnumret sparas i variabeln page_nr. Gäller även för metoden "scroll_b"
        elif choice == "B":
            page_nr = day_planner.scroll_b(page_nr) 
        elif choice == "V":
            day_planner.show_pages()
        elif choice == "M":
            month = read_month(choice)
            day_planner.show_pages_month(month)
        elif choice == "T":
            pages = day_planner.delete_page(page_nr) # Den uppdaterade listan sparas i variabeln "pages". Gäller även för metoderna: "add_to_list" och "sort_list"
            if page_nr > 0: 
                page_nr -= 1 # Programmet backar tillbaks till den föregående sidan så länge inte användaren tar bort den första sidan ur listan.
        elif choice == "L":
            page = create_page(choice)
            pages = day_planner.add_to_list(page)
            pages = day_planner.sort_list()
        elif choice == "A":
            save(FILENAME, pages)
            print("Ha en bra dag!")
        else:
            print("Angivet värde finns ej listat.\n")
            
main()
        










    
    
