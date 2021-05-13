import json

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
    ,
    "image":{
        "id",
        "width",
        "height",
        "file_name",
        "license",
        "flickr_url",
        "coco_url",
        "date_captured",
        "date_captured"
    }
    ,
    "license":{
        "id",
        "name",
        "url",
    }
}

WZOR_OBIEKTOWE = {
    # wykrywanie obiektów
    "annotation":{
        "id",
        "image_id",
        "category_id",
        "segmentation",
        "area",
        "bbox",
        "iscrowd",
    }
    ,
    "categories":{
        "id",
        "name",
        "supercategory"
    }
}

WZOR_PUNKTY_KLUCZOWE = {
    # wykrrywanie punktow kluczowych
    "annotation":{
        "keypoints",
        "num_keypoints",
    }
    ,
    "categories":{
        "keypoints",
        "skeleton",
    }
}

WZOR_SEGMENTACJA_PANOPTYCZNA = {
    # segmentacja panoptyczna
    "anntation":{
        "image_id",
        "file_name",
        "segments_info",
    }
    ,
    "segmentt_info":{
        "id",
        "category_id",
        "area",
        "bbox",
        "iscrowd"
    }
    ,
    "categories":{
        "id",
        "name",
        "supercategory",
        "isthing",
        "color"
    }
}

WZOR_PODPISY_GRAFICZNE = {
    # podpisy graficzne
    "annotation":{
        "id",
        "image_id",
        "caption"
    }
}

WZOR_DENSEPOSE = {
    # densepose
    "annotation":{
        "id",
        "image_id",
        "category_id",
        "is_crowd",
        "area",
        "bbox",
        "dp_I",
        "dp_U",
        "dp_V",
        "dp_x",
        "dp_y",
        "dp_maks"
    }
}


# korzystamy z kluczy
def skladnia_valid(json_file):
    for key, value in WZOR.items():
        if json_file[key]:
            print("jest!")
            
#jakiego typu jest adnotacja i dopiero sprawdzać kolejne wzory jak jest możliwość
#czy możliwe by wtąpiły 2 typy adnotacji
#poniższy skrypt jest ok ale bez sensu sprawdzać wszystko jak może nie być potrzeby

    for key, value in WZOR_OBIEKTOWE.items():
        if json_file[key]:
             print("jest obiektowe!")

    for key, value in WZOR_PUNKTY_KLUCZOWE.items():
        if json_file[key]:
             print("jest punkty kluczowe!")

    for key, value in WZOR_SEGMENTACJA_PANOPTYCZNA.items():
        if json_file[key]:
             print("jest segmentacja panoptyczna!")

    for key, value in WZOR_PODPISY_GRAFICZNE.items():
        if json_file[key]:
             print("jest podpisy graficzne!")

    for key, value in WZOR_DENSEPOSE.items():
        if json_file[key]:
             print("jest densepose!")

    print()



if __name__ == "__main__":
    with open("data.json") as file:
        try:
            data = json.load(file)
        except  JSONDecode:

    print("DONE")

    foo = skladnia_valid(data)
    print(foo)
