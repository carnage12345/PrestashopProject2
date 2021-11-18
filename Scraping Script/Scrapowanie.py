import os
from requests import get
from bs4 import BeautifulSoup
from Produkt import Produkt


def scrapujCalyKurs(lista_produktow, url, id):
    # Zadeklarowanie zmiennych
    nazwa = ''
    zdjecie = ''
    stan = ''
    miasto = ''
    adres = ''
    wszystkie_miasta = []
    tryb = ''
    wszystkie_tryby = []
    data = ''
    wszystkie_daty = []
    pakiet = ''
    wszystkie_pakiety = []
    platnosc = ''
    platnosci = []
    cena = ''
    data_preworku = ''
    liczba_godzin = ''

    harmonogram = ''
    har_link = ''

    wym_wstepne = ''
    wym_link = ''

    program = ''
    prog_link = ''

    warunki = ''
    war_link = ''

    opis = ''
    pierwsze_miasto = False

    # Pobranie strony i jej podzielenie na wiersze

    strona = get(url)
    bs = BeautifulSoup(strona.content, 'html.parser')
    kurs = bs.find('section', {"id": 'main'})
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
        # WSZYSTKIE MIASTA
        elif wiersze[x] == 'Miasto' and pierwsze_miasto is False:
            y = x + 1
            while True:
                if wiersze[y] == 'Tryb':
                    pierwsze_miasto = True
                    break
                else:
                    wszystkie_miasta.append(wiersze[y])
                y += 1
        # WSZYSTKIE TRYBY KURSU
        elif wiersze[x] == 'Tryb':
            y = x + 1
            while True:
                if wiersze[y] == 'Data rozpoczęcia kursu' or 'Pakiet':
                    break
                else:
                    wszystkie_tryby.append(wiersze[y])
                y += 1
        # WSZYSTKIE DATY ROZPOCZEC KURSU
        elif wiersze[x] == 'Data rozpoczęcia kursu':
            y = x + 1
            while True:
                if wiersze[y] == 'Pakiet':
                    break
                else:
                    wszystkie_daty.append(wiersze[y])
                y += 1
        # WSZYSTKIE PAKIETY
        elif wiersze[x] == 'Pakiet':
            y = x + 1
            while True:
                if wiersze[y] == 'Rodzaj płatności':
                    break
                else:
                    wszystkie_pakiety.append(wiersze[y])
                y += 1
        # WSZYSTKIE PLATNOSCI
        elif wiersze[x] == 'Rodzaj płatności':
            y = x + 1
            while True:
                if wiersze[y][0].isdigit():
                    break
                else:
                    platnosci.append(wiersze[y])
                y += 1
            cena = wiersze[y]  # + wiersze[y + 1]
        # MIASTO
        elif pierwsze_miasto and (wiersze[x] == 'Miasto:' or wiersze[x] == 'Miasto'):
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
        # DATA UDOSTEPNIENIA PREWORKU
        elif wiersze[x] in {'Data udostępnienia preworku: ', 'Data udostępnienia preworku:',
                            'Data udostępnienia preworku', 'Data udostępnienia prework'}:
            data_preworku = wiersze[x + 1]
            if len(data_preworku) < 5:
                data_preworku = wiersze[x + 2]
        # LICZBA GODZIN KURSU
        elif wiersze[x] in {'Liczba godzin kursu:', 'Liczba godzin kursu'}:
            liczba_godzin = wiersze[x + 1]
        # ADRES
        elif wiersze[x] in {'Adres', 'Adres zajęć', 'Adres zajęć:'}:
            adres = wiersze[x + 1]
        else:
            pass

    # ZDJECIE
    zdjecie = kurs.find('div', class_='product-cover')
    zdjecie = zdjecie.find('a')['href']

    # DATA ROZPOCZĘCIA KURSU
    data = kurs.find('select', {"id": 'group_7'})
    if data:
        data = data.find('option', {'selected': 'selected'}).get_text()
    else:
        data = ''

    # RODZAJ PLATNOSCI
    platnosc = kurs.find('select', {"id": 'group_9'})
    platnosc = platnosc.find('option', {'selected': 'selected'}).get_text()

    # OPIS

    opis1 = kurs.find('div', class_="product-description")
    opis1 = opis1.get_text(separator='\n')

    opis2 = kurs.find('div', class_="product-reference")
    opis2 = opis2.get_text(separator='\n')

    opis = opis1.replace('\n', '') + opis2.replace('\n', '')

    # LINKI
    licznik = 0
    for span in kurs.find_all('span'):
        all_a = span.find_all('a')
        for a in all_a:
            if a:
                text = a.get_text().strip()
                if text == "Harmonogram kursu":
                    har_link = a['href']
                    harmonogram = span.get_text().split('-')[1].strip()
                elif text == "Szczegółowy program kursu":
                    prog_link = a['href']
                    program = span.get_text().split('-')[1].strip()
                    licznik = 1
                elif text == "Ogólne Warunki Umowy" or licznik == 1:
                    war_link = a['href']
                    warunki = span.get_text().split('-')[1].strip()
                    licznik = 0
                elif text == "Wymagania wstępne":
                    wym_link = a['href']
                    wym_wstepne = span.get_text().split('-')[1].strip()

    # STWORZENIE NOWEGO OBIEKTU PRODUKT I DODANIE GO DO LISTY PRODUKTOW
    lista_produktow.dodaj_produkt(
        Produkt(id, nazwa, zdjecie, stan, miasto, adres, tryb, data, pakiet, platnosc, cena, data_preworku,
                liczba_godzin,
                harmonogram, har_link, wym_wstepne, wym_link, program, prog_link, warunki, war_link, opis))
