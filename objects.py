from pygame.rect import Rect
from pygame.surface import Surface
from pygame.sprite import Group, Sprite
from pygame.draw import circle


CELLS_SIZE = 64
FIRST_COLOR = (176, 131, 96)
SECOND_COLOR = (233, 212, 176)
SELECTED_COLOR = (213, 238, 140)


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
			self.image.fill(SELECTED_COLOR)
		surface.blit(self.image, (self.rect.x, self.rect.y))

class Checker(Sprite):

	def __init__(self, color, pos):
		Sprite.__init__(self)
		self.pos = pos
		self.color = color

	def draw(self, surface):
		pos = (self.pos.x*CELLS_SIZE+CELLS_SIZE//2, self.pos.y*CELLS_SIZE+CELLS_SIZE//2)
		circle(surface, self.color, pos, CELLS_SIZE//2)

	def move_to(self, pos):
		self.pos = (pos.x*CELLS_SIZE+CELLS_SIZE//2, pos.y*CELLS_SIZE+CELLS_SIZE//2)

class Board(Group):

	def __init__(self):
		Group.__init__(self)

		color = FIRST_COLOR

		for y in range(0, 512, CELLS_SIZE):
			if color == FIRST_COLOR:
				color = SECOND_COLOR
			else:
				color = FIRST_COLOR
			for x in range(0, 512, CELLS_SIZE):

				self.add(Cell(color, (x, y)))

				if color == FIRST_COLOR:
					color = SECOND_COLOR
				else:
					color = FIRST_COLOR
				

class GroupChecker(Group):
	pass
