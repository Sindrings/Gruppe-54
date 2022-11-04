from datetime import datetime
import sys
lstAvtaler = []
lst_ny = []


def dato():
    d = input("Gi avtaletidspunkt (dd/mm/yy hh:mm):")
    try:
        tidspunkt = datetime.strptime(d, "%d/%m/%y %H:%M")
    except:
        print('Feil i dato. Prøv på nytt.')
        dato()                                #Dersom feil (except), hopp tilbake til start, inntil brukeren taster riktig
    return(tidspunkt)

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

test_e = avtale("Date", "Oslo","11/11/22 17:00", 3600, "Lykke til Kevin")
print(test_e, "\n")

#Oppgave f
def OpprettAvtale():

    avtalen = input("Hva er avtalen? ")
    stedet = input("Hvilket sted? ")
    kategorien = input("Kategori: ")
    
    
    avt = avtale(avtalen, stedet, dato(), tidsrom(), kategorien)
    #avtale_1 = avtale('Posten','Hinna', 1300, 180, 'brev')
    return(avt)
    

#a = opprettavtale()

#Oppgave g
b = avtale("Avtale1","Rom 1", "01/01/11 11:30", 121, "Møte")
lstAvtaler.append(b)
b = avtale("Avtale2","Rom 2", "02/02/22 12:30", 122, "Mat")
lstAvtaler.append(b)
b = avtale("Avtale3","Rom 3", "03/03/33 13:30", 123, "eple")
lstAvtaler.append(b)
b = avtale("Avtale4","Rom 4", "04/04/44 14:30", 124, "Hjem")
lstAvtaler.append(b)

print("\n")

overskrift = input("Overskrift: ")

def ListAlleAvtaler(lst):
    
    if len(overskrift) > 0:
        
        print(overskrift, "\n")

    for i, avt in enumerate (lst):     #avt er avtale som ligger i listen lst og i er index plassering i lst
        print("Index: ", i, avt, '\n')
        
ListAlleAvtaler(lstAvtaler)

#oppgave h
import csv

def SkrivAvtalerTilFil(lst):
    with open('avtale.csv',"w", encoding = "UTF8", newline = "") as f:
        writer = csv.writer(f)
        
        for avt in lst:
            #print(minAvtale)
            writer.writerow([avt.tittel, avt.sted, avt.starttid, avt.varighet, avt.kategori])
    

#Oppgave i
avtaleCSV = r'C:\Users\sindr\Documents\GitHub\avtale.csv'
lstAvtFraFil = []
lstCSV = []
def LesAvtalerFraFil():
        
           
    with open('avtale.csv', "r", encoding = "UTF8") as g:
        lstAvtFraFil = []
        lstCSV = []
        
        lines = g.readlines()
        #print(lines)
        for line in lines:
            #print(line)
            lst_ny = line.split(",")
            #print(type(lst_ny), lst_ny)
            avtale2 = avtale(tittel = lst_ny[0], sted = lst_ny[1], starttid = lst_ny[2], varighet = lst_ny[3], kategori = lst_ny[4].strip())
            lstAvtFraFil.append(avtale2)
    
    return(lstAvtFraFil)
    #print(avtale2)



def SøkAvtaleDato(lst):
    
    lstDatoAvt = []
    dato = SetDato()
    #print(type(dato), dato)

    for avt in lst:
        avt_dato = avt.starttid                             #str, stime = starttid
        avt_dato = datetime.strptime(avt_dato, "%Y-%m-%d %H:%M:%S").date()
        #print(avt_dato, ' - ', dato)

        if avt_dato == dato:
            lstDatoAvt.append(avt)

    if len(lstDatoAvt)>0:
        print("\nAvtaler for ", datetime.strftime(dato, "%d-%m-%Y"),'\n')
    
        for avt in lstDatoAvt:
            print(avt, '\n')
    else:
        print("Ingen avtaler ", dato)

#SøkAvtaleDato(lstAvtaler)

def SetDato():
    d = input("Gi en dato (dd/mm/yy):")
    try:
        dato = datetime.strptime(d, "%d/%m/%y")
        dato = datetime.date(dato)
    except:
        print('Feil i dato. Prøv på nytt.')
        SetDato()

    return(dato)

#Oppgave k
def SearchInString(lst):
    lstSøkIAvt = []

    søkestreng = input("Avtaletittel skal inneholde dette:")
    søkestreng = søkestreng.lower()   #.lower gjør om til små bokstaver (frivillig oppgave k)
    for avt in lst:
        strTittel = avt.tittel
        strTittel = strTittel.lower()
        
        if strTittel.find(søkestreng) > -1 :
            lstSøkIAvt.append(avt)

    if len(lstSøkIAvt)>0:
        print('\n',len(lstSøkIAvt),"avtaler som inneholder", søkestreng,':\n')
    
        for avt in lstSøkIAvt:
            print(avt, '\n')
    else:
        print("Ingen avtaler som inneholder ", søkestreng)

#SearchInString(lstAvtaler)

def PrintMenyValg():
    print('A - Les inn avtaler fra fil')
    print('B - Skriv avtaler til fil')
    print('C - Lag ny avtale')                          #OpprettAvtale
    print('D - Skriv ut alle avtaler')                  #ListAlleAvtaler
    print('E - Søk etter avtale med dato')              #SøkAvtaleDato
    print('F - Søk etter avtale med tekst')             #SearchInString
    print('H - Slett en avtale')                        #SlettAvtaleFraListe
    print('I - Rediger en avtale')                      #SlettAvtaleFraListe
    print('X - Avslutt (exit)')                         #Exit funksjon

def ExitProgram():
    print("Programmet avsluttes")
    sys.exit()

def SlettAvtaleFraListe(lst):
    ListAlleAvtaler(lst)
    idx = input("Velg index som skal slettes:")

    if len(idx) == 0:
        print("Ingen index ble valgt, avslutter.")
    else:
        try:
            idx = int(idx)
            lst.pop(idx)
            ListAlleAvtaler(lst)
        except:
            print("Index må være et heltall som finnes  i listen. Velg funksjonen på nytt for å slette en avtale.")
    return(lst)

def redigerAvtale(lst):
    ListAlleAvtaler(lst)
    idx = input("Velg index som skal editeres:")

    if len(idx) == 0:
        print("Ingen index ble valgt, avslutter.")
    else:
        try:
            idx = int(idx)
            print(lst[idx])
            lst[idx] = OpprettAvtale()
            print("Redigert avtale: ", lst[idx])
              
        except:
            print("Index må være et heltall som finnes  i listen. Velg funksjonen på nytt for å slette en avtale.")
    return(lst)

#Oppgave l
if __name__ == "__main__":

    while (True):

        PrintMenyValg()
        valg = input("Menyvalg (A-I, (X for å avslutte)", "\n")
        valg = valg.upper()
        print("Valgt verdi: ", valg)
        
        if valg == 'A':
            lstAvtaler = LesAvtalerFraFil()
            print("read ", len(lstAvtaler), " records from file")
        elif valg == 'B':
            SkrivAvtalerTilFil(lstAvtaler)
            #clear_output()  #Fjerner output fra cellen
        elif valg == 'C':
            lstAvtaler.append(OpprettAvtale())
            #clear_output()  #Fjerner output fra cellen
        elif valg == 'D':
            #clear_output()  #Fjerner output fra cellen
            ListAlleAvtaler(lstAvtaler)
        elif valg == 'E':
            #clear_output()  #Fjerner output fra cellen
            SøkAvtaleDato(lstAvtaler)
        elif valg == 'F':
            #clear_output()  #Fjerner output fra cellen
            SearchInString(lstAvtaler)
        elif valg == 'X':
            #exit()
            ExitProgram()
        elif valg == 'H':
            lstAvtaler = SlettAvtaleFraListe(lstAvtaler)
            #clear_output()  #Fjerner output fra cellen
        elif valg == 'I':
            #clear_output()  #Fjerner output fra cellen
            lstAvtaler = redigerAvtale(lstAvtaler)
        else:
            print('Velg et gyldig menyvalg:')