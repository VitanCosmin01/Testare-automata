# SAPTAMANA 4 - part 1

##  📝 OBIECTIVE
1. Sa aflam ce este un API si cum functioneaza
2. Sa intelegem rolul testarii in calitatea unui API Tester
3. JSON vs XML
4. HTTP status codes
5. Postman & componente Postman

## 🔶 API

### ❓ Ce este un API
- API = Application Programming Interface
- Reprezinta un set de proceduri, functii si alte elemente
pe care un sistem le pune la dispozitie pentru a facilita comunicarea
cu un alt sistem.
- In general, se poate decide implementarea unui API, atunci cand avem nevoie
sa transmitem un volum mai mare de date dintr-o aplicatie web catre un sistem extern,
insa nu este necesara atunci cand vrem sa cream spre exemplu un site de prezentare.

## 🔶 Testare API
- Testare care are loc la un nivel foarte timpuriu, pentru a beneficia de avantajul
gasirii timpurii a defectelor, chiar inainte ca GUI-ul sa fie creat
- Exista mai multe aplicatii pe piata pentru testarea de API, printre care cele mai
cunoscute sunt Postman si SOAP UI

## 🔶 API Testing vs Unit Testing

- Testarea de API se face de regula atunci cand avem un output final al sistemului,
si atunci cand doua sisteme sunt deja integrate, pentru a testa comunicarea intre ele,
in timp ce testarea unitara se poate face doar pe o bucata foarte mica dintr-o functionalitate
  (ex: functii, variabile)
- Testarea de API este directionata mai degraba catre verificarea comportamentului de business
si a arhitecturii de sistem, in timp ce testarea unitara verifica functionarea fiecarei functionalitati
individuale, izolate de celalalte functionalitati/componente
- Testarea de API este in general facuta de testeri, in timp ce testarea unitara este de regula facuta
de catre dezvoltatori.

## 🔶 Abordarea testarii de API
- Atunci cand facem testare de API, trebuie sa stim sa interpretam in primul rand erorile care pot aparea,
care pot fi cauzate de erori umane (date incorecte introduse), erori generate de produs (bug-uri in aplicatie),
sau erori generate de server (fisiere corupte, parametri de conectare incorecti, incapacitatea de procesare
a unor date etc.)
- Atunci cand aplicatia este dezvoltata, este recomandat ca testarea sa fie desfasurata concomitent, astfel
incat problemele sa poate fi descoperite in timp util.
- La fel ca orice alt tip de testare, testarea de API, va acoperi atat scenarii pozitive cat si scenarii negative.

## 🔶 Responsabilitati si Cunostiinte necesare ale unui tester de API
- Necesitatea cunoasterii notiunii de Web Service pentru diverse categorii cum ar fi REST, SOAP and Micro Services
(Macar la nivel conceptual)
- Cunoasterea metodelor principale de HTTP - GET, POST, PUT, PATCH, DELETE
- Cunoasterea codurilor de raspuns HTTP pentru validarea raspunsului din punctul de vedere al codului,
mesajului si al timpului de raspuns
- Cunoasterea conceptelor de XML si JSON pentru a putea defini corpul requesturilor de API
- Cunoasterea conceptuala a notiunii de OAuth
- Capacitatea de a intelege documentatia de API si de a scrie test case-uri plecand de la aceasta
- Capacitatea de a putea scrie instructiuni de baza de JS pentru a putea verifica rezultatul request-urilor de API

## 🔶 XML vs JSON

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<root>
    <student>
        <id>01</id>
        <name>Tom</name>
        <lastname>Price</lastname>
    </student>
    <student>
        <id>02</id>
        <name>Nick</name>
        <lastname>Thameson</lastname>
    </student>
</root>
```


```json
{
  "root": {
    "student": [
      {
        "id": "01",
        "name": "Tom",
        "lastname": "Price"
      },
      {
        "id": "02",
        "name": "Nick",
        "lastname": "Thameson"
      }
    ]
  }
}
```

## Mecanisme OAuth
- Un open protocol permite autentificarea sigura a aplicatiilor
de pe web, mobile sau desktop. 
- Open Authentication (OAuth) este un protocol de autorizare
de tip open-standard care furnizeaza aplicatiilor capabilitatea
de a oferi si cere acces în mod sigur. 
- De exemplu, o aplicatie poate sa informeze aplicatia Facebook
ca este ok ca o anumita aplicatie sa acceseze profilul sau
sa posteze actualizari pe timeline fara sa mai ceara parola,
acest lucru minimizand riscul prin faptul ca,
in cazul in care aplicatia este compromisa,
accesul la parola va ramane restrictionat. 

- Mecanismul OAuth nu furnizeaza datele legate de parola,
in schimb foloseste token-uri de autentificare pentru a putea
dovedi identitatea dispozitivului de pe care se cere accesul
(consumer) si furnizorul de servicii (service provider).
- OAuth este un protocol de autentificare care permite
comunicarea dintre doua aplicații in numele utilizatorului
fara ca acesta sa trebuiasca sa furnizeze parola. 
- Exista trei piloni principali in tranzactiile de tipul OAuth:
  - utilizatorul
  - consumatorul
  - furnizorul de servicii

## 🔶 Coduri de raspuns HTTP
- Codurile de raspune HTTP (HTTP status codes) sunt o serie
de numere care definesc daca request-ul care a fost facut
de catre client a fost efectual cu succes sau nu.
- Status code-urile sunt primite in HTTP response, in urma request-ului
facut de catre client.
- Status code-urile sunt impartite in 5 categorii.
- Prima cifra a status code-ului HTTP defineste in care
din cele 5 categorii/clase se incadreaza raspunsul, iar ultimele
doua cifre definesc semnificatia raspunsului.
- Categorii status code-uri:
  - 1xx - Informational
  - 2xx - Succes
  - 3xx - Redirectionare
  - 4xx - Eroare de client
  - 5xx - Eroare de server

## 🔶 POSTMAN - introducere
- Postman este un software independent care este folosit
pentru crearea, design-ul, modificarea si testarea de API.
- Este un GUI simplu de folosit pentru transmiterea si vizualizarea
request-urilor si raspunsurilor HTTP
- Prin intermediul aplicatiei Postman, putem sa transmitem un request
de API, catre un server si sa vizualizam raspunsul detaliat
cu scopul analizei si evaluarii acestuia.
- Folosit foarte mult de catre testeri si developeri pentru
o acoperire mai buna a aplicatiei.
- Instalare aplicatie Postman: https://www.postman.com/downloads/

## 🔶 Componente aplicatie Postman
- New = Opțiune folosită pentru a crea un nou request,
colecție sau mediu de testare
(sau alte elemente utile pentru dezvoltare)
- Import = Opțiune folosită pentru importarea colecțiilor
din exterior
- My Workspace = Un concept similar cu cel de proiect,
în care se vor stoca toate request-urile din cadrul organizației
sau echipei
- Invite = Opțiune folosită pentru a invita alți oameni
sa colaboreze la proiectul nostru. 
- History = Contine toate request-urile trimise anterior
in workspace-ul curent 
- Collections = Contine o serie de request-uri
care sunt grupate in functie de diverse obiective.
  - O colectie poate contine subfoldere.
  - Subfolder-ele si request-urile pot fi dublate
(desi nu se recomanda)
- Request tab = Arata numele request-urilor pe care le ai
deschise 
- HTTP Request = Contine un dropdown cu mai multe metode
de HTTP cum ar fi GET, POST, COPY, DELETE, etc.
  - In testarea de API, cele mai folosite metode sunt
GET si POST. 
- Request URL = Mai poarta numele de endpoint, si reprezinta
un link pe care API-ul il va folosi pentru comunicare 
- Save =  Optiune pentru a salva noul request sau pentru a
actualiza un request creat anterior in urma unor schimbari 
- Params =  Stocheaza parameterii necesari pentru
filtrarea unui request sub forma unei perechi cheie-valoare
- Authorization =  Loc in  care sunt stocate datele de
autentificare pentru a putea fi autorizati
sa executam request-ul.
  - Aici vom pune token-ul pentru Oauth daca este necesar.

- Headers = Headers este locul in care vom defini informatii
legate de tipul request-ului cum ar fi content type JSON.
  - In practica, tot aici se face si autorizarea
- Body =  Informatia care va fi pasata API-ului intr-un
request de POST, PUT sau PATCH .
- Pre-request Script = Bucati de cod care vor fi executate
automat inainte de request. 
  - Cele mai des folosite scripturi sunt cele pentru setarea mediului 
- Tests = Bucati de cod executate automat dupa executarea
request-ului cu scopul de a verifica daca raspunsul returnat 
in timpul executarii testului este cel asteptat
(mesaj, cod, timp de executie, informatii etc)