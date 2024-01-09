# # GRADINITA
# """Abstractizare
# Creati o clasa abstracta numita Gradinita care sa mosteneasca clasa ABC
# (abstract base class) care sa aiba urmatoarele metode:
#
# activitate_practica()
# ora_de_somn()
#
# Corpul primei metode va fi “pass” iar corpul celei de-a doua metode va contine
# un raise NotImplementedException (estimeaza cineva ce inseamna acest raise NotImplementedException?).
        # RASPUNS - NotImplementedError este ridicată în corpul metodei ora_de_somn()
        # pentru a indica că această metodă trebuie implementată în clasele derivate.
# Fiecare din cele doua metode vor avea decoratorul @abstractbaseclass (ce este un decorator?)

from abc import ABC, abstractmethod

class Gradinita(ABC):
    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError("Metoda trebuie implementata in clasele derivate")

# Implementati doua clase: GradinitaPublica si GradinitaPrivata care sa implementeze (mosteneasca) clasa abstracta Gradinita.
# Prima clasa, GradinitaPublica va rescrie ambele metode in felul urmator:
# activitate_practica() va printa pe ecran: “copiii invata sa deseneze”
# ora_de_somn() va printa pe ecran: “copiii trebuie sa doarma la ora cinci”
# A doua clasa, GradinitaPrivata va rescrie o singura metoda in felul urmator:
# activitate_practica() va printa pe ecran: “copiii invata sa modeleze cu plastilina”
#

class GradinitaPublica(Gradinita):
    def activitate_practica(self):
        print("Copiii invata sa deseneze")

    def ora_de_somn(self):
        print("Copiii trebuie sa doarma la ora cinci")

class GradinitaPrivata(Gradinita):
    def activitate_practica(self):
        print("Copiii invata sa modeleze cu plastilina")

    def ora_de_somn(self):
        print("Copiii trebuie sa doarma la ora cinci")

# Rulati codul. Se intampla ceva?
# Instantiati un obiect din clasa GradinitaPublica si rulati codul. Se printeaza ceva pe ecran? De ce?
# Apelati metoda activitate_practica() si rulati codul. Ce observati?
# Instantiati un obiect din clasa GradinitaPrivata si rulati codul. De ce va da eroare?
# Cum putem sa rezolvam eroarea?

        # RASPUNS - GradinitaPublica implementează ambele metode definite în clasa de bază Gradinita.
        # GradinitaPrivata implementează doar o singură metodă, ceea ce duce la o eroare în
        # timpul instanțierii, deoarece nu îndeplinește toate metodele abstracte definite în
        # clasa de bază. Pentru a rezolva eroarea, trebuie să implementăm și metoda ora_de_somn()
        # în clasa GradinitaPrivata

# Instantierea obiectului din clasa GradinitaPublica
gradinita_publica = GradinitaPublica()

# Apelarea metodelor
gradinita_publica.activitate_practica()
gradinita_publica.ora_de_somn()

# Instantierea obiectului din clasa GradinitaPrivata
gradinita_privata = GradinitaPrivata()

# Apelarea metodelor
gradinita_privata.activitate_practica()
gradinita_privata.ora_de_somn()


# """
# Mostenire
# Creati o noua clasa: GradinitaPublica25 care sa mosteneasca clasa GradinitaPublica.
# Implementati doar una din metode in felul urmator:
# activitate_practica() va printa pe ecran: “Copiii se joaca in curte pe balansoar”
#
class GradinitaPublica25(GradinitaPublica):
    def activitate_practica(self):
        print("Copiii se joaca in curte pe balansoar")

# Polimorfism
# In interiorul clasei GradinitaPublica25 creati o noua metoda care sa primeasca de
# la tastatura numarul de buline rosii pe care le-a primit fiecare elev in parte,
#  procesati-le si calculati media aritmetica a numarului de buline rosii.
#  Daca aceasta este mai mare decat cinci, printati pe ecran: “Elevii acestei gradinite
#  sunt foarte neastamparati”.

    def calculeaza_media_buline_rosii(self):

        numar_elevi = int(input("Introduceți numărul de elevi: "))
        buline_rosii = []

        for i in range(numar_elevi):
            buline = int(input(f"Introduceți numărul de buline roșii pentru elevul {i + 1}: "))
            buline_rosii.append(buline)

        media = sum(buline_rosii) / numar_elevi

        if media > 5:
            print("Elevii acestei grădinițe sunt foarte neastâmpărați.")
        else:
            print("Elevii gradinitei sunt foarte cuminti.")

# Bonus:
# In interiorul clasei GradinitaPublica25 creati o noua metoda care sa primeasca de
# la tastatura un dictionar care sa contina o serie de perechi cheie:valoare si dictionare
#  imbricate (embedded, nested) care sa contina urmatoarele informatii: numele elevului,
#  numele parintilor, varsta elevului, activitatea preferata. Printati pentru
#  fiecare elev toate informatiile de mai sus.

    def informatii_elevi(self): #definim o metoda pentru citirea informatiilor si salvarea lor
        numar_elevi = int(input('introduceti numarul de elevi:')) #vom introduce numarul elevilor
        informatii_elevi = {} #cream un dictionar gol

        for i in range(numar_elevi): #pentru toti elevii introducem detaliile de mai jos
            nume_elev = input('introduceti numele elevului: ')
            nume_parinti = input('introduceti numele parintilor: ')
            varsta_elev = int(input('introduceti varsta elevului: '))
            activitate_preferata = input('introduceti activitatea preferata: ')

            informatii_elevi[nume_elev] = {
                'nume' : nume_elev,
                'parinti' : nume_parinti,
                'varsta' : varsta_elev,
                'activitate_preferata' : activitate_preferata
            } #salvam toate informatiile de mai sus in dictionarul creat

        return informatii_elevi #in final ne returneaza dictionarul completat

    def afisare_informatii_elevi(self,informatii_elevi): #definim o metoda pentru afisarea informatiilor
        for nume_elev, informatii_elev in informatii_elevi.items():
            print(f"informatiile despre elevul {nume_elev} sunt : ")
            print(f"nume elev: {informatii_elev['nume']}")
            print(f"nume parinti: {informatii_elev['parinti']}")
            print(f"varsta elev: {informatii_elev['varsta']}")
            print(f"activitate preferata: {informatii_elev['activitate_preferata']}")
            print("\n")

#
#
# Encapsulare
# In interiorul clasei GradinitaPublica25 creati trei atribute: unul public,
# unul private si unul protected.
#
    def __init__(self):
             self.public = "Atribut public"
             self.__private = "Atribut privat"
             self._protected = "Atribut protejat"
#
# Implementati in interiorul clasei GradinitaPublica25 un getter, un setter
# si un deleter pentru atributul private. Cum ne putem folosi de acestia pentru
# accesarea acestui atribut in afara clasei?
#
    def get_private(self):
        print(f'getter: {self.__private}')
        return self.__private

    def set_private(self, valoare_noua):
        print(f'setter: {valoare_noua}')
        self.__private = valoare_noua

    def del_private(self):
        print('deleter: am sters atributul privat')
        del self.__private

#
# Instantiati un obiect din clasa GradinitaPublica25.
# Prin intermediul obiectului instantiat apelati metodele activitate_practica()
# si ora_de_somn(). Ce se printeaza pe ecran? De ce putem sa apelam si metoda somn?
#
#         # RASPUNS - Clasa GradinitaPublica25 mosteneste clasa GradinitaPublica,
#         # astfel încât mostenirea metodei ora_de_somn() vine de la clasa de bază.
#         # Apelând metodele prin intermediul obiectului gradinita_25, se observă că
#         # metoda activitate_practica() a fost suprascrisă în clasa GradinitaPublica25,
#         # iar metoda ora_de_somn() este moștenită de la clasa de bază GradinitaPublica.
#
# Instantierea obiectului din clasa GradinitaPublica25
gradinita_25 = GradinitaPublica25()
#
# Apelarea metodelor
gradinita_25.activitate_practica()
gradinita_25.ora_de_somn()
#
# Apelarea metodei adăugate în clasa GradinitaPublica25 despre buline rosii
gradinita_25.calculeaza_media_buline_rosii()
#
# Citirea informatiilor despre elevi de la tastatura, si apelarea metodei pentru afisarea informatiilor
informatii_introduse = gradinita_25.informatii_elevi()

gradinita_25.afisare_informatii_elevi(informatii_introduse)

#
# Prin intermediul obiectului instantiat din clasa apelati pe rand:
# atributul public, atributul private si respectiv pe cel protected. Care din cele trei sunt sugerate
# atunci cand scriem numele obiectului instantiat urmat de caracterul “.”?
#
gradinita_publica_25 = GradinitaPublica25()
#
#  Accesarea atributului public
print(gradinita_publica_25.public)  # Nu va returna eroare, se poate accesa direct
#
# Accesarea atributului privat
print(gradinita_publica_25.__private)  # Acesta va returna eroare pentru că încercăm să accesăm un atribut privat direct
#
# Accesarea atributului protejat
print(gradinita_publica_25._protected)  # Nu va returna eroare, dar este considerat "protejat" și nu ar trebui să fie accesat direct
#
# Utilizarea getter-ului pentru atributul privat
print(gradinita_publica_25.get_private())  # Va returna valoarea atributului privat
# #
# Utilizarea setter-ului pentru atributul privat
gradinita_publica_25.set_private("Noua valoare")  # Setăm o nouă valoare pentru atributul privat
# #
# Utilizarea deleter-ului pentru atributul privat
gradinita_publica_25.del_private()  # Ștergem atributul privat
print(gradinita_publica_25.get_private())  # Va returna eroare pentru că atributul privat a fost șters

