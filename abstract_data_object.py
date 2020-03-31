import json
from abc import ABC, abstractmethod


class AbstractDataObject(ABC):
    def save(self, filename: str):
        with open(filename, 'w', encoding="utf8") as output:
            json.dump(self.__dict__, output, ensure_ascii=False, indent=4)

    @classmethod
    def load(cls, filename: str):
        with open(filename, 'rb') as input:
            return json.load(input)
