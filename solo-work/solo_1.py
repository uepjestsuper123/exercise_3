# zadanie 1.1

hello = "Hello"
student = "Ola"

print("{} {}".format(hello,student))

# zadanie 1.2

student = input("Wpisz swoje imie: ")
print("Hello "+student)

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

liczba_studentow = len(studenci)
print("Liczba studentow wynosi: ", liczba_studentow)

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

for x in range(liczba_studentow):
    print("Hello "+studenci[x])

# zadanie 1.5

liczba = 3
potega = 4

wynik = pow(liczba,potega)

print("Wynik wynosi: ",wynik)

# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")

print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()

print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie 1.8

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort(key=lambda name: name.split(" ")[-1].lower())

print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie 1.9

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studentN = 0

for student in studenci:
    if student.split(" ")[-1].lower().startswith("n"):
        studentN += 1
print("Liczba studentow na N wynosi: ",studentN)

# zadanie 1.10

wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

def isLinear(coordinates):
    if len(coordinates) < 3:
        return True
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    slope = (y2 - y1 ) / (x2 - x1) if x2 != x1 else float('inf')
    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        new_slope = (y - y1) / (x - x1) if x != x1 else float('inf')
        if abs(new_slope - slope ) >= 1e-9:
            return False
    return True

print(isLinear(wykres_1))
print(isLinear(wykres_2))
print(isLinear(wykres_3))