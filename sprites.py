# Title:  Isometric tile game
# Author: Igor Kucharski

import pygame as pg
from settings import *


class IsoTile(pg.sprite.Sprite):
	def __init__(self, game, x, y):

		self.groups = game.all_sprites, game.isoTiles
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = pg.Surface((TILESIZE, TILESIZE), pg.SRCALPHA)
		self.image.fill(ALPHA)
		self.coords = [(0.5 * TILESIZE, 0), (0, 0.25 * TILESIZE), (0.5 * TILESIZE, 0.5 * TILESIZE), (TILESIZE, 0.25 * TILESIZE)]
		self.global_coords = [(x + 0.5 * TILESIZE, y), (x, y + 0.25 * TILESIZE), (x + 0.5 * TILESIZE, y + 0.5 * TILESIZE), (x + TILESIZE, y + 0.25 * TILESIZE)]
		self.focus = False
		# self.poly = pg.draw.polygon(self.image, WHITE, self.coords, self.focus)
		self.rect = pg.Rect(0, 0, TILESIZE, 0.5 * TILESIZE)
		self.rect.x = x
		self.rect.y = y


	def set_focus(self):
		mouse_pos = pg.mouse.get_pos()
		coeff = (self.global_coords[0][0] - self.rect.x) / (self.global_coords[1][1] - self.rect.y)
		mouse_coeff = 0

		if (mouse_pos[0] > self.rect.x 
		and mouse_pos[1] > self.rect.y
		and mouse_pos[0] < self.global_coords[3][0]
		and mouse_pos[1] < self.global_coords[2][1]):

			if (mouse_pos[0] < self.global_coords[0][0]		 
			and mouse_pos[1] < self.global_coords[1][1]):				
				mouse_coeff = (mouse_pos[0] - self.rect.x) / (self.global_coords[1][1] - mouse_pos[1])

			elif (mouse_pos[0] > self.global_coords[0][0]		 
			and mouse_pos[1] < self.global_coords[1][1]):				
				mouse_coeff = (self.global_coords[3][0] - mouse_pos[0]) / (self.global_coords[1][1] - mouse_pos[1])

			elif (mouse_pos[0] < self.global_coords[0][0]		 
			and mouse_pos[1] > self.global_coords[1][1]):				
				mouse_coeff = (mouse_pos[0] - self.rect.x) / (mouse_pos[1] - self.global_coords[1][1])

			elif (mouse_pos[0] > self.global_coords[0][0]		 
			and mouse_pos[1] > self.global_coords[1][1]):				
				mouse_coeff = (self.global_coords[3][0] - mouse_pos[0]) / (mouse_pos[1] - self.global_coords[1][1])

			elif (mouse_pos[0] == self.global_coords[0][0]
			or	mouse_pos[1] == self.global_coords[1][1]):
				mouse_coeff = coeff

		# Twierdzenie Talesa w celu sprawdzenia kolizji wskaźnika myszy z izometryczną płytką.
		if coeff <= mouse_coeff: 
			pg.draw.polygon(self.image, WHITE, self.coords)
			self.focus = True
		else:
			pg.draw.polygon(self.image, LIGHTGREY, self.coords)
			# pg.draw.polygon(self.image, BLACK, self.coords, 1)
			self.focus = False
				# print(self.rect.x, self.rect.y)
				# print(self.rect.width, self.rect.height)
				# print("Pozycja kursora: ", mouse_pos, "\nWspółczynnik: ", mouse_coeff, "\n")


	def update(self):

		# pg.draw.rect(self.game.screen, BLUE, self.rect, 2)				
		self.set_focus()
		# self.game.screen.blit(self.image, self.rect)
		

class IsoCube(pg.sprite.Sprite):

	def __init__(self, game, x, y):
		# self.groups = game.all_sprites, game.isoCubes
		pg.sprite.Sprite.__init__(self)
		self.game = game
		self.image = pg.Surface((TILESIZE, TILESIZE), pg.SRCALPHA)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y - 0.5 * TILESIZE
		self.layer = self.rect.y
		self.game.isoCubes.add(self, layer = self.layer)
		# self.game.isoCubes.add(self, layer = self.layer)
		self.draw_cube()


	def draw_cube(self):
		self.coords_up = [(0.5 * TILESIZE, 0), (0, 0.25 * TILESIZE), (0.5 * TILESIZE, 0.5 * TILESIZE), (TILESIZE, 0.25 * TILESIZE)]
		self.poly_up = pg.draw.polygon(self.image, RED, self.coords_up)

		self.coords_left = [(0, 0.25 * TILESIZE), (0, 0.75 * TILESIZE), (0.5 * TILESIZE, TILESIZE), (0.5 * TILESIZE, 0.5 * TILESIZE)]
		self.poly_left = pg.draw.polygon(self.image, GREEN, self.coords_left)

		self.coords_right = [(0.5 * TILESIZE, 0.5 * TILESIZE), (0.5 * TILESIZE, TILESIZE), (TILESIZE, 0.75 * TILESIZE), (TILESIZE, 0.25 * TILESIZE)]
		self.poly_right = pg.draw.polygon(self.image, BLUE, self.coords_right)


	def update(self):
		# pg.draw.rect(self.image, BLUE, self.rect, 2)
		# self.game.screen.blit(self.image, self.rect)
		pass
