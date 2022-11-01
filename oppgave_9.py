from datetime import datetime
lst_avtale = []
lst_ny = []

def dato():
    t = input("avtaletid (dd/mm/yy hh:mm)" )
    #t = '04/06/22 12:24'
    
    try:
        tid = datetime.strptime(t, "%d/%m/%y %H:%M")
        
    except:
        print("Prøv på nytt!")
        dato()
    return(tid)

def tidsrom():
    min = input("Hvor mange minutter? ")
    try:
        min = int(min)
    except:
        print("Prøv på nytt!")
        tidsrom()
    return(min)

#Oppgave d
class avtale:
    def __init__(self, tittel:str, sted:str, starttid, varighet:int, kategori:str):
        self.tittel = tittel
        self.sted = sted
        self.starttid = starttid
        self.varighet = varighet
        self.kategori = kategori

#Oppgave e
    def __str__(self):
        return f' \nAvtale: {self.tittel} \nsted: {self.sted} \nstarttid: {self.starttid} \nvarighet: {self.varighet}min \nkategori: {self.kategori}'

test_e = avtale("TT", "UIS","17:00", 3600, "Fylla")
print(test_e)

def opprettavtale():

    avtalen = input("Hva er avtalen? ")
    stedet = input("Hvilket sted? ")
    kategorien = input("Kategori: ")
    
    
    nyavtale = avtale(avtalen, stedet, dato(), tidsrom(), kategorien)
    #avtale_1 = avtale('Posten','Hinna', 1300, 180, 'brev')
    print(nyavtale)

a = opprettavtale()

b = avtale("Avtale1","Rom 1", "01/01/11 11:30", 121, "Møte")
lst_avtale.append(b)
b = avtale("Avtale2","Rom 2", "02/02/22 12:30", 122, "Mat")
lst_avtale.append(b)
b = avtale("Avtale3","Rom 3", "03/03/33 13:30", 123, "eple")
lst_avtale.append(b)
b = avtale("Avtale4","Rom 4", "04/04/44 14:30", 124, "Hjem")
lst_avtale.append(b)

print("\n")

def skriv_avt(lst):
    overskrift = input("Overskrift: ")
    if len(overskrift) > 0:
        print(overskrift, "\n")

    for i, avt in enumerate (lst):
        print("Index: ", i, avt, '\n')
        
skriv_avt(lst_avtale)

import csv
with open('avtale.csv',"w", encoding = "UTF8", newline = "") as f:
    writer = csv.writer(f)
    
    for minAvtale in lst_avtale:
        print(minAvtale)
        writer.writerow([minAvtale.tittel, minAvtale.sted, minAvtale.starttid, minAvtale.varighet, minAvtale.kategori])

tid = lst_avtale[0].kategori
print(tid)

avtaleCSV = r'C:\Users\sindr\Documents\GitHub\avtale.csv'

with open('avtale.csv', "r", encoding = "UTF8") as g:
    lines = g.readlines()
    #print(lines)
    for line in lines:
        #print(line)

        lst_ny = line.split(",")
        #print(type(lst_ny), lst_ny)
        

        avtale2 = avtale(tittel = lst_ny[0], sted = lst_ny[1], starttid = lst_ny[2], varighet = lst_ny[3], kategori = lst_ny[4].strip())
        print(avtale2)
