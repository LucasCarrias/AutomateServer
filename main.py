import bobo

class Flashligth():
    def __init__(self):
        self.is_on = False

    
    def set_on(self, turn_on):
        self.is_on= turn_on

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


cellphone = Cellphone()

@bobo.get('/flashlight', content_type='application/json')
def flahslight_get():
    return {
        "isOn": cellphone.flashlight.is_on
    }

@bobo.post('/flashlight', content_type='application/json')
def flahslight_post(turn_on):
    print(turn_on)
    if not type(turn_on) is bool:
        raise RuntimeError("The value must be a bool")

    cellphone.flashlight.set_on(turn_on)

    return {
        "isOn": cellphone.flashlight.is_on
    }

@bobo.get('/battery', content_type='application/json')
def battery():
    return {
        "status": cellphone.battery.current_status,
        "power": cellphone.battery.power
    }