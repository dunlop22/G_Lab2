import pygame as pg

class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1920, 1080     #Разрешение
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2     #Поверхность для отрисовки
        self.FPS = 60       #Кадры в секунду
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

    def create_objects(self):
        self.object = object_3d(self)

    def new_position(self, fig_position):
        new_position = []
        for i in range(len(fig_position)):
            new_position .append([fig_position[i][0], fig_position[i][1]])
        return new_position

    def draw(self): #Отрисовка
        self.screen.fill(pg.Color('darkslategray')) #Цвет заднего фона
        pg.draw.rect(self.screen, (255, 255, 255), 
                 (256, 256, 514, 514), 1)
        fig1_position = [[300, 300, 10], [500, 300, 10], [300, 500, 10]]
        fig1_color = 'yellow'
        pg.draw.polygon(self.screen, 'black', self.new_position(fig1_position), 1)

    def run(self):
        while True:
            self.draw() #Отрисовка объектов
            [exit() for i in pg.event.get() if i.type == pg.QUIT]   #Проверка на выход из приложения
            pg.display.set_caption(str("Лабораторная работа №2, Голиков"))  #Заголовок приложения 
            pg.display.flip()
            self.clock.tick(self.FPS)   #Обновление поверхности отрисовки
            
            

if __name__ == '__main__':
    app = SoftwareRender()  #Экземпляр класса
    app.run()   #Запуск