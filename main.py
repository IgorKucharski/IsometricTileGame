# Title:  Isometric tile game
# Author: Igor Kucharski


import pygame as pg
import random
import sys
from settings import *
from sprites import *


class Game:
	"""Main class."""
	
	def __init__(self):
		"""Initialization."""
		
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		self.screen.fill(LIGHTGREY)
		# self.draw_isometric_grid()
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		self.running = True
		

	def new(self):
		"""Start a new game."""
		
		self.all_sprites = pg.sprite.LayeredUpdates()
		self.isoTiles = pg.sprite.LayeredUpdates()
		self.isoCubes = pg.sprite.LayeredUpdates()

	
		for y in range(0, 2*HEIGHT, TILESIZE):
			for x in range(0, WIDTH, TILESIZE):
				IsoTile(self, x, 0.5 * y)
				IsoTile(self, x + 0.5 * TILESIZE, 0.5 * y + 0.25 * TILESIZE)

		# for y in range(1, 10, 1):
		# 	for x in range(10, 0, -1):

		# 			IsoCube(self, x * TILESIZE, 0.5 * y * TILESIZE)
		# 			IsoCube(self, x * TILESIZE + 0.5 * TILESIZE, 0.5 * y * TILESIZE + 0.25 * TILESIZE)
					

		self.run()
		

	def run(self):
		"""Game loop."""
		
		self.playing = True
		while self.playing:
			self.dt = self.clock.tick(FPS) / 1000
			self.events()
			self.update()
			self.draw()


	def quit(self):
		"""Quit game."""

		pg.quit()
		sys.exit()

		
	def update(self):
		"""Game loop - update."""
		
		self.all_sprites.update()


	def events(self):
		"""Game loop - events."""
		
		for event in pg.event.get():
			if event.type == pg.QUIT:
				if self.playing:
					self.playing = False
					self.quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.quit()
				if event.key == pg.K_l:
					print(self.isoCubes.get_top_layer())
					print(self.isoCubes.layers())
			if event.type == pg.MOUSEBUTTONDOWN:
				mouse_pos = pg.mouse.get_pos()
				focused_tiles = [tile for tile in self.isoTiles if tile.focus]
				focused_cubes = [cube for cube in self.isoCubes if (cube.rect.collidepoint(mouse_pos) 
																and focused_tiles[0].rect.x == cube.rect.x 
																and focused_tiles[0].rect.y - 0.5 * TILESIZE == cube.rect.y)]
				if pg.mouse.get_pressed()[0] and not focused_cubes:									
					IsoCube(self, focused_tiles[0].rect.x, focused_tiles[0].rect.y)
				if pg.mouse.get_pressed()[2] and focused_cubes:	
					focused_cubes[0].kill()


	def draw_ortogonal_grid(self):
		"""Drawing grid in background."""

		for x in range(0, WIDTH, TILESIZE):
			pg.draw.line(self.screen, DARKGREY, (x, 0), (x, HEIGHT))
		for y in range(0, HEIGHT, TILESIZE):
			pg.draw.line(self.screen, DARKGREY, (0, y), (WIDTH, y))


	def draw_isometric_grid(self):
		"""Drawing grid in background."""

		for x in range(-2*HEIGHT, 2*HEIGHT, TILESIZE):
			pg.draw.line(self.screen, DARKGREY, (2 * HEIGHT - x - 0.5 * TILESIZE, 0), ( -x - 0.5 * TILESIZE, HEIGHT))
			pg.draw.line(self.screen, DARKGREY, (x - 0.5 * TILESIZE, 0), (2 * HEIGHT - 0.5 * TILESIZE + x, HEIGHT))


	def draw(self):
		"""Game loop - draw."""
		
		for sprite in self.isoTiles:
			self.screen.blit(sprite.image, sprite.rect)
		for sprite in self.isoCubes:
			self.screen.blit(sprite.image, sprite.rect)
		self.draw_isometric_grid()

		pg.display.flip()
		

	def show_start_screen(self):
		"""Game start screen."""		
		pass
		
		
	def show_go_screen(self):
		""" Game over screen."""		
		pass
		

game = Game()
game.show_start_screen()

while game.running:
	game.new()
	game.show_go_screen()
	
pg.quit()
