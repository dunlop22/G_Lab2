import pygame as pg
import time

class SoftwareRender:
	def __init__(self):
		pg.init()
		self.RES = self.WIDTH, self.HEIGHT = 1920, 1080     #Разрешение
		self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2     #Поверхность для отрисовки
		self.FPS = 60       #Кадры в секунду
		self.screen = pg.display.set_mode(self.RES)
		self.clock = pg.time.Clock()
		self.figure = [[[[300, 300, 10], [500, 300, 10], [300, 500, 10]] , 'yellow']]
		self.windows = []   #Стек окон

	def create_objects(self):
		self.object = object_3d(self)

	def check_rezult(self, figura, wind):
		rebra = []

		for i in range(len(figura)):
			rebra.append([])
			rebra[i].append(figura[i])
			rebra[i].append(figura[(i + 1) % len(figura)])
		j = 0
		while rezult == false and j < len(rebra):
			
			if not (rebra[j][0][0] > wind[0] + wind[2] and rebra[j][1][0] > wind[0] + wind[2] or rebra[j][0][0] < wind[0] and rebra[j][1][0] < wind[0] or rebra[j][0][1] > wind[1] + wind[3] and rebra[j][1][1] > wind[1] + wind[3] or rebra[j][0][1] < wind[1] and rebra[j][1][1] < wind[1]):
				xr = rebra[j][1][0] - rebra[j][0][0]
				yr = rebra[j][1][1] - rebra[j][0][1]
				if xr == 0:
					if (wind[0] - rebra[j][0][0]) * (wind[0] + wind[2] - rebra[j][0][0]) < 0:
						rezult = True
				elif yr == 0:
					if (wind[1] - rebra[j][1][1]) * (wind[1] + wind[3] - rebra[j][1][1]) < 0:
						rezult = True
				else:
					m = yr / xr
					b = rebra[j][1][1] - m * rebra[j][1][0]
					last = wind[1] - m * wind[0] - b
					for k in range(1, 4):
						c0 = wind[0]
						c1 = wind[1]
						#if ():
						n = c1 - m * c0 - b
						n = c[k][1] - m * c[k][0] - b
						if last * n < 0:
							rezult = True
							break
						if last == 0:
							last = n
			j += 1
				
		return rezult

	def control(self):
		
		for p in range(1024):
			time.sleep(0.000003)
			if (len(self.windows) != 0):
				wind = self.windows.pop()
				size = wind[2]
				i = 0
				vnesh = 0
				vnutr = []

				while (i < len(self.figure)):
					figura = self.figure[i]
					
					x_min = figura[0][0][0]
					x_max = figura[0][0][0]
					y_min = figura[0][0][1]
					y_max = figura[0][0][1]

					for i in range(len(figura[0])):
						if (figura[0][i][0] < x_min):
							x_min = figura[0][i][0]
						if (figura[0][i][0] > x_max):
							x_max = figura[0][i][0]
						if (figura[0][i][1] < y_min):
							y_min = figura[0][i][1]
						if (figura[0][i][1] > y_max):
							y_max = figura[0][i][1]



					#фигура внешняя
					if x_min >= wind[0] + wind[2] or x_max <= wind[0] or y_min >= wind[1] + wind[3] or y_max <= wind[1]:
						vnesh += 1

					elif size == 1 and vnesh != len(self.figure):
						#фигура внутренняя
						if x_min >= wind[0] and x_max <= wind[0] + wind[2] and y_min >= wind[1] and y_max <= wind[1] + wind[3]:
							vnutr.append(figura)
						#else:
							#if 

				
				
				if vnesh == len(self.figure):
					pg.draw.rect(self.screen, (255, 155, 155), wind)
				elif (size > 1):
					size /= 2
					w1 = [wind[0], wind[1], size, size]
					pg.draw.rect(self.screen, (64, 128, 255), w1, 1)
					self.windows.append(w1.copy());
					w1[0] += size
					pg.draw.rect(self.screen, (64, 128, 255), w1, 1)
					self.windows.append(w1.copy());
					w1[1] += size
					pg.draw.rect(self.screen, (64, 128, 255), w1, 1)
					self.windows.append(w1.copy());
					w1[0] -= size
					pg.draw.rect(self.screen, (64, 128, 255), w1, 1)
					self.windows.append(w1.copy());
				#else:


					

						

	def new_position(self, fig_position):
		new_position = []
		for i in range(len(fig_position)):
			new_position.append([fig_position[i][0], fig_position[i][1]])
		return new_position

	def draw(self): #Отрисовка
		self.screen.fill(pg.Color('darkslategray')) #Цвет заднего фона
		pg.draw.rect(self.screen, (255, 255, 255), 
				 (256, 256, 516, 516), 1)
		
		for figura in self.figure:
			pg.draw.polygon(self.screen, 'black', self.new_position(figura[0]), 1)
			self.windows.append([258, 258, 512, 512]); #


	def run(self):
		self.draw() #Отрисовка объектов
		while True:
			
			[exit() for i in pg.event.get() if i.type == pg.QUIT]   #Проверка на выход из приложения
			pg.display.set_caption(str("Лабораторная работа №2, Голиков"))  #Заголовок приложения 
			pg.display.flip()
			self.clock.tick(self.FPS)   #Обновление поверхности отрисовки
			self.control()
			
if __name__ == '__main__':
	app = SoftwareRender()  #Экземпляр класса
	app.run()   #Запуск