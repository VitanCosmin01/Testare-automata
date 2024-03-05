# SAPTAMANA 4 - Part 3 TESTE JavaScript (in Postman)

##  📝 OBIECTIVE


1. Sa scriem teste JavaScript direct in Postman pentru request-urile noastre
2. Sa rulam aceste teste JavaScript

## 🔶 Ce sunt testele din Postman?
- Testele din Postman sunt teste scrise in limbajul de programare JavaScript, care sunt scrise
direct in aplicatia Postman si ne ajuta sa facem verificari in acelasi timp in care se ruleaza/se face
un request.
- De obicei incep cu "pm.test"

## 🔶 Workshop
- Vom testa din Postman, Simple Book API: https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md
- Documentatia: https://learning.postman.com/docs/writing-scripts/test-scripts/

## 🔶 Debugging
- Debugging: https://learning.postman.com/docs/sending-requests/troubleshooting-api-requests/#using-log-statements

## 🔶 Cum rulam toata colectia de teste?

1. Manual, din Postman

2. Cu command-line-ul Newman:
- documentatie: https://learning.postman.com/docs/collections/using-newman-cli/installing-running-newman/
- Instalam nodejs: https://nodejs.org/en#home-downloadhead
- Instalam newman:
  - intr-un git bash: npm install -g newman
- Exportam colectia sub format json din Postman pe local
- Rulam testele: newman run fisierul_json_care_reprezinta_colectia
