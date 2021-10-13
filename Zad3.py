#Zad3
print("------ZAD3-------")
tekst = "TEST"
tekst2 = "TEST ALE WIĘKSZY"
data = {'first': 'Hodor', 'last': 'Hodor!'}
class Data(object):
    def __str__(self):
        return 'str'
    def __repr__(self):
        return 'repr'
print('{:>10}'.format(tekst))
print('{:^10}'.format(tekst))
print('{:.5}'.format(tekst2))
print('{first} {last}'.format(**data))
print('{0!s} {0!r}'.format(Data()))