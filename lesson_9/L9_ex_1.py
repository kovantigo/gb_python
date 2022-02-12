from time import sleep

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        while True:
            for key, value in self.__color.items():
                print(key)
                sleep(value)

traf_dict = {'red': 7, 'yellow': 2, 'green': 7}
traf = TrafficLight(traf_dict)
traf.running()


