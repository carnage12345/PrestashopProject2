import os
from requests import get
from bs4 import BeautifulSoup
from produkty.Produkt import Produkt


def scrapujProdukt(lista_produktow, url, id):
    # Zadeklarowanie zmiennych

    nazwa = '',  # Name
    zdjecie = '',   # Image URL
    stan = '',   # Condition
    miasto = '',
    tryb = '',   # Description
    data = '',   # Product availability date
    pakiet = '',
    platnosc = '',
    opis = '',   # Description
    kategorie = []  # Categories

    # Pobranie strony i jej podzielenie na wiersze

    strona = get(url)
    bs = BeautifulSoup(strona.content, 'html.parser')
    kurs = bs.find('section', {'id': 'main'})
    """
    opis = kurs.get_text(separator='\n')
    opis = os.linesep.join([s for s in opis.splitlines() if s])

    wiersze = []
    for line in opis.splitlines():
        line = line.strip()
        if line != '':
            wiersze.append(line)

    # Wyłuskanie danych: NAZWA, STAN, MIASTO, TRYB, DATA_ROZPOCZĘCIA_KURSU, PAKIET, RODZAJ_PLATNOSCI
    # DATA_UDOSTĘPNIENIA_PREWORKU, LICZBA_GODZIN_KURSU, ADRES_ZAJĘC

    for x in range(len(wiersze)):
        # NAZWA
        if x == 0:
            nazwa = wiersze[x]
        # STAN
        elif wiersze[x] == 'Stan::':
            stan = wiersze[x + 1]
        # MIASTO
        elif wiersze[x] == 'Miasto:' or wiersze[x] == 'Miasto':
            if len(wiersze[x + 1]) > 3:
                miasto = wiersze[x + 1]
            else:
                miasto = wiersze[x + 2]
        # TRYB KURSU
        elif wiersze[x] == 'Tryb kursu:' or wiersze[x] == 'Tryb kursu':
            tryb = wiersze[x + 1]
            if len(tryb) < 5:
                tryb = wiersze[x + 2]
        # PAKIET KURSU
        elif wiersze[x] == 'Pakiet kursu:' or wiersze[x] == 'Pakiet kursu':
            pakiet = wiersze[x + 1]
            data_preworku = wiersze[x + 1]
            if len(data_preworku) < 5:
                data_preworku = wiersze[x + 2]
        else:
            pass
    """

    # NAZWA
    nazwa = kurs.find('h1', class_='h1 productpage_title')
    if nazwa:
        nazwa = nazwa.get_text()
    else:
        nazwa = ''

    # STAN
    stan = kurs.find('div', class_='product-condition')
    if stan:
        span = stan.find('span')
        if span:
            stan = span.get_text()
        else:
            stan = ''
    else:
        stan = ''


    # ZDJECIE
    zdjecie = kurs.find('div', class_='product-cover')
    zdjecie = zdjecie.find('a')['href']

    # MIASTO
    miasto = kurs.find('select', {"id": 'group_5'})
    if miasto:
        miasto = miasto.find('option', {'selected': 'selected'}).get_text()
    else:
        miasto = ''

    # TRYB
    tryb = kurs.find('select', {"id": 'group_6'})
    if tryb:
        tryb = tryb.find('option', {'selected': 'selected'}).get_text()
    else:
        tryb = ''

    # DATA ROZPOCZĘCIA KURSU
    data = kurs.find('select', {"id": 'group_7'})
    if data:
        data = data.find('option', {'selected': 'selected'}).get_text()
    else:
        data = ''

    # Pakiet

    pakiet = kurs.find('select', {"id": 'group_8'})
    if pakiet:
        pakiet = pakiet.find('option', {'selected': 'selected'}).get_text()
    else:
        pakiet = ''

    # RODZAJ PLATNOSCI

    platnosc = kurs.find('select', {"id": 'group_9'})
    if platnosc:
        platnosc = platnosc.find('option', {'selected': 'selected'}).get_text()
    else:
        platnosc = ''

    # OPIS

    opis = kurs.find('div', {'id': 'tab-content'})
    opis = opis.get_text()
    opis = opis.replace('\n', ' ')

    # STWORZENIE NOWEGO OBIEKTU PRODUKT I DODANIE GO DO LISTY PRODUKTOW
    lista_produktow.dodaj_produkt(
        Produkt(id, nazwa, zdjecie, stan, miasto, tryb, data, pakiet, platnosc, opis, kategorie))
