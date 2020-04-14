import pygame

from objects import Board
from uix import Widget

RESOLUTION = (512+128, 512)
FPS = 60

class Program:
	def __init__(self):
		pygame.init()
		pygame.font.init()

		self.window = pygame.display.set_mode(RESOLUTION)
		self.clock = pygame.time.Clock()
		self.board = Board()
		self.widgets = [
			Widget(x=512, y=0, width=128, height=96, text='Reset', font_size=30,
				background_color=(255, 175, 88), background_color_cover=(255, 195, 131),
				background_color_click=(255, 132, 0), font_color=(168, 88, 2), onclick=self.reset),
			Widget(x=512, y=512-96, width=128, height=96, text='Exit', font_size=30,
				background_color=(255, 175, 88), background_color_cover=(255, 195, 131),
				background_color_click=(255, 132, 0), font_color=(168, 88, 2), onclick=self.exit),
		]

		self.scores = [
			Widget(x=512, width=128, height=160, y=96, text='0', font_size=50,
				background_color=(238, 191, 140), font_color=(168, 88, 2)),
			Widget(x=512, width=128, height=160, y=256, text='0', font_size=50,
				background_color=(238, 191, 140), font_color=(168, 88, 2)),
		]

		self.score_black = 0
		self.score_white = 0

	def draw(self):
		self.window.fill((0, 0, 0))
		self.board.draw(self.window)

		for widget in self.widgets:
			widget.show(self.window)


		self.scores[0].text = str(self.score_black)
		self.scores[1].text = str(self.score_white)
		for score in self.scores:
			score.show(self.window)

		pygame.display.update()

	def exit(self, instance):
		self.stop = True

	def reset(self, instance):
		pass

	def run(self):
		self.stop = False

		while not self.stop:

			events = pygame.event.get()
			for event in events:
				if event.type == pygame.QUIT:
					self.stop = True

			for widget in self.widgets:
				widget.update(events)
			for score in self.scores:
				score.update(events)

			self.draw()
			self.clock.tick(FPS)


if __name__ == '__main__':
	Program().run()