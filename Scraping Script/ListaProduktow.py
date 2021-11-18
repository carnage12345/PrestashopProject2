import csv
import os
from requests import get
from bs4 import BeautifulSoup
from Scrapowanie import scrapujCalyKurs

class ListaProduktow:
    wszystkie_produkty = []
    naglowek = ['id', 'nazwa', 'zdjecie', 'stan', 'miasto', 'adres', 'tryb', 'data', 'pakiet', 'platnosc', 'cena', 'data_preworku', 'liczba_godzin',
                'harmonogram', 'har_link', 'wym_wstepne', 'wym_link', 'program', 'prog_link', 'warunki', 'war_link', 'opis']

    def dodaj_produkt(self, produkt):
        self.wszystkie_produkty.append(produkt)

    def scrapuj_wszystkie_kursy(self, url):
        strona = get(url)
        bs = BeautifulSoup(strona.content, 'html.parser')
        kursy = bs.find('section', {"id": 'products'})
        iterator = 0
        for link in kursy.find_all('img'):
            link = link['href']
            scrapujCalyKurs(self, link, iterator)
            iterator += 1

    def drukuj_produkty(self):
        for x in self.wszystkie_produkty:
            x.drukuj()

    def zaladuj_do_csv(self):
        with open('products.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(self.naglowek)
            for x in self.wszystkie_produkty:
                writer.writerow(x.konwersjaNaListe())

