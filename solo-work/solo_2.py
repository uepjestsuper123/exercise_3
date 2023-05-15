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

print(trojkat_rownoboczny.obwod())
print(trojkat_antka.pole())

print(kolo_o_promieniu_6.obwod())
print(kolo_o_promieniu_6.pole())