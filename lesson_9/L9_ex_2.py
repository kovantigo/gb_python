class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def weight_asphalt(self, weight, depth):
        print(self._lenght * self._width * weight * depth // 1000)

asphalt = Road(20, 5000)
asphalt.weight_asphalt(25, 5)
