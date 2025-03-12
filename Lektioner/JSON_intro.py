
#Sista uppgiften tillgängllig måndag 17e
"""
filer
- With open behöver man inte stänga filerna.
- with open as f_obj
- Rad för rad = loopa igenom
- om jag inte sätter något läga är default 'r'
-

JSON
- Javascript object Notiation. Är ett populärt format för att lagra och överföra data.
    - Data utbyte mellan olika system
    - lagring av knfogurationsfiler
    - serialiseing och dess deserialiserings av data
    - lagrin av data
    -
    - Load() hämta data
    - Dump() dumpa data

  CSV <-> JSon <-> www...
  - Läsbart format
  - JSON är ingen lista eller dictionary. endast vid omvanlding kna man jobba med det som lista eller dictionary.
  - JSON är inte python specifikt

  JSON Data: objekt
  {
    "namnn123":{
    "värde":"värde"
    }
  }
  Spara ner och kolla genom om det sparas som en lista eller dictionary för att se vad för data det är.
  print(type(JSON_str_my_Menu))

  JSON string
  JSON_Str_My_menu ='{"frukost"}'

! Du måste vara noga med Encoding(ÅÄÖ). När vi öppnar filer måste vi använda UTF_8.
! När vi använder dump() måste vi använda dump(ensure_ascii= False) så åäö kan användas.

Hämta JSON > load
Skriva "dump" JSON . dump()
JSON - json.load(jsonfile)

Dump(dic, file_pointer) # Lägg in dictionary/lista, pointer pekar flr filen som ska öppnas i skriv eller append mode----
om man kör r- och den inte finns skapas den.

data =[]


    with open('data.jsoin', 'w', encoding="ytf-8-sig") as file:
        json.dump(data, file, indent=4, ensure_asci= false)
            #Indent = 4 läsbart format. och indenterar texten med en läsbar struktur.

    try:
    :except - fileNOtFound as err
        print(err)
#kolla vilken typ av data jag får, list eller dict? De fungerar olika.


1. Med str... kan man skriva ut värdna



"""
