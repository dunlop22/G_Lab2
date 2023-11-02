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
		self.figure = [[[[300, 300, 10], [500, 300, 10], [300, 500, 10]] , 'yellow'], [[[400, 450, 10], [600, 450, 5], [300, 400, 50]] , 'black']]
		self.windows = []   #Стек окон
	
	#ПОМЕНЯТЬ
	def getZ(self, fig, wind):
		
		coord = [[wind[0], wind[1]], [wind[0], wind[1] + wind[3]], [wind[0] + wind[2], wind[1] + wind[3]], [wind[0] + wind[2], wind[1]]]

		d = - (fig[0][0][0] * (fig[0][1][1] * fig[0][2][2] - fig[0][2][1] * fig[0][1][2]) + fig[0][1][0] * (fig[0][2][1] * fig[0][0][2] - fig[0][0][1] * fig[0][2][2]) + fig[0][2][0] * (fig[0][0][1] * fig[0][1][2] - fig[0][1][1] * fig[0][0][2]))
		a = fig[0][0][1] * (fig[0][1][2] - fig[0][2][2]) + fig[0][1][1] * (fig[0][2][2] - fig[0][0][2]) + fig[0][2][1] * (fig[0][0][2] - fig[0][1][2])
		b = fig[0][0][2] * (fig[0][1][0] - fig[0][2][0]) + fig[0][1][2] * (fig[0][2][0] - fig[0][0][0]) + fig[0][2][2] * (fig[0][0][0] - fig[0][1][0])
		c = fig[0][0][0] * (fig[0][1][1] - fig[0][2][1]) + fig[0][1][0] * (fig[0][2][1] - fig[0][0][1]) + fig[0][2][0] * (fig[0][0][1] - fig[0][1][1])
		z = -(d + a * coord[0][0] + b * coord[0][1]) / c

		mn = z
		mx = z

		for i in range(1, len(coord)):
			z = -(d + a * coord[i][0] + b * coord[i][1]) / c

			if z > mx:
				mx = z

			if z < mn:
				mn = z

		return mn, mx

	#ПОМЕНЯТЬ
	def draw_func(self, dr, win):
		ready  = True
		zmin, zmax = self.getZ(dr[0], win)
		n = 0

		for i in range(1, len(dr)):
			a, b = self.getZ(dr[i], win)
			
			if a > zmax:
				n = i
				zmax = b
				zmin = a

		pg.draw.rect(self.screen, dr[n][1], win)
			

	#ПОМЕНЯТЬ
	def check_angle(self, vert, x1, x2, y1, y2):
		x = vert[0]
		y = vert[1]

		if x >= x2 and y >= y1 and y < y2:
			t = 0
		elif x > x2 and y >= y2:
			t = 1
		elif x > x1 and x <= x2 and y >= y2:
			t = 2
		elif x <= x1 and y > y2:
			t = 3
		elif x <= x1 and y > y1 and y <= y2:
			t = 4
		elif x < x1 and y <= y1:
			t = 5
		elif x >= x1 and x < x2 and y <= y1:
			t = 6
		else:
			t = 7

		return t

	#ПОМЕНЯТЬ
	def check_ohvat(self, fig, wind):
		fv = fig[0]
		ang = []

		x1 = wind[0]
		x2 = wind[0] + wind[2]

		y1 = wind[1]
		y2 = wind[1] + wind[3]

		for vert in fv:
			ang.append(self.check_angle(vert, x1, x2, y1, y2))

		s = 0

		for i in range(len(ang)):
			a = ang[(i + 1) % len(ang)] - ang[i]

			if a > 4:
				a -= 8
			elif a < -4:
				a += 8
			elif abs(a) == 4:
				tx1 = fv[i][0]
				tx2 = fv[(i + 1) % len(fv)][0]

				ty1 = fv[i][1]
				ty2 = fv[(i + 1) % len(fv)][1]
				
				f = [fig[0].copy(), fig[1]]

				d = [tx1 + (y1 - ty1) * (tx2 - tx1) / (ty2 -ty1), y1]
				t = self.check_angle(d, x1, x2, y1, y2)

				if (t == ang[i] or t == ang[(i + 1) % len(ang)]):
					d = [tx1 + (y2 - ty1) * (tx2 - tx1) / (ty2 -ty1), y2]
					t = self.check_angle(d, x1, x2, y1, y2)

					if (t == ang[i] or t == ang[(i + 1) % len(ang)]):
						d = [x1, ty1 + (ty2 - ty1) * (x1 - tx1) / (tx2 - tx1)]
						t = self.check_angle(d, x1, x2, y1, y2)

						if (t == ang[i] or t == ang[(i + 1) % len(ang)]):
							d = [x2, ty1 + (ty2 - ty1) * (x2 - tx1) / (tx2 - tx1)]
							t = self.check_angle(d, x1, x2, y1, y2)
				
				f[0].insert(i + 1, d)
				return self.check_ohvat(f, wind)

			s += a

		return s % 8 == 0 and s != 0



	def check_rezult(self, figura, wind):
		rezult = False
		rebra = []

		for i in range(len(figura)):
			rebra.append([])
			rebra[i].append(figura[0][i])
			rebra[i].append(figura[0][(i + 1) % len(figura)])
		j = 0
		while rezult == False and j < len(rebra):
			
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
						ck0 = c0;
						ck1 = c1;
						if (k < 3):
							ck1 += wind[3]

						if (k > 1):
							ck0 += wind[2]
							
						if last * n < 0:
							rezult = True
							break
						if last == 0:
							last = n
			j += 1
				
		return rezult

	def control(self):
		
		for p in range(1024):
			time.sleep(0.000000003)
			if (len(self.windows) != 0):
				wind = self.windows.pop()
				size = wind[2]
				num = 0
				vnesh = 0
				draw = []

				while (num < len(self.figure)):
					figura = self.figure[num]
					
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
							draw.append(figura)
						else:
							if self.check_rezult(figura, wind):
								draw.append(figura)
							elif self.check_ohvat(figura, wind):
								draw.append(figura)
						#else:
							#if 

					num += 1

				
				
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
				else:
					if (len(draw) > 0):
						self.draw_func(draw, wind)
					else:
						pg.draw.rect(self.screen, (255, 155, 155), wind)



					

						

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