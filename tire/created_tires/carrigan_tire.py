from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear_sensor):
        self.tire_wear_sensor = tire_wear_sensor 

    def needs_service(self):
        need_service = False
        for tire_wear in self.tire_wear_sensor:
            if tire_wear >= 0.9:
                need_service = True

        return need_service
