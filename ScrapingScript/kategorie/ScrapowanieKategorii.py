import os
from requests import get
from bs4 import BeautifulSoup
from kategorie.Kategoria import Kategoria


def scrapuj_kategorie(lista_kategorii, url, id):

    # Pobranie strony
    strona = get(url)
    bs = BeautifulSoup(strona.content, 'html.parser')
    kategoria = bs.find('section', {"id": 'main'})
    nazwa = kategoria.find('h1', {"class": 'h1'}).get_text()

    opis = kategoria.find('div', {"id": 'category-description'}).get_text()
    opis = opis.replace('\n', ' ')

    kursy = []
    modul_kursow = kategoria.find('div', {'class': 'products row'})
    wszystkie = modul_kursow.find_all('h3', {'class': 'h3 product-title'})

    for x in wszystkie:
        if x.get_text() == 'JS, React, Redux dla...':
            kursy.append('JS, React, Redux dla Programistów')
        elif x.get_text() == 'SCRUMstudy Scrum Developer...':
            kursy.append('SCRUMstudy Scrum Developer Certified (SDC™)')
        elif x.get_text() == 'Docker - Wstęp do...':
            kursy.append('Docker - Wstęp do Konteneryzacji')
        else:
            kursy.append(x.get_text())

    # Stworzenie nowego obiektu Kategoria i dodanie go do listy
    lista_kategorii.dodaj_kategorie(Kategoria(id, nazwa, opis, kursy))
