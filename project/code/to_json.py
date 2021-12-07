import json
from price import pr
from codes import cd

def convertToJSON():
    with open("price.json", "w") as write_file:
        json.dump(pr, write_file)


def convertInJSON():
    with open("codes.json", "w") as write_file:
        json.dump(cd, write_file)
