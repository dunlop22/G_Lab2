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

    def draw(self): #Jтрисовка
        self.screen.fill(pg.Color('darkslategray')) #Цвет заднего фона

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