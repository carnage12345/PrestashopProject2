from ListaProduktow import ListaProduktow
from Scrapowanie import scrapujCalyKurs

# javascript_developer
javascript_developer = 'https://sklep.coderslab.pl/index.php?id_product=22&id_product_attribute=5329&rewrite=javascript-developer&controller=product#/27-miasto-wroclaw/33-tryb-weekendowy/37-pakiet-premium/38-rodzaj_platnosci-jednorazowa/662-data_rozpoczecia_kursu-04122021_wroferw20'
# tester_man
tester_man = 'https://sklep.coderslab.pl/index.php?id_product=35&id_product_attribute=4795&rewrite=tester-manualny&controller=product#/28-miasto-krakow/32-tryb-dzienny/35-pakiet-podstawowy/38-rodzaj_platnosci-jednorazowa/595-data_rozpoczecia_kursu-07022022_kratems15'
# python_developer
python_developer = 'https://sklep.coderslab.pl/index.php?id_product=24&id_product_attribute=4669&rewrite=python-developer&controller=product#/26-miasto-warszawa/32-tryb-dzienny/35-pakiet-podstawowy/38-rodzaj_platnosci-jednorazowa/582-data_rozpoczecia_kursu-29112021_warpyts27'
# nodejs
nodejs = 'https://sklep.coderslab.pl/index.php?id_product=37&id_product_attribute=5698&rewrite=nodejs-dla-programistow&controller=product#/31-miasto-online/34-tryb-wieczorowy/35-pakiet-podstawowy/38-rodzaj_platnosci-jednorazowa/714-data_rozpoczecia_kursu-17012022_onlfsfe10'
# tester_aut
tester_aut = 'https://sklep.coderslab.pl/index.php?id_product=31&id_product_attribute=5437&rewrite=tester-automatyzujacy-&controller=product#/31-miasto-online/34-tryb-wieczorowy/35-pakiet-podstawowy/38-rodzaj_platnosci-jednorazowa/676-data_rozpoczecia_kursu-31012022_onlteae10'
# test_lab
test_lab = 'https://sklep.coderslab.pl/index.php?id_product=52&id_product_attribute=5647&rewrite=test-lab&controller=product#/31-miasto-online/35-pakiet-podstawowy/38-rodzaj_platnosci-jednorazowa/707-tryb-self_learning'
# java_developer
java_developer = 'https://sklep.coderslab.pl/index.php?id_product=33&id_product_attribute=4564&rewrite=java-developer&controller=product#/27-miasto-wroclaw/33-tryb-weekendowy/35-pakiet-podstawowy/38-rodzaj_platnosci-jednorazowa/569-data_rozpoczecia_kursu-16102021_wrojeew14'
# redux
redux = 'https://sklep.coderslab.pl/index.php?id_product=34&id_product_attribute=5473&rewrite=js-react-redux-dla-programistow&controller=product#/31-miasto-online/34-tryb-wieczorowy/35-pakiet-podstawowy/38-rodzaj_platnosci-jednorazowa/682-data_rozpoczecia_kursu-10012022_onlfsbe11'
# python_analiza
python_analiza = 'https://sklep.coderslab.pl/index.php?id_product=43&id_product_attribute=5713&rewrite=python-analiza-danych&controller=product#/31-miasto-online/33-tryb-weekendowy/35-pakiet-podstawowy/38-rodzaj_platnosci-jednorazowa/717-data_rozpoczecia_kursu-15012022_onlpadw11'
# docker
docker = 'https://sklep.coderslab.pl/index.php?id_product=45&id_product_attribute=5269&rewrite=docker-wstep-do-konteneryzacji&controller=product#/31-miasto-online/33-tryb-weekendowy/35-pakiet-podstawowy/38-rodzaj_platnosci-jednorazowa/654-data_rozpoczecia_kursu-15012022_onldocw05'
# sql
sql = 'https://sklep.coderslab.pl/index.php?id_product=47&id_product_attribute=5710&rewrite=sql-analiza-danych&controller=product#/31-miasto-online/33-tryb-weekendowy/35-pakiet-podstawowy/38-rodzaj_platnosci-jednorazowa/716-data_rozpoczecia_kursu-15012022_onlsqlw06'
# wizualizacja
wizualizacja = 'https://sklep.coderslab.pl/index.php?id_product=48&id_product_attribute=5086&rewrite=wizualizacja-danych&controller=product#/31-miasto-online/33-tryb-weekendowy/35-pakiet-podstawowy/38-rodzaj_platnosci-jednorazowa/633-data_rozpoczecia_kursu-19022022_onlwidw01'
# scrumstudy
scrumstudy = 'https://sklep.coderslab.pl/index.php?id_product=51&id_product_attribute=5458&rewrite=scrumstudy-scrum-developer-certified-sdc&controller=product#/31-miasto-online/33-tryb-weekendowy/35-pakiet-podstawowy/38-rodzaj_platnosci-jednorazowa/679-data_rozpoczecia_kursu-20112021_onlsdcw01'

wszystkie_linki = [javascript_developer, tester_man, python_developer, nodejs, tester_aut, test_lab, java_developer, redux, python_analiza, docker, sql, wizualizacja, scrumstudy ]

lista_produktow = ListaProduktow()
for x in range(len(wszystkie_linki)):
    scrapujCalyKurs(lista_produktow, wszystkie_linki[x], x)

lista_produktow.zaladuj_do_csv()








