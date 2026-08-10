from abc import ABC, abstractmethod


class SmartDevice(ABC):

    @abstractmethod
    def command(self):
        pass


class SmartCar(SmartDevice):

    def command(self):
        print("Smart Car: Starting the engine and driving.")


class SmartBoat(SmartDevice):

    def command(self):
        print("Smart Boat: Starting the motor and sailing.")


class SmartAirplane(SmartDevice):

    def command(self):
        print("Smart Airplane: Starting the engines and taking off.")



car = SmartCar()
boat = SmartBoat()
airplane = SmartAirplane()



devices = [car, boat, airplane]

for device in devices:
    device.command()