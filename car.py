from servicable import Servicable

class Car(Servicable):
    def __init__(self, engine, battery):
        self._engine = engine
        self._battery = battery

    def needs_service(self):
        return self._engine.needs_service() or self._battery.needs_service()
