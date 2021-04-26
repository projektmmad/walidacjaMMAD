import json

#tu wypisuje wszystkie wartości składni, by skrócić funkcję sprawdzania składni - do dokończenia
WZOR = {
    "image": {
        "id",
        "width",
        "height",
        "file_name",
        "license",
        "flickr_url"

    }
    ,
    "info": {
        "year",
        "version",
        "description",
        "contributor",
        "url",
        "date_created",
    }
}


# szybszy zapis wyszukania wartosci
def skladnia2_valid(json_file):
    for key, value in WZOR.items():
        if json_file[key]:
            print("jest!")

    print()



    json_data = json_file

    if json_data.get('info') == None:
        return False
    if json_data.get('images') == None:
        return False
    if json_data.get('annotation') == None:
        return False
    if json_data.get('license') == None:
        return False

    if json_data.get('info').get('year') == None:
        return False
    if json_data.get('info').get('version') == None:
        return False
    if json_data.get('info').get('description') == None:
        return False
    if json_data.get('info').get('contributor') == None:
        return False
    if json_data.get('info').get('url') == None:
        return False
    if json_data.get('info').get('date_created') == None:
        return False

    if json_data.get('image').get('id') == None:
        return False
    if json_data.get('image').get('width') == None:
        return False
    if json_data.get('image').get('height') == None:
        return False
    if json_data.get('image').get('file_name') == None:
        return False
    if json_data.get('image').get('license') == None:
        return False
    if json_data.get('image').get('flickr_url') == None:
        return False
    if json_data.get('image').get('coco_url') == None:
        return False
    if json_data.get('image').get('date_captured') == None:
        return False

    if json_data.get('license').get('id') == None:
        return False
    if json_data.get('license').get('name') == None:
        return False
    if json_data.get('license').get('url') == None:
        return False

 # wykrywanie obiektów
    if json_data.get('annotation').get('id') == None:
        return False
    if json_data.get('annotation').get('image_id') == None:
        return False
    if json_data.get('annotation').get('category_id') == None:
        return False
    if json_data.get('annotation').get('segmentation') == None:
        return False
    if json_data.get('annotation').get('area') == None:
        return False
    if json_data.get('annotation').get('bbox') == None:
        return False
    if json_data.get('annotation').get('iscrowd') == None:
        return False

    if json_data.get('categories').get('id') == None:
        return False
    if json_data.get('categories').get('name') == None:
        return False
    if json_data.get('categories').get('supercategory') == None:
        return False


# wykrrywanie punktow kluczowych
    if json_data.get('annotation').get('keypoints') == None:
        return False
    if json_data.get('annotation').get('num_keypoints') == None:
        return False

    if json_data.get('categories').get('keypoints') == None:
        return False
    if json_data.get('categories').get('skeleton') == None:
        return False


# segmentacja panoptyczna
    if json_data.get('annotation').get('image_id') == None:
        return False
    if json_data.get('annotation').get('file_name') == None:
        return False
    if json_data.get('annotation').get('segments_info') == None:
        return False

    if json_data.get('segment_info').get('id') == None:
        return False
    if json_data.get('segment_info').get('category_id') == None:
        return False
    if json_data.get('segment_info').get('area') == None:
        return False
    if json_data.get('segment_info').get('bboox') == None:
        return False
    if json_data.get('segment_info').get('iscrowd') == None:
        return False

    if json_data.get('categories').get('id') == None:
        return False
    if json_data.get('categories').get('name') == None:
        return False
    if json_data.get('categories').get('supercategory') == None:
        return False
    if json_data.get('categories').get('isthing') == None:
        return False
    if json_data.get('categories').get('color') == None:
        return False

# podpisy graficzne
    if json_data.get('annotation').get('id') == None:
        return False
    if json_data.get('annotation').get('image_id') == None:
        return False
    if json_data.get('annotation').get('caption') == None:
        return False

# densepose

    if json_data.get('annotation').get('id') == None:
        return False
    if json_data.get('annotation').get('image_id') == None:
        return False
    if json_data.get('annotation').get('category_id') == None:
        return False
    if json_data.get('annotation').get('is_crowd') == None:
        return False
    if json_data.get('annotation').get('area') == None:
        return False
    if json_data.get('annotation').get('bbox') == None:
        return False
    if json_data.get('annotation').get('dp_I') == None:
        return False
    if json_data.get('annotation').get('dp_U') == None:
        return False
    if json_data.get('annotation').get('dp_V') == None:
        return False
    if json_data.get('annotation').get('dp_x') == None:
        return False
    if json_data.get('annotation').get('dp_y') == None:
        return False
    if json_data.get('annotation').get('dp_maks') == None:
        return False

    return True


if __name__ == "__main__":
    with open("data.json") as file:
        try:
            data = json.load(file)
        except  JSONDecode:

    print("DONE")

    foo = skladnia2_valid(data)
    print(foo)
