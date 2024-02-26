x = 10
print(x)
x = 20
print(x)

# Typy zmiennych
# Komentarz
a = 5  # (int) liczba całkowita
b = 5.4  # (float) liczba zmienno-przecinkowa
zdanie = 'Barbiturian'  # (str)
obecnyUczen = True  # (bool)

# Operatory arytmetyczne
# + = / * **-potęgowanie //-dzielenie w dół (z zaokrągleniem w dół) %-modulo (reszta z dzielenia)
x = 2 ** 3
print(x)
y = 11 // 2
print(y)
z = 5 % 3
print(z)

# Lekcja 1.7

cenaNettoJS = 10000
cenaNettoPython = 7500

cenaBruttoJS = cenaNettoJS * 1.23
cenaBruttoPython = cenaNettoPython * 1.23

print('cena brutto za kurs JS:')
print(cenaBruttoJS)
print('cena brutto za kurs python:')
print(cenaBruttoPython)

vat = 21

cenaNettoJS = 10000
cenaNettoPython = 7500
obliczonyVat = (1 + vat / 100)

cenaBruttoJS = cenaNettoJS * obliczonyVat
cenaBruttoPython = cenaNettoPython * obliczonyVat

print('cena brutto za kurs JS:')
print(cenaBruttoJS)
print('cena brutto za kurs python:')
print(cenaBruttoPython)

'''Oblicz cenę netto programu wiedząc, że:
cena brutto programu wynosi 215 zł
VAT - 19 %'''

abletonBrutto = 215
vat = 19

obliczonyVat = (1 + vat / 100)
abletonNetto = abletonBrutto / obliczonyVat
print('Cena Abletona Netto:')
print(abletonNetto)

netto = 25
vat = 20
kwotabrutto = netto * (vat / 100)
brutto = kwotabrutto + netto
print(brutto)

brutto = 100
vat = 20
oblicznienetoo = ((100 - vat) / 100)
kwotanetto = brutto * oblicznienetoo
print(kwotanetto)