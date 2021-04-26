#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

if __name__ == "__main__":

    def syntax_validator(path, filename):
        try:
            with open("data.json") as json_file:
                data = json.load(file)
                print("Plik ma poprawny format")
        except Exception as e:
            print("Plik jest złego formatu")
            return False