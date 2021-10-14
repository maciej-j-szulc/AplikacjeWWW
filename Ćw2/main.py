import FileManager

#Zad1
def ablist(alist,blist):
    listaC = []
    for x in listaA:
        if x%2 == 0:
            listaC.append(x)
    for x in listaB:
        if x%2 == 1:
            listaC.append(x)
    print(listaC)


listaA = [1,2,3,4,5]
listaB = [6,7,8,9,10]
ablist(listaA,listaB)

#Zad2
def dataOps(data_text):
    slownik = {
        "length":len(data_text),
        "letters":list(data_text),
        "big_letters":data_text.upper(),
        "small_letters":data_text.lower()
    }
    print(slownik)

dataOps("Przykładowy tekst")

#Zad3
def delaLetter(text, letter):
    text = text.replace(letter,"")
    print(text)

delaLetter("Maciek","a")

#Zad4
def tempCalc(temperature,temperature_type):
    if temperature_type == "Fahrenheit":
        Fahrenheit = (temperature * 1.8) + 32
        print(Fahrenheit)
    elif temperature_type == "Rankine":
        Rankine = ((temperature * 1.8) + 32) + 459.67
        print(Rankine)
    elif temperature_type == "Kelvin":
        Kelvin = temperature + 273.15
        print(Kelvin)
    else:
        print("Wartość nieprawidłowa")

tempCalc(20,"Fahrenheit")

#Zad5
class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def difference(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y



liczby = Calculator(5,10)
print(liczby.add())
print(liczby.difference())
print(liczby.multiply())
print(liczby.divide())

#Zad6
class ScienceCalculator(Calculator):
    def exponentiation(self):
        return self.x**self.y

liczby2 = ScienceCalculator(5,10)
print(liczby2.exponentiation())

#Zad7
def revString(text):
    print(text[::-1])

revString("Haha")

#Zad9
uchwyt = FileManager.FileManager("sample.txt")
uchwyt.read_file()
uchwyt.update_file()