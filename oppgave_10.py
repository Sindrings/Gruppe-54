from datetime import date, time


class Avtale:
    def __init__(self, tittel, sted, dato, tid, varighet, personer):
        self.tittel = tittel
        self.sted = sted
        self.tid = tid
        self.dato = dato
        self.varighet = varighet
        self.personer = personer
        self.kategorier = []

    def __str__(self):
        return f"Avtale: {self.tittel}  klokken: {self.tid} den {self.dato} skal {self.personer} møte på {self.sted.gateadresse} med varighet {self.varighet}. Avtalen har kategoriene: {self.kategorierString()}"

    def kategorierString(self):
        result = ""
        for kategori in self.kategorier:
            result = result + f" navn: {kategori.navn} id: {kategori.id}"
        return result

    def legg_til_kategori(self, kategori):
        self.kategorier.append(kategori)


def skrivListe(liste, overskrift=""):
    if (not overskrift == ""): print("_____" + overskrift + "_____")
    for i in range(len(liste)):
        print(f"\t{i}   {liste[i]}")


# region get input functions
def tryint(prompt):
    try:
        return int(input(prompt))
    except:
        print("Verdien du skrev inn kunne ikke leses som et tall.")
        if (input("Prøv igjen? [y/n]: ").lower()[0] == "y"): return tryint(prompt)
        return 0


def trydate(prompt):
    try:
        args = input(prompt).split('-')
        return date(int(args[0]), int(args[1]), int(args[2]))
    except:
        print("Verdien du skrev inn kunne ikke leses som en dato.")
        if (input("Prøv igjen? [y/n]: ").lower()[0] == "y"): return trydate(prompt)
        return 0


def trytime(prompt):
    try:
        args = input(prompt).split(':')
        return time(int(args[0]), int(args[1]))
    except:
        print("Verdien du skrev inn kunne ikke leses som en dato.")
        if (input("Prøv igjen? [y/n]: ").lower()[0] == "y"): return trydate(prompt)
        return 0


# endregion

# region Create/edit h-j)
def _lagAvtale():
    avtaleListe.append(lagAvtale())


def lagAvtale():
    print("Du skriver nå en ny avtale:")
    return Avtale(input("Tittel: "), nyttsted(), trydate("Dato (yyyy-mm-dd): "), trytime("Tid (hh:mm): "),
                  tryint("Varighet (minutter): "), input('Personer: '))


def velgAvtale():
    if (len(avtaleListe) == 0): return -1
    try:
        i = int(input(f"Velg en avtale [0-{len(avtaleListe) - 1}]: "))
    except:
        return velgAvtale("Angitt verdi ikke gjenkjent som heltall. Prøv igjen: ")
    if (i < 0):
        return 0
    if (i >= len(avtaleListe)):
        return len(avtaleListe) - 1
    return i


def _endreAvtale(i=-1):
    if i == -1: i = velgAvtale()
    if i == -1: return
    p = [
        f"Tittel: {avtaleListe[i].tittel}",
        f"Sted: {avtaleListe[i].sted}",
        f"Dato: {avtaleListe[i].dato}",
        f"Tid: {avtaleListe[i].tid}",
        f"Varighet: {avtaleListe[i].varighet}min",
        f"Personer: {avtaleListe[i].personer}",
        f"Legg til kategori",
        "Lagre og gå ut"
    ]
    for j in range(len(p)):
        print(str(j + 1) + " " + p[j])
    j = int(input("Endre eller gå ut [1-8]: ")) - 1

    if j == 0:
        avtaleListe[i].tittel = input("Ny tittel: ")
    elif j == 1:
        avtaleListe[i].sted = input("Nytt sted: ")
    elif j == 2:
        avtaleListe[i].date = trydate("Ny dato [yyyy-: ")
    elif j == 3:
        avtaleListe[i].date = trydate("Ny tid [hh:mm]: ")
    elif j == 4:
        avtaleListe[i].varighet = tryint("Ny varighet: ")
    elif j == 5:
        avtaleListe[i].personer = input("Nye personer: ").split(',')
    elif j==6:
        if len(kategoriliste) == 0:
            print("ingen kategorier funnet")
        for kategori in kategoriliste:
            if (input(f"Legg til kategori: {kategori.navn}? [y/n]: ").lower() == "y"):
                avtaleListe[i].legg_til_kategori(kategori)

    if not j == 7: _endreAvtale(i)


def _slettAvtale():
    i = velgAvtale()
    if i == -1: return
    print(f"Du har valgt avtale {i}:\n\t{avtaleListe[i]}")
    if input("Ønsker du å slette? [y/n]: ").lower() == "y":
        del avtaleListe[i]


def _avtaleDetaljer():
    i = velgAvtale()
    if i == -1: return
    print(f"Avtale {i}:\n\t{avtaleListe[i]}")


# endregion

# region read/write file
def _lagreAvtaleListe():
    lagreAvtaleListe(avtaleListe, input("Destinasjonsfil: "))


def lagreAvtaleListe(avtaler, destinasjonsfil="mine avtaler.txt"):
    result = ""
    for a in avtaler:
        for p in [a.tittel, str(a.sted.id),  a.sted.navn, a.sted.gateadresse, str(a.sted.postnr), a.sted.poststed, str(a.dato), str(a.tid), str(a.varighet), str(a.personer)]:
            result += p + ","
        for kategori in a.kategorier: result += str(kategori.id) + ";" + str(kategori.navn) + ";" + str(kategori.prioritet) + ","
        result = result[:-1] + "\n"
    f = open(destinasjonsfil, "w")
    f.write(result)
    f.close()


def _lesAvtaleListeFraFil():
    for avtale in lesAvtaleListeFraFil(input("Les fra fil: ")):
        avtaleListe.append(avtale)


def lesAvtaleListeFraFil(fil):
    f = open(fil, "r")
    tekst = f.read()
    f.close()
    avtaler = []
    for avtale in tekst.split('\n'):
        args = avtale.split(',')
        if (len(args) < 4): continue
        dato = args[6].split('-')
        tid = args[7].split(':')

        nyavtale = Avtale(args[0], Sted(args[1], args[2], args[3], args[4], args[5]),
               date(int(dato[0]), int(dato[1]), int(dato[2])),
               time(int(tid[0]), int(tid[1]), int(tid[2])), int(args[8]), int(args[9]))
        for i in range(len(args[10:])):
            id, navn, prio = args[10+i].split(";")
            nyavtale.legg_til_kategori(Kategori(id, navn, prio))
        avtaler.append(nyavtale)
    return avtaler


# endregion

# region search functions
def avtalerGittDato(avtaleListe, dato):
    return søkAvtaler(avtaleListe, lambda avtale: date == avtale.date)


def avtalerGittTittel(avtaleListe, tittel):
    return søkAvtaler(avtaleListe, lambda avtale: tittel in avtale.tittel)


def _søkAvtaler():
    a = input("Søkeord: ")
    kriterie = lambda avtale: a in (avtale.tittel + avtale.sted)
    resultater = søkAvtaler(avtaleListe, kriterie)
    skrivListe(resultater, f"Ditt søk ga {len(resultater)} resultater")


def søkAvtaler(avtaleListe, condition):
    result = []
    for avtale in avtaleListe:
        if condition(avtale): result.append(avtale)
    return result

def _finnmedsted():
    counter = 0
    string = ""
    for sted in stedliste:
        string = string + f"Index {counter}: sted: {sted.navn} med id {sted.id} "
        counter +=1
    print(string)
    index = int(input(f"velg et sted med index [0:{counter-1}]: "))
    for avtale in avtaleListe:
        if avtale.sted == stedliste[index]:
            print(avtale)
    input("")



# endregion

def meny():
    print(f"Avtaleboka mi: ({len(avtaleListe)})")
    if (len(avtaleListe) == 0):
        print("\tDu har ikke lagd noen avtaler enda.")
    else:
        skrivListe(avtaleListe)
    if (len(kategoriliste) == 0):
        print("\tDu har ikke lagd noen kategorier enda.")
    else:
        skrivListe(kategoriliste)
    if (len(stedliste) == 0):
        print("\tDu har ikke lagd noen steder enda.")
    else:
        skrivListe(stedliste)

    handlinger = ["Lag ny avtale",
                  "Lag ny kategori",
                  "Lag nytt sted",
                  "Les inn avtaler fra fil",
                  "Skriv avtaler til fil",
                  "Søk i avtaler",
                  "Avslutt"]
    funksjoner = [_lagAvtale, _lagKategori, _lagSted, _lesAvtaleListeFraFil, _lagreAvtaleListe, _søkAvtaler, lambda: None]

    # Hvis vi ikke har noen avtaler enda, er det ikke vits å vise disse handlingene til brukeren.
    if (len(avtaleListe) > 0):
        handlinger.insert(1, "Endre avtale")
        handlinger.insert(2, "Slett avtale")
        handlinger.insert(3, "Se avtaledetaljer")
        handlinger.insert(4, "Finn avtale med sted")
        funksjoner.insert(1, _endreAvtale)
        funksjoner.insert(2, _slettAvtale)
        funksjoner.insert(3, _avtaleDetaljer)
        funksjoner.insert(4, _finnmedsted)

    for i in range(len(handlinger)):
        print(f"{str(i + 1)}: {handlinger[i]}")
    i = int(input(f"Velg en handling [1-{len(handlinger)}]: ")) - 1
    funksjoner[i]()
    if (not handlinger[i] == "Avslutt"): meny()

class Kategori:
    def __init__(self, id, navn, prioritet = 1):
        self.id = id
        self.navn = navn
        self.prioritet = prioritet

    def __str__(self):
        return f"Kategori id: {self.id}, navn: {self.navn}, prioritet: {self.prioritet}"

def _lagKategori():
    kategoriliste.append(nykategori())

def nykategori():
    return Kategori(int(input("Kategori id:")), input("Kategori navn:"), int(input("Kategori prioritet:")))

def lestkategorifrafil(path):
    f = open(path, "r")
    lines = f.readlines()
    kategorier = []
    for line in lines:
        id, navn, prio = line.split(";")
        kategorier.append(Kategori(id, navn, prio))
    f.close()
    return kategorier

class Sted:
    def __init__(self, id, navn, gateadresse, postnr, poststed ):
        self.id = id
        self.navn = navn
        self.gateadresse = gateadresse
        self.postnr = postnr
        self.poststed = poststed

    def __str__(self):
        return f"id: {self.id}, navn {self.navn}, gateadresse {self.gateadresse}, postnr {self.postnr}, poststed{self.poststed}"

def nyttsted():
    stid = int(input("Sted id:"))
    for sted in stedliste:
        if stid == sted.id:
            return sted
    return Sted(stid, input("Sted navn:"), input("gateadresse:"), int(input("postnr:")), input("poststed:"))

def _lagSted():
    stedliste.append(nyttsted())


def lestkategorifrafil(path):
    f = open(path, "r")
    lines = f.readlines()
    steder = []
    for line in lines:
        id, navn, gateadr, postnr, poststed = line.split(";")
        steder.append(Sted(id, navn, gateadr, postnr, poststed))
    f.close()
    return steder

avtaleListe = []
kategoriliste = []
stedliste = []
if __name__ == "__main__":
    meny()