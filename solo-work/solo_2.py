from cmath import pi


print("buongiorno")

class Trojkat:
    def __init__(self, a, b, c, h_a):
            self.bok_a = a
            self.b = b
            self.c = c
            self.h_a = h_a
            #self.obwod = a + b + c

    def obwod(self):
        return self.bok_a + self.b + self.c

    def pole(self):
        return self.bok_a * self.h_a * 0.5

class Kolo:
    def __init__(self, r):
        self.promien = r

    def obwod(self):
        return self.promien * pi * 2

    def pole(self):
        return self.promien * self.promien * pi

kolo_o_promieniu_6 = Kolo(6)

trojkat_rownoboczny = Trojkat(10, 10, 10, 8)
trojkat_antka = Trojkat(12, 13, 5, 12)


class Student:
    def __init__(self, imie, nazwisko, nr_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_indeksu = nr_indeksu
        self.oceny = []

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.nr_indeksu}"

    def __int__(self):
        return 5

    def dodaj_ocene(self, oceny):
        self.oceny.append(oceny)

    def zwroc_srednia(self):
        return sum(self.oceny) / len(self.oceny)

student_gordie = Student("Gordie", "Greep", 1234567809)
student_gordie.dodaj_ocene (4.5)
student_gordie.dodaj_ocene (5)

class Mieszkanie:
    def __init__(self, adres, rodzaj, metraz, czynsz, pietro, ogrod, pokoje):
        self.adres = adres
        self.rodzaj = rodzaj
        self.metraz = metraz
        self.czynsz = czynsz
        self.pietro = pietro
        self.ogrod = ogrod
        self.pokoje = pokoje

    def __str__(self):
        return f"{self.adres} - {self.rodzaj}. Miesięczny czynsz za to mieszkanie wynosi: {self.czynsz} złotych, a jego powierzchnia to {self.metraz} metrów kwadratowych."

    def oblicz_czynsz_roczny(self):
        return f"Czynsz roczny za to mieszkanie wynosi {12 * self.czynsz} złotych."

    def podnies_czynsz(self):
        self.czynsz = self.czynsz*1.25

    def obniz_czynsz(self):
        self.czynsz = self.czynsz*0.8

mieszkanie_Jacoba = Mieszkanie("Łączna 43, Lipinki Łużyckie", "Kawalerka", 40, 2345, 2, "nie", 3)

#print(trojkat_rownoboczny.obwod())
#print(trojkat_antka.pole())

#print(kolo_o_promieniu_6.obwod())
#print(kolo_o_promieniu_6.pole())

#print(student_gordie.oceny)

print(mieszkanie_Jacoba.__str__())
print(mieszkanie_Jacoba.oblicz_czynsz_roczny())
mieszkanie_Jacoba.podnies_czynsz()
print(mieszkanie_Jacoba.__str__())
print(mieszkanie_Jacoba.oblicz_czynsz_roczny())
mieszkanie_Jacoba.obniz_czynsz()
print(mieszkanie_Jacoba.__str__())
print(mieszkanie_Jacoba.oblicz_czynsz_roczny())
