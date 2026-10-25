class Human:
    def __init__(self, name='Human'):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_names(self):
        if self.passengers != []:
            print(f"Імена пасажирів в бусіку: {self.brand} ")
            for passenger in self.passengers:
                print(passenger.name)

        else:
            print(f"В автомобілі {self.brand} пасажирів немає")

maks = Human("Maks")
elya = Human("Elya")
nazar = Human("Nazar")
auto = Auto("BMW")
auto.add_passenger(maks,elya,nazar)
auto.print_names()

messi = Human("Messi")
kostya = Human("Kostya")
ronaldo = Human("Ronaldo")
auto = Auto("Mercedes")
auto.add_passenger(messi,kostya,ronaldo)
auto.print_names()