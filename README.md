# Pràctica 1: Com podem capturar les dades de la web?
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14107063.svg)](https://doi.org/10.5281/zenodo.14107063)

## Versions
Versió|Data|Descripció dels canvis
-|-|-
V1|12/11/24|Publicació inicial.

## Descripció
Aquest repositori conté la documentació per a la *Pràctica 1* de l'assignatura *Tipologia i cicle de vida de les dades* amb codi *M2.951* del *Màster en Ciència de Dades* de la Universitat Oberta de Catalunya (UOC).
En aquesta pràctica s'identifiquen i extreuen dades rellevants per a un projecte analític mitjançant eines específiques de *web scraping*.

## Membres del grup
L'activitat ha estat realitzada per:
| | | |
---|---|---
[Arnau Biosca Romanillos, PhD](https://www.linkedin.com/in/naubiosca/) | <img href="mailto:abioscaro@uoc.edu" src="https://www.uoc.edu/etc.clientlibs/uoc-common/clientlibs/clientlib-site/resources/images/favicons/favicon-32x32.png" width="16"> [abioscaro@uoc.edu](mailto:abioscaro@uoc.edu) | <img href="https://orcid.org/0000-0002-3047-8991" src="https://orcid.org/assets/vectors/orcid.logo.icon.svg" width="16"> [https://orcid.org/0000-0002-3047-8991](https://orcid.org/0000-0002-3047-8991)
[Eduard Ferrer Font](https://www.linkedin.com/in/eduard-ferrer-font/) | <img href="mailto:eduardferrer@uoc.edu" src="https://www.uoc.edu/etc.clientlibs/uoc-common/clientlibs/clientlib-site/resources/images/favicons/favicon-32x32.png" width="16"> [eduardferrer@uoc.edu](mailto:eduardferrer@uoc.edu) | <img href="https://orcid.org/0009-0000-1286-7646" src="https://orcid.org/assets/vectors/orcid.logo.icon.svg" width="16"> [https://orcid.org/0009-0000-1286-7646](https://orcid.org/0009-0000-1286-7646)


## Lloc web

[https://www.cuinacatalana.eu/ca/pag/receptes/](https://www.cuinacatalana.eu/ca/pag/receptes/)

## Context
Amb l'objectiu de promoure una millor salut a través de l'alimentació, així com de promoure i explorar la cultura culinaria catalana, la Fundació Institut Català de la Cuina i de la Cultura Gastromòmica està realitzant, en col·laboració amb la UOC, un estudi sobre el valor energètic i nutricional dels plats que conformen el receptari culinari català.
En aquest context, el següent programa busca crear un repositori amb les dades obtingudes d'aquest estudi per a tal de poder fer-ne un posterior anàlisis.

## Descripció del dataset
Per aquesta pràctica hem decidit desenvolupar una eina per a extreure informació rellevant de receptes de cuina catalana, fent servir com a font la web de la Fundació Institut Català de la Cuina i de la Cultura Gastronòmica.

El dataset està composat per aproximadament 900 receptes de cuina, de les quals es disposa el nom, els ingredients, el procés d'elaboració, una categoria i, en determinats casos, el seu valor nutricional, així com variacions.

Els objectius de la solució són:
- Extreure les dades de les receptes de cuina de pàgines webs rellevants (versió 1)
- Disposar de les dades en format estandaritzat i ordenat per a la seva posterior explotació (versió 2)
- Realitzar estudis sobre les dades obtingudes. Alguns casos d'ús poden ser la recerca de noves receptes, la recuperació de receptes en desús o la optimització de dietes, l'estudi de l'alimentació catalana. (versió 2)

## Representació gràfica
Aquesta representació gràfica mostra les relacions entre les dades d'una manera teòrica i com a proposta d'estructura que podria implementar-se per a la seva seva explotació posterior.

Per tant, aquesta representació no correspon a la estructura original del dataset, el qual es troba sense processar i guardat en format CSV.

<img src="img.png" alt="Representació ideal de les dades" width=500>

## Contingut
El dataset esà composat per un llistat de receptes. Cada recepta té els atributs "títol", "secció" (categoria), "Ingredients" (llistat d'ingredients), "Instruction" (descripció del procés d'elaboració), "Variations" (variacions de la recepta original i "Nutrition Information" (informació nutricional).

## Propietari
El propietari del conjunt de dades és la Fundació Institut Català de la Cuina i de la Cultura Gastronòmica. Anteriorment s'han realitzat estudis i publicacions amb algunes de les dades del dataset. Destaquem les publicacions presents a https://www.uoc.edu/opencms_portal2/opencms/CA/unesco-chair-food-culture-development/publications/list.html.

Per altra banda, estudis similars al proposat en aquesta pràctica, han permés la creació de *datasets* de receptes per facilitar la recerca de l'espai culinari (receptes, ingredients, processos de cocció, tècniques, patrons d'alimentació) i associacions amb els sabors i la salut: https://pubmed.ncbi.nlm.nih.gov/33238002/

Per a determinar els requeriments legals de les dades utilitzades s'ha consultat l'arxiu `robots.txt` així com l'Avís Legal de la pàgina web. No s'hi ha trobar cap limitaicó en l'explotació de les dades.

El dataset esà composat per un llistat de receptes. Cada recepta té els atributs "títol", "secció" (categoria), "Ingredients" (llistat d'ingredients), "Instruction" (descripció del procés d'elaboració), "Variations" (variacions de la recepta original i "Nutrition Information" (informació nutricional).

## Inspiració
Aquest conjunt de dades preten servir de base de coneixement per a la creació d'enies que permetin la creació de receptes noves, la recomanació de receptes segons, trobar relacions entre patrons alimentaris i salud. Un cas d'éxit similar és el de l'estudi realitzat per Batra et al,en el que creen un dataset de 118171 receptes de tot el món amb objectius similars.

## Llicència
El contingut d'aquest repositori està sotmés a una llicència MIT. Aquesta llicència permet la lliure distribució, contribució i modificació del contingut del repositori, tant del codi font com de les dades extretes.
Qualsevol distribució realitzada a partir del repositori original ha d'inlcoure també l'avís dels drets d'autor original, és a dir, el text de la llicència MIT. Podeu consultar la llicència a l'arxiu LICENCE del repositori.
S'ha escollit aquesta llicència per a fomentar l'ús d'aquestes dades sense restriccions, conservant-ne l'autoria i exlcoent als autors de tota responsabilitat.

## Codi
El codi es troba a la carpeta **/source**
Veure **requirements.txt** per a les llibreries utilitzades i la seva versió.
Executar l'arxiu `main.py`. Les funcions estan a `scraper.py`. En finalitzar l'execució del codi, l'arxiu `csv_data.csv` serà creat al directori.

## Dataset
El dataset està disponible a Zenodo amb[DOI: 10.5281/zenodo.14107062](https://zenodo.org/records/14107063)

## Vídeo
Enllaç a la memòria del projecte.

## Recursos
1. Subirats, L., Calvo, M. (2018). Web Scraping. Editorial UOC.
2. Masip, D. El lenguaje Python. Editorial UOC.
3. Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
4. Simon Munzert, Christian Rubba, Peter Meißner, Dominic Nyhuis. (2015). Automated Data Collection with R: A Practical Guide to Web Scraping and Text Mining. John Wiley & Sons.
5. freeCodeCamp. (2024). *How to Create and Sync Git and GitHub Repositories*. https://www.freecodecamp.org/news/create-and-sync-git-and-github-repositories/
7. Devansh B. et al. RecipeDB: a resource for exploring recipes, Database, Volume 2020, 2020, baaa077, https://doi.org/10.1093/database/baaa077.
