import json
with open("C:/Users/akost/PycharmProjects/Projekt_walidacja_intel/data.json", 'r') as f:
    data = f.read()
python_obj = json.loads(data)

def id_unique(a):
    list_id = []
    for i in python_obj[a]:
        list_id.append(i['id'])

    set_id = set()
    for i in python_obj[a]:
        set_id.add(i['id'])

    if len(list_id) == len(set_id):
        print("id jest unikalne")
    else:
        print("id nie jest unikalne")

id_unique("images")
