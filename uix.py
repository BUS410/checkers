from pygame.mouse import (get_pos as get_mouse_pos,
						get_pressed as get_mouse_pressed)
from pygame.event import get as get_events
from pygame.surface import Surface
from pygame.rect import Rect
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP

class Widget:
	def __init__(self, **kwargs):
		self.rect = Rect(kwargs.get('x', 0),
						kwargs.get('y', 0),
						kwargs.get('width', 100),
						kwargs.get('height', 50))
		self.image = Surface((self.rect.width, self.rect.height))
		self.background_color = kwargs.get('background_color', (0, 0, 0))
		self.background_color_cover = kwargs.get('background_color_cover', (0, 0, 0))
		self.background_color_click = kwargs.get('background_color_click', (0, 0, 0))
		self.image.fill(self.background_color)

	def show(self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))

	def _onclick(self):
		pass

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

class Label(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

class Button(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

class CheckBox(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

def test():
	import pygame as pg
	pg.init()
	
	window = pg.display.set_mode((800, 480))

	run = True
	FPS = 60
	clock = pg.time.Clock()

	widget = Widget(x = 50, y = 50, background_color=(255, 255, 255),
					background_color_cover = (128, 128, 128))

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