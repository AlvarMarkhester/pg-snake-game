import pygame as pg
from settings import *
import random
import time


class Player(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = pg.Surface((TILESIZE, TILESIZE))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.snake_length = 1
		self.gamescore = self.snake_length - 1
		self.snake_list = []
		self.x = x
		self.y = y
		self.direction = "STOP"

	def move(self):
		if self.direction == "UP":
			self.y += -1
		if self.direction == "DOWN":
			self.y += 1
		if self.direction == "RIGHT":
			self.x += 1
		if self.direction == "LEFT":
			self.x += -1
		self.checkFood() 
		self.addSnakeLength()
		self.checkCollision()
		

	def checkCollision(self):
		if self.x < 0 or self.x > GRIDWIDTH:
			self.game.new()
		if self.y < 0 or self.y > GRIDHEIGHT:
			self.game.new()
		for pos in self.snake_list[-2::-1]:
			if self.snake_list[-1] == pos:
				self.game.new()

	def goUp(self):
		if not self.direction == "DOWN":
			self.direction = "UP"

	def goDown(self):
		if not self.direction == "UP":
			self.direction = "DOWN"

	def goLeft(self):
		if not self.direction == "RIGHT":
			self.direction = "LEFT"


	def goRight(self):
		if not self.direction == "LEFT":
			self.direction = "RIGHT"

	def addSnakeLength(self):
		self.snake_list.append((self.x * TILESIZE, self.y * TILESIZE))
		if len(self.snake_list) > self.snake_length:
			del self.snake_list[0]

	def eatFood(self):
		self.game.food.x, self.game.food.y = (random.randrange(0, 25), random.randrange(0, 25))
		self.snake_length += 1
		self.gamescore += 1

	def checkFood(self):
		if self.game.food.x == self.x and self.game.food.y == self.y:
			self.eatFood()

	def drawSnakeLength(self):
		if len(self.snake_list) >= 2:
			for size in self.snake_list[-2::-1]:
				pg.draw.rect(self.game.screen, DARKGREEN,[size[0],size[1],TILESIZE,TILESIZE])

	def update(self):
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE



class Food(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites, game.foods
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = pg.Surface((TILESIZE, TILESIZE))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y

	def update(self):
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE