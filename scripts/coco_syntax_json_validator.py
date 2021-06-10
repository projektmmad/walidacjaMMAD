import json
{ "$schema": "http://json-schema.org/draft-07/schema#" }

        def syntax_validator(path, filename):
            try:
                with open("data.json") as json_file:
                    data = json.load(file)
                    print("Plik ma poprawny format")
            except ValueError as e:
                print("Plik jest złego formatu")
                return False

            if not isinstance(data, dict):
                raise ParseError("Expected an object!")

             try:
            name = data['data.json']
            except KeyError:
                raise ParseError('Expected a name')

            if not isinstance(name, dict):
                raise ParseError("Expected an object for name")

            try:
             first = name['data.json']
            except KeyError:
                 raise ParseError("Expected a first name")

            if not isinstance(first, basestring):
                raise ParseError("Expected first name to be a string")

             if first == '':
                raise ParseError("Expected non-empty first name")

if __name__ == "__main__":
    with open("data.json") as file:
        try:
            data=json.load(file)
            except
