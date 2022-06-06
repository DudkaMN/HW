from random import randint


class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        self.speed = randint(20, 80)
        print(f'Car is traveling at a speed of  {self.speed} mph')

    def stop(self):
        self.speed = 0
        print('Car is stopped')

    def tern_detektor(self):
        detektor = randint(1, 3)
        print('Car turned ' + ('left' if detektor == 1 else 'right'))

    def show_speed(self):
        print(f'Current auto speed {self.speed}')


class TownCar(Car):
    '''Town Car'''

    def show_speed(self):
        print(f'Current auto speed {self.speed}')
        if self.speed > 60:
            print(f'Speed exceeded by {self.speed - 60}')
            self.speed = 60


class SportCar(Car):
    '''Sport Car'''


class WorcCar(Car):
    '''Worc Car'''

    def show_speed(self):
        print(f'Current auto speed {self.speed}')
        if self.speed > 40:
            print(f'Speed exceeded by {self.speed - 40}')
            self.speed = 40


class PoliceCar(Car):
    '''Police Car'''
    is_police = True


def car_test(car):
    print(f'{car.name}, {car.__class__}')
    car.go()
    car.tern_detektor()
    car.show_speed()
    print(f'{car.speed}, {car.color}, {car.name}, {car.is_police}')
    car.stop()
    car.show_speed()
    print('\n')


t_c_1 = TownCar(0, 'green', 'Lada')
w_c_1 = WorcCar(0, 'black', 'GAZ')
s_c_1 = SportCar(0, 'red', 'Ferrari')
p_c_1 = PoliceCar(0, 'blue', 'UAZ')
car_test(t_c_1)
car_test(w_c_1)
car_test(s_c_1)
car_test(p_c_1)
