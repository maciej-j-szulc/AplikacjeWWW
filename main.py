#Zad1
print("------ZAD1--------")
lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. " \
        "Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. " \
        "Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. " \
        "Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty " \
        "Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym " \
        "do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

#Zad2
print("------ZAD2--------")
imie = "Maciej"
nazwisko = "Szulc"
litera_1 = imie[2]
litera_2 = nazwisko[3]
l1counter = lorem.count(litera_1)
l2counter = lorem.count(litera_2)
print("W tekście jest {0} liter {2} oraz {1} liter {3}".format(l1counter, l2counter, litera_1, litera_2))

#Zad4
print("------ZAD4--------")
tekst = "Ala ma kota"
print(dir(tekst))
help(tekst.isnumeric())

#Zad5
print("------ZAD5--------")
imie = "Maciej"
nazwisko = "Szulc"

print(imie[::-1].capitalize()+" "+nazwisko[::-1].capitalize())

#Zad6
print("------ZAD6--------")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dlugosc = len(lista)
srodek = dlugosc/2
nowa_lista = lista[int(srodek):]
lista = lista[:int(srodek)]
print(lista)
print(nowa_lista)

#Zad7
print("------ZAD7--------")
lista.extend(nowa_lista)
lista.insert(0,0)
kopia = lista.copy()
kopia.sort(reverse=True)
print(kopia)

#Zad8
print("------ZAD8--------")
imiona_nazwiska = ("Cezary Welter","Mateusz Wiśniowski", "Paweł Wroński")
numery_indeksu = ("111111", "222222", "333333")
lista8 = list()

for i in range(len(imiona_nazwiska)):
    for j in range(len(numery_indeksu)):
        if i == j:
            para = imiona_nazwiska[i] + " " + numery_indeksu[j]
            lista8.append(para)

print(lista8)

#Zad9
print("------ZAD9--------")
for i in range(len(lista8)):
    para = lista8[i]
    keys = list()
    values = list()
    keys.append(para[0])
    values.append((para[1]))

slownik = dict.fromkeys(keys,values)


#Zad10
print("------ZAD10-------")
lista10 = ["123456789","234567890","345678901","123456789","234567890"]
zbior = set(lista10)

print(zbior)

#Zad11
print("------ZAD11-------")
for x in range(11):
    print(x)

#Zad12
print("------ZAD12-------")

for x in range(100,19,-5):
    print(x)

#Zad13
print("------ZAD13-------")
lista13 = [
{"jeden": 1, "dwa": 2, "trzy": 3},
{"cztery": 4, "pięć": 5, "sześć": 6},
{"siedem": 7, "osiem": 8, "dziewięć": 9},
{"dziesięć": 10, "jedenaście": 11, "dwanaście": 12}
]
print(lista13)
