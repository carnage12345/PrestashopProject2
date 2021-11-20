class Produkt:
    def __init__(self, id, nazwa, zdjecie, stan, miasto, tryb, data, pakiet, platnosc,
                  opis, kategorie):
        # Po prawej identyfikatory w bazie
        self.id = id     # ID
        self.nazwa = nazwa    # Name
        self.zdjecie = zdjecie  # Image URL
        self.stan = stan  # Condition
        self.miasto = miasto
        self.tryb = tryb  # Description
        self.data = data  # Product availability date
        self.pakiet = pakiet
        self.platnosc = platnosc
        self.opis = opis    # Description
        self.kategorie = []  # Categories

    def kategorie_na_string(self):
        napis = ''
        for x in self.kategorie:
            napis += (x + ',')
        napis = napis[:-1]
        return napis

    def drukuj(self):
        print('Id: ',  self.id)
        print('Nazwa: ' + self.nazwa)
        print('Zdjecie: ' + self.zdjecie)
        print('Stan: ' + self.stan)
        print('Miasto: ' + self.miasto)
        print('Tryb: ' + self.tryb)
        print('Data: ' + self.data)
        print('Pakiet: ' + self.pakiet)
        print('Platnosc: ' + self.platnosc)
        print('Opis: ' + self.opis)
        print('Kategorie: ' + self.kategorie_na_string())

    def konwersja_na_liste(self):
        lista = []
        lista.append(self.id)
        lista.append(self.nazwa)
        lista.append(self.zdjecie)
        lista.append(self.stan)
        lista.append(self.miasto)
        lista.append(self.tryb)
        lista.append(self.data)
        lista.append(self.pakiet)
        lista.append(self.platnosc)
        lista.append(self.opis)
        lista.append(self.kategorie_na_string())

        return lista
