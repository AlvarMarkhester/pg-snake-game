import pygame as pg
from settings import *
import random


class Player(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = pg.Surface((TILESIZE, TILESIZE))
		self.image.fill(YELLOW)
		self.rect = self.image.get_rect()
		self.snake_length = 1
		self.snake_list = []
		self.x = x
		self.y = y

	def move(self, dx=0, dy=0):
		if self.game.food.x == self.x + dx and self.game.food.y == self.y + dy:
			self.eatFood()
		self.x += dx
		self.y += dy
		self.snake_list.append((self.x, self.y))
		if len(self.snake_list) > self.snake_length:
			del self.snake_list[0]

	def eatFood(self):
		self.game.food.x, self.game.food.y = (random.randrange(0, 25), random.randrange(0, 25))
		self.snake_length += 1
		
		
	#def drawSnakeBody(self):
		#for index in range(len(self.snake_list)-1,0,-1):
			#pg.draw.rect(self.game.screen, YELLOW, pg.Rect(self.game.screen, YELLOW, self.snake_list[index-1], self.snake_list[index-1],TILESIZE, TILESIZE))

	def update(self):
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE



class Food(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites, game.foods
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = pg.Surface((TILESIZE, TILESIZE))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y

	def update(self):
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE