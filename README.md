# Pràctica 1: Com podem capturar les dades de la web?
## Notes
vmorantc@uoc.edu
veure repo > https://github.com/jmoreiras-uoc/tcvd-formato-practica1
## Versions
Versió|Data|Descripció dels canvis
-|-|-
V0|27/10/24|Creació del repositori i preparació de la documentació.

## Descripció

Aquest repositori conté la documentació per a la *Pràctica 1* de l'as-
signatura *Tipologia i cicle de vida de les dades* amb codi *M2.951* del
*Màster en Ciència de Dades* de la Universitat Oberta de Catalunya (UOC).

En aquesta pràctica s'identifiquen i extreuen dades rellevants per a un
projecte analític mitjançant eines específiques de *web scraping*.

## Membres del grup

L'activitat ha estat realitzada per:
[Arnau Biosca Romanillos, PhD](https://www.linkedin.com/in/naubiosca/)
[Eduard Ferrer Font](https://www.linkedin.com/in/eduard-ferrer-font/)

## Context
Explicar en quin context específic s’han recollit les dades i argumentar perquè el lloc web seleccionat és una font pertinent i fiable d’aquesta informació. Indicar l’adreça del lloc web.

## Títol
Web scraping per a la cerca d'immobles

## Descripció del dataset
Per aquesta pràctica hem decidit desenvolupar una eina per a extreure 
informació rellevant de portals immobiliaris com ara idealista,
habitaclia o fotocasa. 

Tots dos estem cercant immobles actualment i ens ha semblat que donar
resposta a una necessitat real era la millor manera d'aproximar-nos a
l'activitat. 

Els objectius de la solució són:
- Extreure les dades de les plataformes de compra-venda i lloguer d'im-
mobles de manera automatitzada. (versió 1)
- Escollir les millors opcions per a inversió mitjançant eines de proces
sament que incloguin analítica de dades. (versió 2)

## Representació gràfica
Dibuixar un esquema o diagrama que reflecteixi visualment
el dataset i el projecte escollit.

## Contingut
Explicar els camps que s’inclouen al dataset i el període de temps a què pertanyen les dades.
## Propietari
Presentar el propietari del conjunt de dades. És necessari incloure cites d'anàlisis anteriors o, en cas de no  haver-n’hi, justificar aquesta cerca amb anàlisis similars. Indiqueu quins passos s’han seguit per actuar d’acord amb els principis ètics i legals en el context del projecte escollit.
## Inspiració
Explicar per què pot ser interessant aquest conjunt de dades i quines preguntes s’hi pretenen respondre. És necessari comparar amb les anàlisis anteriors o anàlisis similars presentades a l’apartat 6.
## Llicència
Seleccionar una d'aquestes llicències pel dataset resultant i justificar el motiu de la seva selecció. Exemples de llicències que poden considerar-se:
- Released Under CC0: Public Domain License.
- Released Under CC BY-NC-SA 4.0 License.
- Released Under CC BY-SA 4.0 License.
- Database released under Open Database License, individual contents under Database Contents License.
- Altres (especificar quina).
## Codi
Codi implementat per a l’obtenció del dataset, preferiblement en Python o, alternativament, en R.
- El codi haurà de situar-se a la carpeta /source del repositori.
- S'han d'indicar les llibreries i versions utilitzades. P. ex., en Python poden obtenir-se mitjançant la comanda pip3 freeze > requirements.txt
- Al document PDF s'han de comentar els aspectes més rellevants sobre com el codi realitza el procés de  recol·lecció de dades, quines dificultats presenta el lloc web triat, i com les heu resolt.

## Dataset
Publicar el dataset obtingut en format CSV a Zenodo, incloent-hi una breu descripció del mateix. Obtenir i adjuntar l'enllaç del DOI del dataset (https://doi.org/...). El dataset també haurà d’incloure’s a la carpeta /dataset del repositori. Si existeix qualsevol circumstància que impedeixi publicar obertament el dataset real a Zenodo, s’haurà de:
a. Comentar aquesta circumstància i justificar el motiu.
b. Generar un dataset simulat i publicar-lo a Zenodo, obtenint l'enllaç del DOI.
c. Comunicar al professor el dataset real de manera privada (p. ex., al repositori privat o a una carpeta de Google Drive privada).

## Vídeo
Realitzar un breu vídeo explicatiu de la pràctica (màxim 10 minuts), que haurà de comptar amb la participació dels dos integrants del grup. Al vídeo s'haurà de realitzar una presentació del projecte, destacant els punts més rellevants, tant de les respostes als apartats com del codi utilitzat per a extreure les dades. Indicar l'enllaç del vídeo (https://drive.google.com/...), que haurà d’estar al Google Drive de la UOC

```markdown
## Ficheros del código fuente

* **src/main.py**: punto de entrada al programa. Inicia el proceso de scraping.
* **src/scraper.py**: contiene la implementación de la clase _AccidentsScraper_ cuyos métodos generan el conjunto de datos a partir de la base de datos online [PlaneCrashInfo](http://www.planecrashinfo.com/database.htm).
* **src/reason_classifier.py**: contiene la implementación de la clase que se encarga de asignar una causa a un resumen de accidente dado. Para ello, utiliza la librería *TextBlob*.
```
## Recursos
1. Subirats, L., Calvo, M. (2018). Web Scraping. Editorial UOC.
2. Masip, D. El lenguaje Python. Editorial UOC.
3. Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
4. Simon Munzert, Christian Rubba, Peter Meißner, Dominic Nyhuis. (2015). Automated Data Collection with R: A Practical Guide to Web Scraping and Text Mining. John Wiley & Sons.
5. freeCodeCamp. (2024). *How to Create and Sync Git and GitHub Repositories*. https://www.freecodecamp.org/news/create-and-sync-git-and-github-repositories/