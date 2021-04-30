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
    ,
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
    ,
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
    ,
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
    ,
    # podpisy graficzne
    "annotation":{
        "id",
        "image_id",
        "caption"
    }
    ,
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


def skladnia2_valid(json_file):
    for key, value in WZOR.items():
        if json_file[key]:
            print("jest!")

    print()


if __name__ == "__main__":
    with open("data.json") as file:
        try:
            data = json.load(file)
        except  JSONDecode:

    print("DONE")

    foo = skladnia2_valid(data)
    print(foo)
