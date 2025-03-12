
# början till kod för .py filen där programmet kommer att köras ifrån:
import json
import os
from icecream_class
import IceCream

JSON_FILENAME = "icecream_data.json"


# Funktion för att läsa in glassar från JSON-fil
def load_icecreams():
    """Hämtar glassar från JSON-filen om den finns, annars returnerar en tom dictionary."""
    icecream_dict = {}

    if os.path.exists(JSON_FILENAME):  # kollar om filen finnns

    # öppna json filen
    # lägg till kod try except
    # spara ner innehållet i filen med hjälp av json.load()
    # loopa igenom innehållet och skapa upp ett objekt av klassen för varje varv i loopen spara sedan ner objektet i dictionrayn
    # except: fånga upp json.JSONDecodeError för att fånga upp om det blev något fel från läsningen av data i json filen.

    return icecream_dict


# Funktion för att spara glassdictionaryn till JSON-fil
def save_icecreams(icecream_dict):
    """Sparar glassdictionaryn till JSON-filen."""
    data_list = []  # Tom lista för att lagra dictionaries
    # lägg till kod för att loopa igenom värdena i dictionaryn och spara ner i en lista
    # öppna sedan json filen för att skriva till den genom att anropa dump() för att skriva till den

    print("Glasslistan har sparats till fil.")


# Funktion för att lägga till en ny glass
def add_icecream(icecream_dict):
    """Låter användaren lägga till en ny glass i dictionaryn."""
    try:
        # input från användaren
        new_id = max(icecream_dict.keys(), default=0) + 1  # Generera nytt ID
        name = input("Ange glassens namn: ")
        price = float(input("Ange pris (i kronor): "))

        # Skapa objekt
        # lägg till i dictionaryn nyckeln ska vara new_id, värdet ska vara objektet

        print("Ny glass har lagts till!")
    except ValueError:
        print("Ogiltig inmatning. Ange ett nummer för priset.")


# Funktion för att visa alla glassar
def display_icecreams(icecream_dict):
    """Visar alla glassar i listan."""
    if not icecream_dict:
        print("Ingen glass hittades.")
    else:
        print("\nTillgängliga glassar:")
        # loopa igenom glassobjekten och skriv ut dessa


# Meny
def menu():
    """Huvudmeny för att hantera glassar."""
    icecream_dict = load_icecreams()  # Ladda befintliga glassar

    while True:
        print("\n Meny:")
        print("1️. Visa glassar")
        print("2️. Lägg till en ny glass")
        print("3️. Spara glassarna till fil")
        print("4️. Avsluta programmet")

        choice = input("Välj ett alternativ: ")

        if choice == "1":
            display_icecreams(icecream_dict)
        elif choice == "2":
            add_icecream(icecream_dict)
        elif choice == "3":
            save_icecreams(icecream_dict)
        elif choice == "4":
            print("Avslutar programmet...")
            break
        else:
            print("Ogiltigt val, försök igen.")


# Starta programmet
if __name__ == "__main__":
    menu()