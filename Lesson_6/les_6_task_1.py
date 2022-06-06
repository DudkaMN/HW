import time


class TrafficLight:
    color = 'red'

    def running():
        while True:
            color = 'red'
            print(color)
            time.sleep(7)
            color = 'yellow'
            print(color)
            time.sleep(2)
            color = 'green'
            print(color)
            time.sleep(15)


t_l = TrafficLight

t_l.running()
