from tires.tires import Tires


class OctoprimeTires():
    def __init__(self, array_of_tire_wear):
        self.array_of_tire_wear = array_of_tire_wear

    def needs_service(self):
        if sum(self.array_of_tire_wear) >= 3:
            return True    
        else:
            return False