from pygame.mouse import (get_pos as get_mouse_pos,
						get_pressed as get_mouse_pressed)
from pygame.event import get as get_events
from pygame.surface import Surface
from pygame.rect import Rect
from pygame.font import SysFont
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP

class Widget:
	def __init__(self, **kwargs):
		self.rect = Rect(kwargs.get('x', 0),
						kwargs.get('y', 0),
						kwargs.get('width', 100),
						kwargs.get('height', 50))
		self.image = Surface((self.rect.width, self.rect.height))
		self.background_image = kwargs.get('background_image', 0)
		self.background_image_pos = kwargs.get('background_image_pos', (0, 0))
		self.background_color = kwargs.get('background_color', (0, 0, 0))
		self.background_color_cover = kwargs.get('background_color_cover', self.background_color)
		self.background_color_click = kwargs.get('background_color_click', self.background_color)
		self.text = kwargs.get('text', '')
		self.font_size = kwargs.get('font_size', 20)
		self.font_color = kwargs.get('font_color', (255, 255, 255))
		self.font_pos = kwargs.get('font_pos', None)
		self.font = SysFont('consolas', self.font_size, 1)
		self.image.fill(self.background_color)
		self.onclick = kwargs.get('onclick', lambda instance : None)

	def show(self, surface):
		if self.background_image:
			self.image.blit(self.background_image, self.background_image_pos)
		font = self.font.render(self.text, 1, self.font_color)
		pos = self.font_pos or ((self.rect.width - font.get_rect().width)//2,
			(self.rect.height - font.get_rect().height)//2)
		self.image.blit(font, pos)
		surface.blit(self.image, (self.rect.x, self.rect.y))

	def _onclick(self):
		self.onclick(self)

	def update(self, events):
		if self.rect.collidepoint(*get_mouse_pos()) and get_mouse_pressed()[0]:
			self.image.fill(self.background_color_click)
		elif self.rect.collidepoint(*get_mouse_pos()):
			self.image.fill(self.background_color_cover)
			for event in events:
				if event.type == MOUSEBUTTONUP:
					self._onclick()
		else:
			self.image.fill(self.background_color)


def test():
	import pygame as pg
	pg.init()
	
	window = pg.display.set_mode((800, 600))

	run = True
	FPS = 60
	clock = pg.time.Clock()

	def click(instance):
		instance.text = 'Hello world'

	widget = Widget(width = 800//2, height = 480//2, background_color_cover=(156, 156, 156),
					background_color = (128, 128, 128), text='text', font_size=50,
					onclick=click, background_color_click = (0, 240, 240))

	while run:
		events = pg.event.get()
		for event in events:
			if event.type == pg.QUIT:
				run = False
		keys = pg.key.get_pressed()
		if keys[pg.K_ESCAPE]:
			run = False

		window.fill((0, 0, 0))
		widget.update(events)
		widget.show(window)
		pg.display.update()
		clock.tick(FPS)
	pg.quit()

if __name__ == '__main__':
	test()