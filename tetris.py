#din/env python3

import pygame 
import random 
import math
import time 
from typing import Union

WIDTH, HEIGHT = 400, 600

GRID_WIDTH = 10
GRID_HEIGHT = 15
CELL_SIZE = WIDTH // GRID_WIDTH

BLUE = (51, 153, 255)
GREEN = (0, 204, 0)
RED = (255, 0, 0)
PURPLE = (153, 0, 153)

def initialiseGrid(): 
	return [[0 for _ in range(15)] for _ in range(10)]


class Shape(): 

	pieceNum = 0

	def __init__(self, pieceShape): 
		self.piece = pieceShape

		# x and y track position of shape on board
		self.x = (GRID_WIDTH + self.piece) // 2
		self.y = 0

	def canMoveRight(self, grid):
		for i in self.piece[0].length(): 
			if grid[(self.x + self.piece.length()) + 1][self.y + i] != 0:
				self.x += 1
			else: 
				return False

	def canMoveLeft(self, grid): 
		for i in self.piece[0].length(): 
			if grid[self.x - 1][self.y + i] != 0:
				self.x -= 1
		else: 
			return False

	def canMoveDown(self, grid): 
		for i in self.piece.length(): 
			if grid[(self.x + i - 1)][self.y + self.piece[0].length()] != 0:
				return False

		self.y += 1	
		return True

	def rotatePieceLeft(self, grid)-> Union[list[list], bool]: 
		rows = self.piece.length()
		cols = self.piece[0].length()

		newpiece = [[0 for _ in range(cols)] for _ in range(rows)]

		# TODO: this is probably wrong
		for i in rows: 
			if grid[self.x + i][self.y + j] != 0:
				return False
			# TODO: need to figure out how to test left direction as well 

		for i in rows: 
			for j in cols: 
				newpiece[j][i] = self.piece[i][j]

		return newpiece

	def rotatePieceRight(self, grid)-> Union[list[list], bool]:
		rows = self.piece.length()
		cols = self.piece[0].length()

		newpiece = [[0 for _ in range(cols)] for _ in range(rows)]

		for i in rows: 
			for j in cols: 
				newpiece[j][i] = self.piece[rows - i][cols - j]

		return newpiece

	@classmethod
	def incDeadNum(cls): 
		cls.pieceNum += 1

	def endPiece(self): 
		for i in self.piece.length():
			for j in self.piece[0].length(): 
				self.piece[i][j] == self.piece[i][j].lower()

		self.incDeadNum()

	def step(self, grid): 
		if self.canMoveDown(grid): 
			self.y += 1
		else: 
			self.endPiece()


Tshape = Shape([
    [0, 'R', 0],
    ['R', 'R', 'R'],
])

Lshape = Shape([
    ['B', 0],
    ['B', 0],
    ['B', 'B'],
])

Ishape = Shape([['G'], ['G'], ['G']])

SquareShape = Shape([
    ['Y', 'Y'],
    ['Y', 'Y'],
])

colors = {
	'R': "RED",
	'G': "GREEN", 
	'B': "BLUE", 
	'P': "PURPLE",
	'r': "RED",
	'g': "GREEN", 
	'b': "BLUE", 
	'p': "PURPLE"
}

def randomPiece() -> Shape:
	shapes = [Tshape, Lshape, Ishape, SquareShape]
	randomIndex = math.floor(random.random() * len(shapes))

	return shapes[randomIndex]

def drawGrid(grid: list[list], screen, cell_size): 
	for i in range(GRID_HEIGHT):
		for j in range(GRID_WIDTH):
			color = colors[grid[i][j]] 
			rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, 
					  CELL_SIZE, CELL_SIZE)
			pygame.draw.rect(screen, color, rect)

def updateGrid(grid: list[list], shape: Shape): 
	pass


def userInput(piece: Shape, event): 
	if event.type == pygame.KEYDOWN:	
		if event.key == pygame.K_LEFT:
			piece.canMoveLeft
		elif event.key == pygame.K_RIGHT:
			piece.canMoveRight
		elif event.key == pygame.K_DOWN:
			pass
		elif event.key == pygame.K_SPACE:
			# space bar rotates the piece
			pass

def step(shape: Shape, grid): 
	pass

def main(): 
	# fixed FPS for now 
	FPS = 10
	grid = initialiseGrid()

	pygame.init() 
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Tetris")

	running = True
	clock = pygame.time.Clock()

	while running:
		for event in pygame.event.get():
			userInput(event)
			if event.type == pygame.QUIT:
				running = False

		drawGrid(grid, CELL_SIZE, grid, screen)

		step()

		pygame.display.flip()

		clock.tick(FPS)
		time.sleep(0.05)

	pygame.quit()

if __name__ == "__main__":
	main()