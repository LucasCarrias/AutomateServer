import bobo
from http import HTTPStatus


class Flashligth():
    def __init__(self):
        self.is_on = False

    def set_on(self, turn_on):
        self.is_on= turn_on

    def toggle(self):
        self.is_on = not self.is_on

    def get_status(self):
        return {
            "isOn":self.is_on
        }

class Battery():
    MODES = ["normal", "charging", "unknown"]
    def __init__(self):
        self.power = ""
        self.mode = self.MODES[-1]

    def set_mode(self, mode_index):
        self.mode = self.MODES[mode_index]

    def set_power(self, value):
        self.power = value

    def get_status(self):
        return {
            "mode": self.mode,
            "power": self.power
        }

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
    if not type(turn_on) is bool:
        raise RuntimeError(HTTPStatus(400))
    cellphone.flashlight.set_on(turn_on)
    return {
        "isOn": cellphone.flashlight.is_on
    }


@bobo.get('/battery/:info', content_type='application/json')
def battery(info=None):
    if info == "power":
        return cellphone.battery.power
    elif info == "mode":
        return cellphone.battery.mode
    return cellphone.battery.get_status()


@bobo.post('/battery/power', content_type='application/json')
def battery_power_post(value):
    cellphone.battery.set_power(value)
    return cellphone.battery.get_status()


@bobo.post('/battery/mode', content_type='application/json')
def battery_mode_post(value):
    cellphone.battery.set_mode(value)
    return cellphone.battery.get_status()

