class Produkt:
    def __init__(self, id, nazwa, zdjecie, stan, miasto, adres, tryb, data, pakiet, platnosc, cena, data_preworku,
                 liczba_godzin,
                 harmonogram, har_link, wym_wstepne, wym_link, program, prog_link, warunki, war_link, opis):
        self.id = id
        self.nazwa = nazwa
        self.zdjecie = zdjecie
        self.stan = stan
        self.miasto = miasto
        self.adres = adres
        self.tryb = tryb
        self.data = data
        self.pakiet = pakiet
        self.platnosc = platnosc
        self.cena = cena
        self.data_preworku = data_preworku
        self.liczba_godzin = liczba_godzin
        self.harmonogram = harmonogram
        self.har_link = har_link
        self.wym_wstepne = wym_wstepne
        self.wym_link = wym_link
        self.program = program
        self.prog_link = prog_link
        self.warunki = warunki
        self.war_link = war_link
        self.opis = opis

    def drukuj(self):
        print('Id: ',  self.id)
        print('Nazwa: ' + self.nazwa)
        print('Zdjecie: ' + self.zdjecie)
        print('Stan: ' + self.stan)
        print('Miasto: ' + self.miasto)
        print('Adres : ' + self.adres)
        print('Tryb: ' + self.tryb)
        print('Data: ' + self.data)
        print('Pakiet: ' + self.pakiet)
        print('Platnosc: ' + self.platnosc)
        print('Cena: ' + self.cena)
        print('Data preworku: ' + self.data_preworku)
        print('Liczba godzin: ' + self.liczba_godzin)
        print()
        print(self.har_link + ' ' + self.harmonogram)
        print(self.wym_link + ' ' + self.wym_wstepne)
        print(self.prog_link + ' ' + self.program)
        print(self.war_link + ' ' + self.warunki)
        print()
        print(self.opis)

    def konwersjaNaListe(self):
        lista = []
        lista.append(self.id)
        lista.append(self.nazwa)
        lista.append(self.zdjecie)
        lista.append(self.stan)
        lista.append(self.miasto)
        lista.append(self.adres)
        lista.append(self.tryb)
        lista.append(self.data)
        lista.append(self.pakiet)
        lista.append(self.platnosc)
        lista.append(self.cena)
        lista.append(self.data_preworku)
        lista.append(self.liczba_godzin)
        lista.append(self.harmonogram)
        lista.append(self.har_link)
        lista.append(self.wym_wstepne)
        lista.append(self.wym_link)
        lista.append(self.program)
        lista.append(self.prog_link)
        lista.append(self.warunki)
        lista.append(self.war_link)
        lista.append(self.opis)

        return lista
