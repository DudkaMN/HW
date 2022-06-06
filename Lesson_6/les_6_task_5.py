class Stationery:
    title = 'Принадлежности'

    def draw():
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw():
        print('Пишем ручкой')


class Pencil(Stationery):
    def draw():
        print('Рисуем карандашом')


class Handle(Stationery):
    def draw():
        print('Красим маркером')


stationery_1 = Stationery
pen_1 = Pen
pencil_1 = Pencil
handle_1 = Handle
stationery_1.draw()
pen_1.draw()
pencil_1.draw()
handle_1.draw()
