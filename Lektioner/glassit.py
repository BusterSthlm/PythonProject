glass_dict = {
    'nogger':26,
    'daimstrut':29,
    'cornetto':23,
    'sandwitch':15
}
while True:
    Icecream_list=""
    for glass,price in glass_dict.items():
        Icecream_list = Icecream_list+"Glass: " + glass +" Price: "+ str(price) +"kr\n"
    choice = input(f"vad för glass av dessa alaternativ vill du ha?\n{Icecream_list}")
    print(f"Du valde {choice} och det kostade {str(glass_dict[choice])}kr\ndu kan betala med swish eller kort betalning\n")

    update_icecream=input("Vilken glass vill du uppdatera?\n")

    for icecream in glass_dict:
        if icecream == update_icecream:
            glass_dict[icecream] = int(input(f"Vilket pris vill du ändra till på {icecream}?\n"))

    ending=input("Vill du stänga av programet skriv då 'Avsluta'!\n")
    if ending == 'Avsluta':
        break