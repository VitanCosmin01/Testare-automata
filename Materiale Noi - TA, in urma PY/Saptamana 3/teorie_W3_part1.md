# SAPTAMANA 3 - part 1

##  📝 OBIECTIVE
1. TDD
2. Testarea unitara in contextul nivelurilor de testare
3. BDD - introducere
4. BDD - Gherkin syntax
5. POM Design Pattern

## 🔶 TDD

### ❓ Ce este TDD?
- TDD = Test Driven Development
- Abordare de dezvoltare software care presupune
crearea testelor automate inainte de scrierea efectiva
a codului.
- In general, implementata de echipa de development, prin
definirea testelor unitare inainte de implementarea
functionalitatii.

### 👍 Avantaje TDD
1. Ajuta la crearea minimului de cod optim necesar implementarii
unei functionalitati.
2. Acoperire mai mare a scenariilor de business si nevoilor clientului
3. Claritate mai mare asupra testarii

### 📃 Succesiunea etapelor de dezvoltare TDD
- Crearea testelor automate pe baza cerintelor de business
- Rularea testelor automate (si ne asteptam ca acestea sa pice avand in vedere ca nu am scris codul)
- Crearea codului pe baza testelor automate scrise mai sus
- Refactorizarea testelor si re-rularea testelor automate (ne asteptam ca acestea sa treaca, pentru ca de data asta avem codul scris)
- Refactorizare cod in urma defectelor gasite in timpul testarii
- Rerularea testelor cu fixurile aplicate

! **Refactorizare** = modificarea codului prin eliminarea elementelor neutilizate sau adaugarea elementelor lipsa

## 🔶 Testarea unitara in contextul nivelurilor de testare
- In procesul de software testing, exista 5 niveluri de testare
care reflecta testarea facuta la diverse grade de finalizare
a aplicatiei: Unit Testing, Integration Testing, System Testing
si Acceptance Testing.

### 🔷 Unit Testing - Testare unitara (Testare de componente)
- Fiecare bucata individuala de cod este testata pentru
a verifica daca este pregatita pentru utilizare.
- Test unitar = testarea celei mai mici bucati functionale
dintr-o aplicatie (functii, clase etc.).

### 🔷 Integration Testing - Testare de integrare
- Se concentreaza pe interactiunile intre componente
si sisteme si pe felul in care acestea comunica intre ele.
- 2 tipuri de testare de integrare:
#### 🔹 Integrare intre componente
- cand doua sau mai multe module/componente sunt legate intre ele
#### 🔹 Integrare intre sisteme
- cand doua sau mai multe sisteme sunt legate intre ele.

### 🔷 System Testing - Testare de sistem
- Se concentreaza pe comportamentul si capabilitatea sistemului
ca un tot unitar, tinand cont de comportamentul end-to-end
al functionalitatilor pe care sistemul trebuie sa le execute,
tinand cont si de comportamentul non-functional asteptat al acelor task-uri.

### 🔷 Acceptance Testing - Teste de acceptanta
- Se concentreaza pe comportamentul si capabilitatile sistemului ca un tot
unitar.
- Exista 2 tipuri de testare de acceptanta:
#### 🔹 Alpha Testing
- Ultima sesiunea de testare inainte ca produsul sa fie lansat
publicului larg.
- Testarea unei aplicatii atunci cand dezvoltarea este completa
sau aproape completa.
- In urma testarii alpha, se pot face cateva schimbari minore
daca e necesar.
- Testarea are loc la site-ul dezvoltatorului si se realizeaza
in doua faze:
  - Faza 1 - software-ul este testat de catre dezvoltatori
  - Faza 2 - testarea se face de catre echipa de QA, intr-un
mediu similar cu cel al clientului.

#### 🔹 Beta testing
- Are loc la site-ul clientului.
- Se va trimite sistemul/softul la utilizatori, acestia vor
instala aplicatia si vor incepe sa o foloseasca in conditii reale.
- Scopul testarii beta este sa puna aplicatia in mana unor utilizatori
reali, oameni ce nu fac parte din echipa de dezvoltatori, pentru
a descoperi defecte din perspectiva utilizatorului.

## 🔶 BDD

### ❓ Ce este BDD?
- BDD = Behaviour Driven Development
- BDD este o abordare derivata din TDD
- Atentie mai mare asupra scenariilor de testare
- Presupune maparea testelor automate cu o serie de fisiere descriptive 
scrise intr-un limbaj natural.
- Diferenta intre TDD si BDD este data de fisierele descriptive
incluse in BDD, numite **FEATURE FILES**.

### 👍 Avantajele BDD

1. O intelegere mai usoara a codului
2. O atentie mai mare acordata testelor si produsului dezvoltat ca intreg
3. O acoperire mai mare a scenariilor de business si nevoilor clientului
4. O claritate mai mare asupra testarii
5. Toate persoanele interesate (Clienti, Manageri, BAs, Developeri, Testeri etc.)
vor intelege mai usor rapoartele generate -> 'Living Documentation' pentru proiect


### 📃 Succesiunea etapelor de dezvoltare BDD

- Crearea fisierelor descriptive pe baza cerintelor de business (feature files)
- Crearea testelor automate pe baza fisierelor descriptive
- Rularea testelor automate (si ne asteptam ca acestea sa pice avand in vedere ca nu am scris codul)
- Crearea codului pe baza testelor automate scrise mai sus
- Refactorizarea testelor si re-rularea testelor automate ( ne asteptam ca acestea sa treaca, pentru ca de data asta avem codul scris)
- Refactorizare cod in urma defectelor gasite in timpul testarii
- Rerularea testelor cu fixurile aplicate


## 🔶 Gherkin syntax

- BDD-ul foloseste fisiere descriptive pe baza cerintelor de business.
- Aceste fisiere se numesc feature files.
- Limbajul in care este scris un feature file se numeste Gherkin.
- Gherkin este un limbaj de specificatii usor de citit si de inteles.
- Acesta permite descrierea scenariilor de testare intr-un mod standardizat
si usor de inteles de catre toate partile implicate in dezvoltarea
software-ului: developeri, testeri, product manageri etc.

- In general, intr-un feature file de BDD putem gasi urmatoarele <span style="color:#8044EA">**elemente**</span>:
1. <span style="color:#8044EA">**Feature**</span> = o functionalitate mai mare care se doreste a fi testata
2. <span style="color:#8044EA">**Scenario**</span> = o descriere a unei situatii specifice care poate fi intalnita de un utilizator in viata reala
3. <span style="color:#8044EA">**Scenario steps**</span> = instructiuni care trebuie urmarite pas cu pas pentru verificarea unui scenariu (Given, When, Then, And, But)
4. <span style="color:#8044EA">**Background**</span> = context general valabil pentru majoritatea scenariilor de testare.

- Scenariile sunt scrise in limbajul gherkin pe baza unor user stories = descrieri ale unor situatii specifice din viata utilizatorului, pe baza urmatoarelor componente:
1. Cine face actiunea
2. Care este sistemul asupra caruia se actioneaza
3. Care este rezultatul / beneficiul pe care vreau sa il obtin.


## 🔶 POM Design Pattern
- **POM Design Pattern** = Page Object Model Design Pattern
- POM este **cel mai folosit design pattern** in testarea web
- **Design Pattern** = o solutie gasita pentru o problema general
intalnita la software -> o structura/un how-to de urmat astfel incat sa avem o solutie/o implementare consistenta, readable si extensibila
- **PAGE OBJECT MODEL** = un design pattern care presupune gruparea
codului de TESTARE AUTOMATA, astfel incat fiecare pagina web sa aiba un corespondent (o clasa intr-un fisier python) de mapare
a elementelor si actiunilor de pe acea pagina

## 🔶 Structura unui proiect BDD implementat cu POM

1. un folder features = contine toate fisierele de tip feature-files
2. un folder steps = contine implementarea tehnica a fisierelor de tip feature
3. un folder pages (cel care defineste structura BDD) = contine paginile de mapare a paginilor web
4. un fisier browser (py) = contine implementarea browser-ului
5. un fisier environment (py) = contine instantierea tuturor obiectelor din clasele de tip Page
6. un fisier base_page (py) = contine metode ce sunt folosite in mai multe fisiere,
pentru a fi importate si reutilizate
