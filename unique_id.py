import json
import numpy as np
with open("C:/Users/akost/PycharmProjects/Projekt_walidacja_intel/data.json", 'r') as f:
    data = f.read()
python_obj = json.loads(data)

def lista_id(a):
    list_id = []
    for i in python_obj[a]:
        list_id.append(i['id'])
    return list_id

def id_unique(a):
    list_id = lista_id(a)
    set_id = set()
    for i in python_obj[a]:
        set_id.add(i['id'])

    if len(list_id) == len(set_id):
        return [True]
    else:
        return [False, a]

lista_sekcje = ["images", "licenses", "annotations", "categories"]

for i in lista_sekcje:
    x = id_unique(i)
    if not x[0]:
        print("Nieunikalne id w sekcji " + str(x[1]))

def poprawnosc_id(a, b, c):
    list_id = lista_id(a)
    list_id = np.array(list_id)
    y = []
    for i in range(len(python_obj[b])):
        x = python_obj[b][i][c]
        y.append(x in list_id)
    if False in y:
        print("Blad " + str(c) + " w sekcji " + str(b))
        return False
    else:
        return True
print(poprawnosc_id("categories", "annotations", "category_id"))
print(poprawnosc_id("images", "annotations", "image_id"))
print(poprawnosc_id("licenses", "images", "license"))
