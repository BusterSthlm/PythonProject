glass_dict = {'nogger': 15, 'daimstrut':28, 'Cornetto': 24}

print(glass_dict)
#längd
print(len(glass_dict)) # längd på lista

#Hämtar värde --------
#nyckel
print(glass_dict['Cornetto'])
glass_dict['Cornetto'] = 20
print(glass_dict)
#get
print(glass_dict.get('Solero','Glassen finns inte')) #retunerar och behöver hämtas upp i en var.
glass = glass_dict.get('Cornette', 'Glassen finns inte')

#Lägger till värde ---------
glass_dict['sandwich'] = 18
print(glass_dict)
#så man inte skriver över existerande, men lägger till om den inte finns.
glass_dict.setdefault('Cornetto', 23)
print(glass_dict)

for k in glass_dict.keys():
    print(k)

for v in glass_dict.values():
    print(v)

for glass,pris in glass_dict.items():
    print(f'glassen: {glass} kostar: {pris} kr')
print(glass_dict)

print(sum(glass_dict.values()))
# Kollar om det finns i något,
print('88:an' in glass_dict) # Går det att hämta positionen? också

# Ta bort ---
del glass_dict['Cornetto']
print(glass_dict)

Svar = glass_dict.pop('Cornetto', 'finns inte')
print(Svar)
print(glass_dict)
#popItem
print(glass_dict.popitem()) # tar bort den sista och retunerar en tuple
extra_glassar = {'tophat': 8, 'twister': 10}
glass_dict.update(extra_glassar)
print(glass_dict)
glass_dict.clear()
print(glass_dict)


