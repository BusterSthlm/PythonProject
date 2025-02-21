import math


def area_cirkel(radie=0.0):
    return math.pi * radie ** 2


def area_rektangel(langd=0.0, bredd=0.0):
    return langd * bredd

#Kalla existerande def från ovan.
def area_triangel(basen=0.0, hojden=0.0):
    #
    return area_rektangel(basen,hojden)/2


def area_kvadrat(sida=0.0):
    return sida ** 2

print(f"area av cirkeln: {area_cirkel(10):.2f}")

print(f"Area av rektangel: {area_rektangel(10):.2f}")
print(f"Area av triangel")