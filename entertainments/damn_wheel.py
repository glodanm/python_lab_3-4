from .Entertainment import Entertainment, Age


class DamnWheel(Entertainment):
    def __init__(self, name: str = "", price: int = 0, height: int = 0, max_people: int = 0,  max_num_of_kids: int = 0,
                 number_of_circles: int = 0, construction_height: float = 0):
        super().__init__(Age.ADULT, name, price, height, max_people, max_num_of_kids)
        self._number_of_circles = number_of_circles
        self._construction_height = construction_height

    def __str__(self):
        res4 = super().__str__() + f"\nNumbers_of_circles: {self._number_of_circles}\nConstruction_height: {self._construction_height}"
        return res4
