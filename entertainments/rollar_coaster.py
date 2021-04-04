from .Entertainment import Entertainment, Age


class RollarCoaster(Entertainment):
    def __init__(self, name: str = "", price: int = 0, height: int = 0, max_people: int = 0, max_num_of_kids: int = 0,
                 material_type: str = "", number_of_trolleys: int = 0):
        super().__init__(Age.ADULT, name, price, height, max_people, max_num_of_kids)
        self._material_type = material_type
        self._number_of_trolleys = number_of_trolleys

    def __str__(self):
        res3 = super().__str__() + f"\nMaterial_type: {self._material_type}\nNumbers_of_trolleys: {self._number_of_trolleys}"
        return res3
