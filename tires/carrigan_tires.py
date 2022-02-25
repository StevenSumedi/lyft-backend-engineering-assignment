from tires.tires import Tires


class CarriganTires():
    def __init__(self, array_of_tire_wear):
        self.array_of_tire_wear = array_of_tire_wear

    def needs_service(self):
        for value in self.array_of_tire_wear:
            if value >= 0.9:
                return True    
        return False
