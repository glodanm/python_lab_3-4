from entertainments.entertainment_manager import EntertainmentManager
from entertainments import Age, RollarCoaster, DamnWheel, RiverExcurcion, Entertainment


class EntertainmentTest:
    def __init__(self):
        pass    
        
    def main(self):
        amusement = EntertainmentManager()
        amusement.add_entertainments([
            RollarCoaster("Fury 325", 50, 150, 4, 0, "Metal", 8),
            DamnWheel("London eye", 25, 150, 8, 0, 5, 135),
            RiverExcurcion("Finding nemo", 15, 100, 50, 10, 5000, 15.5)
        ])

        print('\nSorted by price\n\n' + '\n\n'.join([str(x) for x in amusement.sort_by_price()]), '\n')
        print('Sorted by max kids:\n\n' + '\n\n'.join([str(x) for x in amusement.sort_by_max_num_of_kids()]), '\n')
        print('Find by age:\n\n' + '\n\n'.join([str(x) for x in amusement.find_by_age(Age.ADULT)]), '\n')


if __name__ == '__main__':
    test = EntertainmentTest()
    test.main()
