
### Engine Controls

# Throttle
def set_engine_throttle(throttle: float = 0):
    """
    Throttle setpoint 0 to 1.
    """
    raise NotImplementedError

def get_engine_throttle():
    """
    Retuns the throttle setpoint (float) between 0 and 1 and current thrust (flaot) experessed in N.
    """
    return (throttle_setpoint, current_thrust) # touple of float of the throttle and current float of the thrust

def set_engine_thrust_setpoint(thrust: float = 0):
    """
    Takes a setpoint thrust and automatically calculates and implements the correct throttle to reach the thrust setpoint.
    Note that this will lock the engine thust control to thust setpoint and controlling thust should only be done using this function.
    If *set_egnine_throttle* is used, it will deactivate thrust control and override the throttle setpoint.
    Thust is expressed in N (Newton)
    """
    raise NotImplementedError

def get_engine_thrust():
    return current_thrust # float of the current thrust in newton

# Rotation
def set_engine_gimbal(rotation_angle: float = 0, angle_intensity: float = 0):
    """
    rotation_anmle - is a 0 to 360 degree angle of the rotation, seen from a top down view.
    angle_intensity - along the circular path (cone shaped) rotation for the given angle, angle_intensity specifies how far out from the center/origin to the border (5deg)

    Note that both rotation_angle and angle_intensity are floats with degrees, from 0 to 360 and 0 to 5.
    """
    raise NotImplementedError

def get_engine_gimbal():
    """
    Returns the CURRENT position of the engine gimbal rotation at any given time.
    """
    return (rotaiton_angle, angle_intensity) # touple of angle and intensity

def set_engine_gimbal_speed(speed: float = 1)


# Ignition / Engine Status
def set_engine_ignition():
    """
    Igniting the engine with one command, make sure to first set a throttle or thrust setpoint. If the throttle is set to zero, the ignition attempt will fail.
    Call set engine ignition only once, however ignition will not trigger if the engine is running.
    """
    raise NotImplementedError

def get_engine_status():
    """
    Returns the status of the engine with the following information
    * ignited/running - A boolean stating whether the engine is running or not
    * gimbal moving - A boolean returning the status of the gimbal pistons. If they are moving or static. (v')
    """
    return (engine_running, gimbal_movement)


### Position and Rotation

# Current Positioning
def get_rocket_position():
    """
    Returns the current position of the rocket in coordinates.
    x - float of x position (horizontal)
    y - flaot of y position (horizontal)
    z - float of z position (height / vertical)
    """
    return (x, y, z)

def get_rocket_velocity():
    return (rocket_velocity_x, rocket_velocity_y, rocket_velocity_z) # Rocket velocity as a float of meters per second.

def get_rocket_acceleration():
    return (rocket_acceleration_x, rocket_acceleration_y, rocket_acceleration_z) # bro, if you don't know this you shouldn't be doingthis shit

def get_rocket_rotation():
    """
    Returns the rockets rotation in umm....
    """
    return (do it later gang)


def get_rocket_trajectory(step: float = 0.01):
    """
    Returns an array of tuple positions (x, y, z) for the trajectory at every step.
    Step length says how many meters there should be between each step.

    A 1m section with 0.01 step length will give 100 steps with (x,y,z) coordinates.
    """
    return [..., (x,y,z), ...]


### Sensors / Data

# Altitude
def get_data_altitude():
    return altitude # float aka z coordinate for position (over sealevel)

def get_data_pressure():
    return outside_pressure # float, pascal or some shit, let me cook gang!

def get_data_temperature():
    return outside_temperature # flaot, kelvin

def get_data_engine_fuel_capacity():
    return fuel_capacity # total fuel capacity

def get_data_engine_fuel_remaining():
    return remaining_fuel # float of remaining fuel in kilograms

def get_data_engine_oxidizer_capacity():
    return oxidizer_capacity # float total oxidizer capacity

def get_data_engine_oxidizer_remaining():
    return remianing_oxidizer # float of remaining oxidizer in kilograms

def get_data_engine_temperature():
    return engine_temp # flaot of temp in kelvin
