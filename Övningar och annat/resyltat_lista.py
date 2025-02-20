def cal_avarage(resultat_lista):
    #res_lista =[23,56,45,76,25,88,48]
    #total = 0
    #for resultat in res_lista: samma som sum funktionen
        #total += resultat
    #total = sum(res_lista)
    #medel=total/len(res_lista)
    #print(round(medel,2))
    return round(sum(resultat_lista)/len(resultat_lista),2)


def fill_in_result():
    res_lista=[]
    while True:
        number = int(input('0 avslutar programet\nMata in olika tal: '))
        res_lista.append(number)
        if number == 0:
            break
    return res_lista

if __name__ == '__main__':
    print(cal_avarage(fill_in_result()))