from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear_sensor):
        self.tire_wear_sensor = tire_wear_sensor 

    def needs_service(self):
        return sum(self.tire_wear_sensor) >= 3
