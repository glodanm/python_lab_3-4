from enum import Enum


class Age(Enum):
    KIDS = 0
    ADULT = 1
    ALL_AGES = 2


class Entertainment:

    def __init__(self, age: Age, name: str = "", price: int = 0, height: int = 0, max_people: int = 0, max_num_of_kids: int = 0):
        self._name = name
        self._age = Age(age)
        self._price = price
        self._height = height
        self._max_people = max_people
        self._max_num_of_kids = max_num_of_kids

    def __str__(self):
        res1 = f"Name: {self._name}\nPrice: {self._price}\nHeight: {self._height}\nMax_people: {self._max_people}\nMax num of kids: {self._max_num_of_kids}"
        return res1

    def get_type(self):
        return self._age
