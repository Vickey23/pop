import string
from os import path
dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path = path.join(dir_path, filename)

if not path.exists(data_path):
    exit()

with open(data_path, 'r', encoding="utf-8") as f:
    linie = f.readlines()
    f.close()

    slowa = []
    for linia in linie:
        slowa += linia.split()

    for i in range(len(slowa)):
        if "." in slowa[i]:
            slowa[i] = slowa[i].replace(".", "")
        if "," in slowa[i]:
            slowa[i] = slowa[i].replace(",", "")
        if ";" in slowa[i]:
            slowa[i] = slowa[i].replace(";", "")

    print (f"Ilość słów: {len(slowa)}")

    koncowki = []

    for slowo in slowa:
        litera = slowo[-1]
        if litera not in koncowki and litera.isalpha():
            koncowki.append(litera)

    staty = {}
    for litera in koncowki:
        staty[litera] = sum(slowo.endswith((litera)) for slowo in slowa)

    print(staty)