class TrainCar:
    MAX_PASSENGERS = 10

    def __init__(self, number):
        self.number = number
        self.passengers = []

    def add_passenger(self, name, destination, place):
        if len(self.passengers) >= TrainCar.MAX_PASSENGERS:
            raise ValueError("The traincar is full")
        self.passengers.append({"name": name, "destination": destination, "place": place})

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        passengers_str = "\n".join(
            [f'name: {p["name"]}, destination: {p["destination"]}, place: {p["place"]}' for p in self.passengers])
        return f"Carriage {self.number} ({len(self)} passengers):\n{passengers_str}"


class Train:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def __len__(self):
        return len(self.cars) - 1 

    def __str__(self):
        cars_str = "\n".join([str(car) for car in self.cars])
        return f"Train ({len(self)} cars):\n{cars_str}"


train = Train()

locomotive = TrainCar("L")
train.add_car(locomotive)

car1 = TrainCar(1)
car1.add_passenger("John Matrix", "London", 1)
car1.add_passenger("Jane Smith", "New Hampshire", 2)
train.add_car(car1)

car2 = TrainCar(2)
car2.add_passenger("Bobi Mo", "Hogwartz", 5)
train.add_car(car2)

print(train)
print(len(train))
print(len(car1))
