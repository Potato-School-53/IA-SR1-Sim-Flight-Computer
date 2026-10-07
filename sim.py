from CDF import pycdf as cdf


### Setup

# Initialize environment from env.json
# Load rocket model from rocket.step
# Initialize rocket in sim space
# Initialize engine submodel in rocket
# Specialize / Define enigne limits



def ignition():
    # Implement engine ignition simulation for Lars
    raise NotImplementedError


class FuelType:
    def __init__(self):
        self.LCH4 = {
            "molecule": "CH4",
            "temperature": 100,
            "density": 423,
        }
        self.LOX = {
            "molecule": "O2",
            "temperature": 90,
            "density":  1141
        }

    def CH4_rho(self, T=100, P=101325, M=16.04):
        R = cdf.constants.R
        rho = (P * M) / (R * T)
        return rho

    def LOX_rho(self, T=90, P=60000000, M=31.998):
        R = cdf.constants.R
        rho = (P * M) / (R * T)
        return rho


class Engine:
    def __init__(self):
        self.fuel = FuelType.LCH4
        self.oxidizer = FuelType.LOX

        self.fuel_pump_power = 0
        self.oxidizer_pump_power = 0

    def fuel_oxidizer_ratio_converter(self, throttle: float = 0):
        fuel_ratio = throttle ^ 2
        oxidizer_ratio = throttle^2 / 2
        
        return self.fuel_pump_power * fuel_ratio, self.oxidizer_pump_power * oxidizer_ratio


class Rocket:
    def __init__(self, rocketObject):
        self.position = rocketObject.position.to([1,3])
        self.rotation = rocketObject.rotation.to([1,3])
        self.velocity = rocketObject.velocity.to([1,3])
        self.acceleration = rocketObject.acceleration.to([1,3])
        self.

    def 
