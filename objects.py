from pygame.rect import Rect
from pygame.surface import Surface
from pygame.sprite import Group, Sprite
from pygame.draw import circle


CELLS_SIZE = 64
FIRST_COLOR_CELL = (233, 212, 176)
SECOND_COLOR_CELL = (176, 131, 96)
VALID_COLOR = (58, 233, 100)

FIRST_COLOR_CHECKER = (255, 255, 255)
SECOND_COLOR_CHECKER = (0, 0, 0)


class Cell(Sprite):

	def __init__(self, color, pos):
		Sprite.__init__(self)
		self.rect = Rect(*pos, CELLS_SIZE, CELLS_SIZE)
		self.image = Surface((self.rect.width, self.rect.height))
		self.image.fill(color)
		self.state = 'normal'

	def draw(self, surface):
		if self.state == 'normal':
			self.image.fill(color)
		elif self.state == 'selected':
			self.image.fill(VALID_COLOR)
		surface.blit(self.image, (self.rect.x, self.rect.y))

class Checker:

	def __init__(self, color, pos):
		self.pos = pos
		self.color = color
		self.state = 'normal'

	def draw(self, surface):
		pos = (self.pos[0]*CELLS_SIZE+CELLS_SIZE//2, self.pos[1]*CELLS_SIZE+CELLS_SIZE//2)
		circle(surface, (58, 228, 233) if self.state == 'selected' else self.color, pos, CELLS_SIZE//2)

	def move_to(self, pos):
		self.pos = (pos[0]*CELLS_SIZE+CELLS_SIZE//2, pos[1]*CELLS_SIZE+CELLS_SIZE//2)

class Board(Group):

	def __init__(self):
		Group.__init__(self)

		color = FIRST_COLOR_CELL

		for y in range(0, 512, CELLS_SIZE):
			if color == FIRST_COLOR_CELL:
				color = SECOND_COLOR_CELL
			else:
				color = FIRST_COLOR_CELL
			for x in range(0, 512, CELLS_SIZE):

				self.add(Cell(color, (x, y)))

				if color == FIRST_COLOR_CELL:
					color = SECOND_COLOR_CELL
				else:
					color = FIRST_COLOR_CELL
				




class GroupChecker(list):
	def reset_pos_checkers(self):

		self.clear()


		for y in range(0, 3):
			for x in range(0+y%2, 8, 2):
				self.append(Checker(SECOND_COLOR_CHECKER, (x, y)))

		for y in range(5, 8):
			for x in range(0+y%2, 8, 2):
				self.append(Checker(FIRST_COLOR_CHECKER, (x, y)))
