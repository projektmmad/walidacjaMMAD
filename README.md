Projekt ma na celu zaprojektowanie, implementację i wykonanie narzędzi do walidacji formatu zbiorów danych używanych w dziedzinie AI. Jako podstawowe wspierane formaty wybrane zostały: Pascal, COCO.

Program odpala się w linuxowym command window. Głównym argumentem programu jest ścieżka do całego folderu VOC. Domyślne działanie programu opiera się  jednocześnie na walidacji struktury folderu VOC, składni pliku xml oraz składni pod kątem formatu Pascal. Jednakże jest możliwość oddzielnej walidacji przedtem wymienionych aspektów. 
Kluczowa jest zawartość folderu VOC, bowiem w folderze VOC MUSI być zamieszczony folder o nazwie 'Annotation' zawierający pliki xml. Do domyślnej walidacji potrzebny jest także folder o nazwie 'JPEGImages' zawierający obrazy. 

Ze względu na 3 opcje programu, aby go uruchomić należy wpisać:
1. "python3 pascal_validator.py "path_VOC" " w celu domyślnej walidacji
2. "python3 pascal_validator.py "path_VOC" -c only_pascal_xml " w celu walidacji tylko plików xml pod kątem formatu pascal
3. "python3 pascal_validator.py "path_VOC" -c only_syntax " w celu walidacji tylko składni xml

Brak jakiegokolwiek komunikatu oznacza, że zbiór jest poprawny.

Link do przykładowych datasetów:
http://host.robots.ox.ac.uk/pascal/VOC/
