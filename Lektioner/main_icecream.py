# början till kod för .py filen där programmet kommer att köras ifrån:
# 1. öppna json filen
    # 2. lägg till kod try except
    # 3. spara ner innehållet i filen med hjälp av json.load()
    # 4. loopa igenom innehållet och skapa upp ett objekt av klassen för varje varv i loopen spara sedan ner objektet i dictionrayn
    # 5. except: fånga upp json.JSONDecodeError för att fånga upp om det blev något fel från läsningen av data i json filen.

import json
import os
from icecream_class import IceCream

JSON_FILENAME = "icecream_data.json" #konstant


# Funktion för att läsa in glassar från JSON-fil
def load_icecreams():
    """Hämtar glassar från JSON-filen om den finns, annars returnerar en tom dictionary."""
    icecream_dict = {}

    if os.path.exists(JSON_FILENAME):  # kollar om filen finnns
        with open(JSON_FILENAME,'r', encoding=' Utf-8' ) as j_file:
            try:
                icecreams = json.load(j_file) #Retunerar och behöver hämtas upp i en variable
                print(type(icecreams))
                print(icecreams)
                for data in icecreams:
                    icecreams_obj = IceCream( # hämtar vädet från filen J_file
                        data['id_ice'], #id
                        data['name'],
                        data['price']
                    )
                #Spara ner i dictionary iceam_dict lägg in objektet i dictionary.
                #lägga värde på nyckel
                icecream_dict[icecreams_obj.get_id()] =icecreams_obj

            except json.JSONDecodeError:
                print("något gick fel vid läsningen av JSON filen")


    return icecream_dict


# Funktion för att spara glassdictionaryn till JSON-fil
def save_icecreams(icecream_dict):
    """Sparar glassdictionaryn till JSON-filen."""
    data_list = []  # Tom lista för att lagra dictionaries
    # lägg till kod för att loopa igenom värdena i dictionaryn och spara ner i en lista
    for obj in icecream_dict:
        data_list.append(obj.to_dict())
    # öppna sedan json filen för att skriva till den genom att anropa dump() för att skriva till den
    with open (JSON_FILENAME,'w', encoding='utf-8') as file:
        json.dump(data_list, file, indent=4, )
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
        new_cecream = IceCream(new_id, name, price)
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