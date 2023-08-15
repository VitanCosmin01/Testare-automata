# SAPTAMANA 3 - part 2

##  📝 OBIECTIVE
- PRACTICA: proiect BDD
- Scenario steps: Given, When, Then, And, But
- Rularea scenariilor de test
- Tag-uri scenarii

## 💻 Practica
- Vom folosi POM pentru a testa feature-uri de pe o pagina web:
https://www.saucedemo.com/

## 🔶 Setup proiect BDD
1. Pycharm -> New Project
2. pip install selenium
3. pip install behave (o librarie BDD care va interpreta si rula testele scrise in Gherkin)
4. pip install behave-html-formatter (ne ajuta sa generam rapoarte BDD)
5. pip install webdriver-manager

## 🔶 behave

- Documentatie: https://behave.readthedocs.io/en/stable/


## 🔶 Structura unui proiect BDD, urmand DP POM

1. un folder features = contine toate fisierele de tip feature-files
2. un folder steps = contine implementarea tehnica a fisierelor de tip feature
3. un folder pages (cel care defineste structura BDD) = contine paginile de mapare a paginilor web
4. un fisier browser (py) = contine implementarea browser-ului
5. un fisier environment (py) = contine instantierea tuturor obiectelor din clasele de tip Page
6. un fisier base_page (py) = contine metode ce sunt folosite in mai multe fisiere,
pentru a fi importate si reutilizate


## 🔶 Scenario steps: Given, When, Then, And, But

### 🐾 Given
- Crearea contextului scenariului de testare
- Punerea sistemului intr-un context cunoscut inainte
ca utilizatorul sa inceapa sa interactioneze cu sistemul
- Exemple: navigarea catre o pagina, logarea utilizatorului etc

### 🐾 When
- Cuprinde actiuni ale utilizatorului
- Descrie interactiunea cu sistemul (ce vrem sa testam)
- Exemple: click pe elemente de pe pagina, completare valori pe pagina


### 🐾 Then
- Verificarea rezultatelor observabile de catre utilizator
- Ce se intampla daca utilizatorul a urmat tot scenariul

### 🐾 And si But

```
Scenario: Multiple Givens
  Given one thing
  Given an other thing
  Given yet an other thing
   When I open my eyes
   Then I see something
   Then I don't see something else
```

```
Scenario: Multiple Givens
  Given one thing
    And an other thing
    And yet an other thing
   When I open my eyes
   Then I see something
    But I don't see something else
```


## 🔶 Rulare scenarii de test

- Pentru a rula testele folosim comanda **behave**:

```commandline
behave
```

## 🔶 Tag-uri scenarii
- Putem adauga tag-uri pentru scenariile testate in feature files.

```
Feature: Fight or flight
  In order to increase the ninja survival rate,
  As a ninja commander
  I want my ninjas to decide whether to take on an
  opponent based on their skill levels

  @slow
  Scenario: Weaker opponent
    Given the ninja has a third level black-belt
    When attacked by a samurai
    Then the ninja should engage the opponent

  Scenario: Stronger opponent
    Given the ninja has a third level black-belt
    When attacked by Chuck Norris
    Then the ninja should run for his life
```

- Folosind tag-uri, putem sa personalizam rularea testelor astfel:
1. Rularea scenariilor de test cu un anumit tag:
```commandline
behave --tags=slow
```
2. Rularea scenariilor de test, cu exceptia celor care au un anumit tag:
```commandline
behave --tags=-slow
```
- Use case: definirea unui tag @wip si rularea doar
acelui scenariu de test
