class Flashligth():
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def toggle(self):
        self.is_on = not self.is_on

class Battery():
    STATUS= ["ok", "charging", "low", "unknown"]
    def __init__(self):
        self.power = None
        self.current_status = self.STATUS[-1]

class Cellphone():
    def __init__(self):
        self.flashlight = Flashligth()
        self.battery = Battery()


if __name__ == "__main__":
    cell = Cellphone()

