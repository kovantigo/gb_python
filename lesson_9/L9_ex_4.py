from random import shuffle

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.__speed = speed
        self.__color = color
        self.__name = name
        self.__is_police = is_police

    def go(self):
        if (isinstance(self.__speed, int) or isinstance(self.__speed, float)) and self.__speed > 0:
            return f'{self.__name} is moving...'
        elif not(isinstance(self.__speed, int) or isinstance(self.__speed, float)):
            raise TypeError(f'TypeValue error')
        else:
            raise ValueError(f'Wrong value')

    def stop(self):
        if (isinstance(self.__speed, int) or isinstance(self.__speed, float)) and self.__speed == 0:
            return f'{self.__name} is standing...'
        elif not(isinstance(self.__speed, int) or isinstance(self.__speed, float)):
            raise TypeError(f'TypeValue error')
        else:
            raise ValueError(f'Wrong value')

    def turn(self):
        turn_list = ['left', 'right', 'forward', 'backward']
        shuffle(turn_list)
        return f'{self.__name} is going {turn_list[0]}'

    def show_speed(self):
        if isinstance(self.__speed, int) or isinstance(self.__speed, float):
            return self.__speed
        else:
            raise TypeError(f'TypeValue error')


class TownCar(Car):
    def show_speed(self):
        tc_speed = super().show_speed()
        if tc_speed > 60:
            return f'Overspeed: {tc_speed}'
        else:
            return f'Normal speed: {tc_speed}'


class WorkCar(Car):
    def show_speed(self):
        wc_speed = super().show_speed()
        if wc_speed > 40:
            return f'Overspeed: {wc_speed}'
        else:
            return f'Normal speed: {wc_speed}'

    def go(self):
        return super().go()

    def stop(self):
        return super().stop()

    def turn(self):
        return super().turn()

class PoliceCar(Car):
    def show_speed(self):
        if self._Car__is_police:
            return f'It is a police car: {super().show_speed()}'
        else:
            raise ValueError(f'no argument for police car')

    def go(self):
        return super().go()

    def stop(self):
        return super().stop()

    def turn(self):
        return super().turn()



try:
    #car = Car(61, 'yellow', 'Toyota')
    #print(car.go())
    #print(car.stop())
    #print(car.turn())
    #print(car.show_speed())
    #print(car._Car__name, car._Car__color)

    #tc = TownCar(60, 'green', 'Kia')
    #print(tc.show_speed())

    #wc = WorkCar(60, 'red', 'Fiat')
    #print(wc.show_speed())
    #print(wc.go())
    #print(wc.stop())
    #print(wc.turn())

    #pc = PoliceCar(150, 'blue', 'Mazda', True)
    #print(pc.show_speed())
    #print(pc.go())
    #print(pc.stop())
    #print(pc.turn())
except (TypeError, ValueError) as error:
    print(f'ERROR - {error}')
