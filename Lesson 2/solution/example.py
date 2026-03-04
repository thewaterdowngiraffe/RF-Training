class animal:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class primates(animal):
    def __init__(self, age, height, running_speed, jump_height, name="primates"):
        weight = (20/703)*(height ^ 2)
        super().__init__(name, age, height, weight)
        self.running_speed = running_speed
        self.jump_height = jump_height


class bird(animal):
    def __init__(self, age, height, weight, wing_span, name="bird"):
        super().__init__(name, age, height, weight)
        self.wing_span = wing_span
        self.flying_speed = (wing_span**2)/weight


class fish(animal):
    def __init__(self, age, height, weight, fin_count, name="fish"):
        super().__init__(name, age, height, weight)
        self.fin_count = fin_count
        self.swimming_speed = height * fin_count/weight


class human(primates):
    def __init__(self, age, height, running_speed, jump_height, name="human"):
        super().__init__(age, height, running_speed, jump_height, name)


class monkey(primates):
    def __init__(self, age, height, running_speed, jump_height, name="monkey"):
        super().__init__(age, height, running_speed, jump_height, name)


class hawk(bird):
    def __init__(self, age, height, weight, wing_span, name="hawk"):
        super().__init__(age, height, weight, wing_span, name)


class crow(bird):
    def __init__(self, age, height, weight, wing_span, name="crow"):
        super().__init__(age, height, weight, wing_span, name)


class cod(fish):
    def __init__(self, age, height, weight, fin_count, name="cod"):
        super().__init__(age, height, weight, fin_count, name)
