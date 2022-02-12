class Stationery:
    title = ''
    def draw(self):
        print(f'Запуск отрисовки...')

class Pen(Stationery):
    title = 'ручка'
    def draw(self):
        print(f'Используется {self.title}')

class Pencil(Stationery):
    title = 'карандаш'
    def draw(self):
        print(f'Используется {self.title}')

class Handle(Stationery):
    title = 'маркер'
    def draw(self):
        print(f'Используется {self.title}')


pen = Pen()
pencil = Pencil()
handle = Handle()

for item in [pen, pencil, handle]:
    item.draw()