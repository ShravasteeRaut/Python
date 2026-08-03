class Vehicle:

    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type

    def show_details(self):
        print("Brand:", self.brand)
        print("Fuel Type:", self.fuel_type)



class Car(Vehicle):

    def __init__(self, brand, fuel_type, model, seats):
        self.model = model
        self.seats = seats
        super().__init__(brand, fuel_type)


    def show_details(self):
        print("Model:", self.model)
        print("Seats:", self.seats)
        super().show_details()


    def start_engine(self):
        print(self.model, "engine started!!")



my_car = Car("BMW", "Koenisegg", "M4 Competition", 2)


my_car.show_details()
my_car.start_engine()


print("Is Car a subclass of Vehicle?", issubclass(Car, Vehicle))