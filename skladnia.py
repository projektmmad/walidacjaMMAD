import json

def skladnia_valid(json_file):

    json_data = json.load(open('data.json'))

    if json_data.get('info') == None:
        return False
    if json_data.get('images') == None:
        return False
    if json_data.get('annotation') == None:
        return False
    if json_data.get('licenses') == None:
        return False

    return True


