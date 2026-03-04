
class vehicle:
    def __init__(self, top_speed, passengers, vehicle_type, force, mass):
        self.top_speed: float = top_speed
        self.passengers = passengers
        self.vehicle_type = vehicle_type
        self.speed = 0
        self.force = force
        self.mass = mass
        self.done = False

    def get_speed(self) -> float | int:
        if self.done:
            return self.speed
        self.speed: float | int = min(
            (
                (
                    self.force/self.mass
                )*0.25
            )+self.speed, self.top_speed)
        return self.speed


class car(vehicle):
    def __init__(self, top_speed=140, passengers=3, vehicle_type="car", force=3000, mass=1000):
        super().__init__(top_speed, passengers, vehicle_type, force, mass)


class motorcycle(vehicle):
    def __init__(self, top_speed=200, passengers=1, vehicle_type="motorcycle", force=2500, mass=227):
        """__init__ _summary_

        _extended_summary_

        :param top_speed: _description_, defaults to 200
        :type top_speed: int, optional
        :param passengers: _description_, defaults to 1
        :type passengers: int, optional
        :param vehicle_type: _description_, defaults to "motorcycle"
        :type vehicle_type: str, optional
        :param force: _description_, defaults to 2500
        :type force: int, optional
        :param mass: _description_, defaults to 227
        :type mass: int, optional
        """
        super().__init__(top_speed, passengers, vehicle_type, force, mass)


class plane(vehicle):
    def __init__(self, top_speed: int | float = 700, passengers=50, vehicle_type="plane", force=10000, mass=5670):
        super().__init__(top_speed, passengers, vehicle_type, force, mass)
