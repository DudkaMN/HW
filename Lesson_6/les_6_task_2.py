class Road:

    def __init__(self, length, width, thickness, density=25):
        self._length = length
        self._width = width
        self.thickness = thickness
        self.density = density

    def weight(self):
        weight = (self._length * self._width * self.thickness * self.density)/1000
        return (weight)


road_1 = Road(5000, 20, 5)
r_1_w = road_1.weight()
print(r_1_w if road_1.weight() == ((road_1._width * road_1._length * road_1.thickness * road_1.density)/1000) else 'ошибка')
