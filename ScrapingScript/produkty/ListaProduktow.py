import csv
from requests import get
from bs4 import BeautifulSoup
from produkty.ScrapowanieProduktow import scrapujProdukt

# self.id = id  # ID
# self.nazwa = nazwa  # Name
# self.zdjecie = zdjecie  # Image URL
# self.stan = stan  # Condition
# self.miasto = miasto
# self.tryb = tryb  # Description
# self.data = data  # Product availability date
# self.pakiet = pakiet
# self.platnosc = platnosc
# self.opis = opis  # Description
# self.kategorie = []  # Categories

class ListaProduktow:
    wszystkie_produkty = []
    naglowek = ['id', 'nazwa', 'zdjecie', 'stan', 'miasto', 'tryb', 'data', 'pakiet', 'platnosc', 'opis', 'kategorie']

    def dodaj_produkt(self, produkt):
        self.wszystkie_produkty.append(produkt)

    def scrapuj_wszystkie_kursy(self, url):
        strona = get(url)
        bs = BeautifulSoup(strona.content, 'html.parser')

        paginacje = bs.find('nav', {'class': 'pagination'})
        paginacje = paginacje.find_all('a', {'rel': 'nofollow'})
        iterator = 0

        for x in paginacje:
            zmienna = get(x['href'])
            zmienna1 = BeautifulSoup(zmienna.content, 'html.parser')
            kursy = zmienna1.find_all('li', {'class': 'product_item col-xs-12 col-sm-6 col-md-6 col-lg-4'})
            for link in kursy:
                scrapujProdukt(self, link.find('a')['href'], iterator)
                iterator += 1

    def drukuj_produkty(self):
        for x in self.wszystkie_produkty:
            x.drukuj()

    def zaladuj_do_csv(self):
        with open('produkty.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(self.naglowek)
            for x in self.wszystkie_produkty:
                writer.writerow(x.konwersja_na_liste())

