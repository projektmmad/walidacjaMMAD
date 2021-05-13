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

lista_sekcje=["images","licenses","annotations","categories"]
for i in lista_sekcje:
    x=id_unique(i)
    if not x[0]:
        print(x[1])
