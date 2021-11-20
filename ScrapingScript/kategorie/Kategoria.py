class Kategoria:
    def __init__(self, id, nazwa, opis, kursy):
        self.id = id
        self.nazwa = nazwa
        self.opis = opis
        self.kursy = kursy

    def kursy_na_string(self):
        napis = ''
        for x in self.kursy:
            napis += (x + ' |')
        napis = napis[:-2]
        return napis

    def drukuj(self):
        print('Id: ',  self.id)
        print('Nazwa: ' + self.nazwa)
        print('Opis: ' + self.opis)
        print('Kursy wchodzące w skład kategorii: ' + self.kursy_na_string())

    def zwroc_kursy(self):
        return self.kursy

    def konwersja_na_liste(self):
        lista = []
        lista.append(self.id)
        lista.append(self.nazwa)
        lista.append(self.opis)
        lista.append(self.kursy_na_string())
        return lista
