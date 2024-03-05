"""
1. Ce este o variabila in Python?
"""
# VARIABILA = un container de memorie din calculator in care stocam date
mama = "Maria"

"""
2. Cum afisam un mesaj in consola?
"""
print("Hello World")
print(mama)
print(f"Hello {mama}")
msg = "Hello " + mama
print(msg)
print("Hello", mama)

"""
3. Ce tipuri de date cunosti?
"""
# string
x = "Azi e vineri"

# integer
y = 10

# float
z = 10.1

# boolean
w = True

"""
4. Cum putem extrage un subsir de caractere dintr-un string?
"""
str1 = "It's almost Christmas"
# str1 = 'It\'s almost Chirstmas'

# 1. extragem subsirul de la indexul 0 la indexul 4
print(str1[:5])
print(str1[0:5])

# 2. extragem subsirul de la indexul 5 la indexul 8
print(str1[5:9])

# 3. extragem subsirul de la indexul 6 pana la finalul string-ului
print(str1[6:])


"""
5. Caracterieaza urmatoarele structuri de date din punct de vedere
al mutabilitatii (mutabil/imutabil) si al ordonarii (ordonat/neordonat):
- liste
- dictionare
- tupluri
- seturi
"""
# mutabil = putem adauga, sterge, modifica lista
# ordonat = elementele din structura de date sunt salvate in memorie in ordinea
# in care sunt scrise -> ca le putem accesa dupa INDEX

# LISTE
# mutabile + ordonate
my_list = ["alb", 12,  "albastru", 12, True, False, 15.9]
print(f"BEFORE {my_list}")

# lista e mutabila
my_list[1] = "verde"
print(f"AFTER {my_list}")

# lista e ordonata
print(my_list[3])


# SET-urile
# Set-urile contin doar elemente UNICE
# MUTABILE + NEORDONATE
# Atentie! -> set-urile contin doar elemente IMUTABILE
pyta5 = {"mult", "succes"}
print(pyta5)

# putem adauga o valoare noua in set
pyta5.add("maine")
print(pyta5)

pyta5.add("mult")
print(pyta5)

# dictionarele
# mutabile + neordonate
# cheile din dictionar sunt unice

my_dict = {
    "user1": "Mihai",
    "user2": "Georgel"
}

# dictionarele sunt mutabile
my_dict.update({"user3": "Valentin", "user4": "Laurentia"})
print(my_dict)

# daca cheia exista, se va actualiza valoarea
# daca nu, se va adauga un element nou cu cheia respectiv valoarea
my_dict["user5"] = "Daniel"


# accesarea elementelor din dictionar se face dupa CHEIE
print(my_dict["user5"])
# ATENTIE! -> daca cheia nu exista in dictionar, obtinem eroare: KeyError

# ca sa nu avem eroare cand accesam o valoare din dictionar dupa cheie
# ne folosim de metoda get
print(my_dict.get("user5", None))

# tupluri
# ordonate + imutabile

my_tuple = ("mere", "pere", "mere", "pere")
print(my_tuple[1])

"""
6. Ce este o exceptie in Python si cum o putem trata?
"""
# O exceptie/o eroare este o situatie in care nu se poate executa codul.

# Ca sa tratam o exceptie ne folosim de blocul try/except
try:
    mama = Maria
except NameError:
    print("Valoarea trebuie sa fie intre ghilimele")


"""
7. Ce sunt functiile in Python?
"""
# FUNCTII = o bucata de cod care se executa doar atunci cand este apelata
# Functiile sunt reutilizabile! Le definim o singura data, si le folosim/apelam/invocam
# de cate ori avem nevoie


def my_function(mama):
    print(f"Hi {mama}")

my_function("Maria")

"""
8. Ce sunt clasele in Python?
"""
# CLASELE sunt un template/sablon/reteta pentru a crea obiecte
# practic, ne ajuta sa transpunem in cod obiecte din viata reala
# si in clase definim comportamentul si caracteristicile acestor obiecte


class Product:

    def __init__(self, name, price):
        self.price = price
        self.name = name

    def show_details(self):
        return f"Product has the following attributes: {self.price}, {self.name}"


product1 = Product("telefon", 12)
print(product1.name)
print(product1.price)
msg = product1.show_details()
print(msg)


"""
9. Care sunt principiile OOP?
"""
# INCAPSULARE
# ABSTRACTIZARE
# MOSTENIRE
# POLIMORFISM


class A:

    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b

    def some_method1(self):
        print("some_message")


class B(A):

    # in clasa B, sa mai avem un atribut pe obiect numit c1
    # in clasa B, sa mai avem o metoda, numita some_method2

    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c1 = c

    def some_method2(self):
        print("some other message")

# 1. initializeaza un obiect din clasa A
# Acceseaza toate atributele si metodele disponibile


obj1 = A(a="mult", b="succes")
print(obj1.a1)
print(obj1.b1)
obj1.some_method1()

# 2. Initializeaza un obiect din clasa B
# Acceseaza toate atributele si metodele disponibile

obj2 = B(a="mult", b="succes", c="tuturor")
print(obj2.a1)
print(obj2.b1)
print(obj2.c1)
obj2.some_method2()
obj2.some_method1()


"""
10. Ce face blocul else atasat unui ciclu repetitiv?
"""
# BLOCUL ELSE atasat unui ciclu repetitiv este codul
# care se executa la finalul ciclului repetitiv
# DOAR DACA ciclul repetitiv a ajuns la final

# for i in range(1, 10):
#     print(i)
# else:
#     print("bloc else")

for i in range(1, 10):
    if i == 2:
        continue
    print(i)
    if i == 5:
        break
else:
    print("bloc else")

x = 0
while x < 5:
    print(x) # 0 1 2 3 4
    x += 1 # 1 2 3 4 5
else:
    print("bloc else de la while")

"""
11. Cum putem accesa o valoare dintr-un dictionar?
"""
my_dict = {
    "key1": "value1"
}

print(my_dict["key1"])
print(my_dict.get("key2", False))

"""
12. Cum putem inversa un string?
"""
my_str = "abc"
print(my_str[::-1])

# my_str[start:end:pas]

"""
13. Care este diferenta dintre o interfata si o clasa abstracta?
"""
# INTERFATA = Are doar metode abstracte
# CLASA ABSTRACTA = Are atat metode abstracte + metode cu implementare

"""
14. Ce reprezinta parametru self folosit in clase?
"""
# self = un parametru care reprezinta o referinta catre instanta clasei ce urmeaza
# a fi creata.
for i in range(4, 0, -2):
    print(i)