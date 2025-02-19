glass_list = ['nogger', 'daimstrut', 'sandwich']

def meny():
    while True:
        match get_choice():
            case 1:
                add_glass_to_list(input('Vilken glass vill du lägga till?'))
            case 2:
                print(glass_list_render(glass_list))
            case 3:
                print(glass_list_render(glass_list))
                remove_glass(input('vilken glass vill du ta bort?'))
            case 4:
                print(f'Antal glassorter: {glass_selections()}')
            case 5:
                break
            case _:
                print('välj ett av det alternativer som finns')

def get_choice():
    choice=5
    try:
        choice = int(input('välj 1: lägga till ny glass,\nvälj 2: skriv ut alla,\nvälj 3: ta bort,\nvälj 4 se antalen\nvälj 5: avsluta program\n'))
    except ValueError:
        print("Error ValueError program shut down")
    except TypeError:
        print("Error TypeError program shut down")
    except KeyboardInterrupt:
        print("Error KeyboardInterrupt program shut down")
    return choice

def glass_selections():
    return len(glass_list)

def remove_glass(choice_glass):
    return glass_list.remove(choice_glass)

def add_glass_to_list(ny_glass):
    return glass_list.append(ny_glass)

def glass_list_render(glass_list_display):
    glass_result=""
    for glass in glass_list_display:
        glass_result+=glass+" "
    return glass_result


if __name__ == '__main__':
    meny()