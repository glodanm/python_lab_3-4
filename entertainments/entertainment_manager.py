from typing import List
from .Entertainment import Entertainment, Age


class EntertainmentManager:
    def __init__(self):
        self.entertainments = []

    def add_entertainment(self, entertainment: Entertainment):
        self.entertainments.append(entertainment)

    def add_entertainments(self, entertainments: List[Entertainment]):
        self.entertainments += entertainments

    def sort_by_price(self, reverse: bool = False, entertainments: List[Entertainment] = None):
        return sorted(entertainments if entertainments else self.entertainments, key=lambda s: s._price, reverse=reverse)

    def sort_by_max_num_of_kids(self, reverse: bool = False, entertainments: List[Entertainment] = None):
        return sorted(entertainments if entertainments else self.entertainments, key=lambda s: s._max_num_of_kids,
                      reverse=reverse)

    def find_by_age(self, age: Age, entertainments: List[Entertainment] = None):
        return [x for x in (entertainments if entertainments else self.entertainments) if x._age == age]
