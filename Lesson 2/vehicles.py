
class vehicle:
    def __init__(self, top_speed, passengers, vehicle_type, force, mass):
        self.top_speed = top_speed
        self.passengers = passengers
        self.vehicle_type = vehicle_type
        self.speed = 0
        self.force = force
        self.mass = mass
        self.done = False

    def get_speed(self):
        if self.done:
            return self.speed
        self.speed = min(
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
        super().__init__(top_speed, passengers, vehicle_type, force, mass)


class plane(vehicle):
    def __init__(self, top_speed=700, passengers=50, vehicle_type="plane", force=10000, mass=5670):
        super().__init__(top_speed, passengers, vehicle_type, force, mass)
