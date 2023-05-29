from typing_extensions import Self
import pandas as pd

class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto

    def __str__(self):
        return f"Witaj {self.imie} {self.nazwisko}! Technokrates czujnie nad Tobą czuwa :)"

    def oblicz_netto(self):
        self.netto = 0,7852*self.wynagrodzenie_brutto

    def oblicz_koszty(self):
        self.koszty = 0,2048*self.wynagrodzenie_brutto

    def oblicz_koszty_calkowity(self):
        self.koszty_calkowite = (1-self.oblicz_netto)+self.koszty

df = pd.read_csv(r'salary.csv')
print(df)

pracownicy = [df]

for Pracownik in pracownicy:
    print("Pracownik "self.imie+" "+self.nazwisko)
    print("- pensja brutto: "+Self.wynagrodzenie_brutto)
    print("- pensja netto: "+Self.oblicz_netto)
    print("- koszt pracodawcy: "+Self.oblicz_koszty)
    print("- koszt całkowity: "+Self.oblicz_koszt_calkowity)

print("Suma kosztów wynosi: "+Self.koszty_calkowite)