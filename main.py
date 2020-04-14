import pygame

from objects import Board, GroupChecker
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
		self.checkers = GroupChecker()
		self.checkers.reset_pos_checkers()
		self.step = (255, 255, 255)
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
		
		for cell in self.board:
			cell.draw(self.window)

		for widget in self.widgets:
			widget.show(self.window)

		for checker in self.checkers:
			checker.draw(self.window)


		self.scores[0].text = str(self.score_black)
		self.scores[1].text = str(self.score_white)
		for score in self.scores:
			score.show(self.window)

		pygame.display.update()

	def exit(self, instance):
		self.stop = True

	def reset(self, instance):
		self.checkers.reset_pos_checkers()
		self.step = (255, 255, 255)
		for cell in self.board:
			cell.state = 'normal'

	def run(self):
		self.stop = False

		while not self.stop:

			events = pygame.event.get()
			for event in events:
				if event.type == pygame.QUIT:
					self.stop = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					temp_pos = (pos[0]//64, pos[1]//64)
					if pos[0] < 512:
						poses = []
						selected = None
						for checker in self.checkers:
							poses.append(checker.pos)
							if checker.pos == temp_pos and self.step == checker.color:
								checker.state = 'selected'
								selected = checker
							else:
								checker.state = 'normal'

						if selected:
							valid_steps = []
							temp_valid_steps = [
								(selected.pos[0]+1, selected.pos[1]+1),
								(selected.pos[0]-1, selected.pos[1]-1),
								(selected.pos[0]+1, selected.pos[1]-1),
								(selected.pos[0]-1, selected.pos[1]+1),
							]

							for vp in temp_valid_steps:
								if not (8 in vp or -1 in vp or vp in poses):
									valid_steps.append(vp)
								if vp in poses:
									for checker in self.checkers:
										if checker.pos == vp and checker.color!=selected.color:
											pos = ((
													selected.pos[0]-(selected.pos[0]-vp[0])*2,
													selected.pos[1]-(selected.pos[1]-vp[1])*2,
												))
											if pos not in poses:
												valid_steps.append(pos)



							for cell in self.board:
								if (cell.rect.x//64, cell.rect.y//64) in valid_steps:
									cell.state = 'selected'
								else:
									cell.state = 'normal'
						else: # if click on cell

							for cell in self.board:
								cell_pos = (cell.rect.x//64, cell.rect.y//64)
								if cell_pos == temp_pos:
									if cell.state == 'selected':
										self.selected.move_to(cell_pos)
										
										if self.step == (255, 255, 255):
											self.step = (0, 0, 0)
										elif self. step == (0, 0, 0):
											self.step = (255, 255, 255)

							for cell in self.board:
								cell.state = 'normal'

						poses.clear()
						self.selected = selected
						selected = None


			for widget in self.widgets:
				widget.update(events)
			for score in self.scores:
				score.update(events)

			self.draw()
			self.clock.tick(FPS)


if __name__ == '__main__':
	Program().run()