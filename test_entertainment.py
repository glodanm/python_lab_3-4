import unittest
from entertainments import *

class TestEntertainment(unittest.TestCase):
    
    def setUp(self):
        self.rollar_coaster = RollarCoaster()
        self.damn_wheel = DamnWheel()
        self.river_excurcion = RiverExcurcion()

    
    def test_rollar_coaster(self):

        expected_entertainments = RollarCoaster("Fury 325", 50, 150, 4, 0, "Metal", 8)

        self.assertEqual(expected_entertainments._name, "Fury 325")
        self.assertEqual(expected_entertainments._price, 50)
        self.assertEqual(expected_entertainments._height, 150)
        self.assertEqual(expected_entertainments._max_people, 4)
        self.assertEqual(expected_entertainments._max_num_of_kids, 0)
        self.assertEqual(expected_entertainments._material_type, "Metal")
        self.assertEqual(expected_entertainments._number_of_trolleys, 8)

    def test_damn_wheel(self):

        expected_entertainment = DamnWheel("London eye", 25, 150, 8, 0, 5, 135)

        self.assertEqual(expected_entertainment._name, "London eye")
        self.assertEqual(expected_entertainment._price, 25)
        self.assertEqual(expected_entertainment._height, 150)
        self.assertEqual(expected_entertainment._max_people, 8)
        self.assertEqual(expected_entertainment._max_num_of_kids, 0)
        self.assertEqual(expected_entertainment._number_of_circles, 5)
        self.assertEqual(expected_entertainment._construction_height, 135)

    def test_river_excurcion(self):

        expected_entertainment = RiverExcurcion("Finding nemo", 15, 100, 50, 10, 5000, 15.5)

        self.assertEqual(expected_entertainment._name, "Finding nemo")
        self.assertEqual(expected_entertainment._price, 15)
        self.assertEqual(expected_entertainment._height, 100)
        self.assertEqual(expected_entertainment._max_people, 50)
        self.assertEqual(expected_entertainment._max_num_of_kids, 10)
        self.assertEqual(expected_entertainment._route_length, 5000)
        self.assertEqual(expected_entertainment._length_of_boat, 15.5)


class TestEntertainmentManager(unittest.TestCase):

    def setUp(self):
    
        self.rollar_coaster = RollarCoaster()
        self.damn_wheel = DamnWheel()
        self.river_excurcion = RiverExcurcion()
        self.manager = EntertainmentManager()
        self.manager.add_entertainment(self.river_excurcion)
        self.manager.add_entertainment(self.rollar_coaster)
        self.manager.add_entertainment(self.damn_wheel)

    def test_find_by_age(self):
        expected_entertainments = [self.rollar_coaster, self.damn_wheel]
        res = self.manager.find_by_age(Age.ADULT)
        self.assertNotIn(self.river_excurcion, res)
        self.assertEqual(res, expected_entertainments)

    def test_sort_by_price(self):
        expected_entertainments = [self.river_excurcion, self.rollar_coaster, self.damn_wheel]
        res = self.manager.sort_by_price(entertainments = expected_entertainments)
        self.assertEqual(res, sorted(expected_entertainments, key=lambda s: s._price))

    def test_sort_by_max_num_of_kids(self):
        expected_entertainments = [self.river_excurcion, self.rollar_coaster, self.damn_wheel]
        res = self.manager.sort_by_max_num_of_kids(entertainments=expected_entertainments)
        self.assertEqual(res, sorted(expected_entertainments, key=lambda s: s._max_num_of_kids))


if __name__ == "__main__":
    unittest.main()
