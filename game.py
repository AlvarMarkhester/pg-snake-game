import pygame as pg
import sys
import random
from settings import *
from sprites import *

class Game:
	def __init__(self):
		#init game windows etc
		pg.init()
		pg.font.init()
		self.myfont = pg.font.SysFont('Calibri', 50)
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()


	def new(self):
		# start a new game
		self.all_sprites = pg.sprite.Group()
		self.foods = pg.sprite.Group()
		self.player = Player(self, 15, 15)
		self.food = Food(self, random.randrange(0, GRIDWIDTH), random.randrange(0, GRIDHEIGHT))
		g.run()

	def run(self):
		# game loop
		while True:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()
			self.player.move()

	def quit(self):
		pg.quit()
		sys.exit()

	def update(self):
		# game loop update
		self.all_sprites.update()

	def events(self):
		# game loop events
		for event in pg.event.get():
        # check for closing window
			if event.type == pg.QUIT:
				self.quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.quit()
				if event.key == pg.K_LEFT or event.key == pg.K_a:
					self.player.goLeft()
				if event.key == pg.K_UP or event.key == pg.K_w:
					self.player.goUp()
				if event.key == pg.K_RIGHT or event.key == pg.K_d:
					self.player.goRight()
				if event.key == pg.K_DOWN or event.key == pg.K_s:
					self.player.goDown()
				

	def draw_grid(self):
		for x in range(0, WIDTH, TILESIZE):
			pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
		for y in range(0, HEIGHT, TILESIZE):
			pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

	def draw_game_score(self):
		self.gamescore = self.myfont.render(f"Gamescore: {self.player.gamescore}" , False, YELLOW)
		self.screen.blit(self.gamescore,(50,25))

	def draw(self):
		# game loop draw
		self.screen.fill(BGCOLOR)
		self.draw_grid()
		self.all_sprites.draw(self.screen)
		self.player.drawSnakeLength()
		self.draw_game_score()
		# flipping display after drawing
		pg.display.flip()

	def show_start_screen(self):
		pass

	def show_go_screen(self):
		pass

g = Game()
g.show_start_screen()
while True:
	g.new()
	g.show_go_screen()

pg.quit()