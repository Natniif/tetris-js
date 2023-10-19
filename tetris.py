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
BLACK = (0, 0, 0)

def initialiseGrid(): 
	return [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]



class Shape(): 

	pieceNum = 0

	def __init__(self, pieceShape: list[list]): 
		self.piece = pieceShape

		# x and y track position of shape on board
		# both positions track the top left position of the piece on the board
		self.x = (GRID_WIDTH - len(self.piece)) // 2
		self.y = 0

		self.isNew = True

	def canMoveRight(self, grid):
		for i in len(self.piece[0]): 
			if grid[(self.x + self.piece.length()) + 1][self.y + i] != 0:
				self.x += 1
				return True
			else: 
				return False

	def canMoveLeft(self, grid): 
		for i in len(self.piece[0]): 
			if grid[self.x - 1][self.y + i] != 0:
				self.x -= 1
				return True
		else: 
			return False

	def canMoveDown(self, grid): 
		for i in range(len(self.piece)): 
			if (self.x + i) >= GRID_WIDTH or (self.y + len(self.piece[0])) >= GRID_HEIGHT:
				self.endPiece()
				return False
			elif grid[(self.x + i)][self.y + len(self.piece[0])] != 0:
				self.endPiece()
				return False

		self.y += 1	
		self.isNew = False
		return True

	def rotatePieceLeft(self, grid)-> Union[list[list], bool]: 
		rows = len(self.piece)
		cols = len(self.piece[0])

		newpiece = [[0 for _ in range(cols)] for _ in range(rows)]

		# TODO: this is probably wrong
		for i in range(rows): 
			for j in range(cols): 
				if grid[self.x + i][self.y + j] != 0:
					return False
			# TODO: need to figure out how to test left direction as well 

		for i in range(rows): 
			for j in range(cols): 
				newpiece[j][i] = self.piece[i][j]

		return newpiece

	def rotatePieceRight(self, grid)-> Union[list[list], bool]:
		rows = len(self.piece)
		cols = len(self.piece[0])

		newpiece = [[0 for _ in range(cols)] for _ in range(rows)]

		for i in range(rows): 
			for j in range(cols): 
				newpiece[j][i] = self.piece[rows - i][cols - j]

		return newpiece

	@classmethod
	def incDeadNum(cls): 
		cls.pieceNum += 1

	def endPiece(self): 
		for i in range(len(self.piece)):
			for j in range(len(self.piece[0])): 
				if (isinstance(self.piece[i][j], str)):
					self.piece[i][j] == self.piece[i][j].lower()

		self.incDeadNum()
		# return true so that pointer can now point to new piece
		return True

	def step(self, grid): 
		if self.canMoveDown(grid): 
			self.y += 1
		else: 
			self.endPiece()


Tshape = Shape([
    [0, "R", 0],
    ["R", "R", "R"],
])

Lshape = Shape([
    ["B", 0],
    ["B", 0],
    ["B", "B"],
])

Ishape = Shape([["G"], ["G"], ["G"]])

SquareShape = Shape([
    ["P", "P"],
    ["P", "P"],
])

colors = {
	"R": RED,
	"G": GREEN, 
	"B": BLUE, 
	"P": PURPLE,
	"r": RED,
	"g": GREEN, 
	"b": BLUE, 
	"p": PURPLE,
	0 : BLACK, 
}

def randomPiece() -> Shape:
	shapes = [Tshape, Lshape, Ishape, SquareShape]
	randomIndex = math.floor(random.random() * len(shapes))

	return shapes[randomIndex]

def drawGrid(grid: list[list], screen, cell_size): 
	for i in range(GRID_WIDTH):
		for j in range(GRID_HEIGHT):
			color = colors[grid[i][j]] 
			rect = pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, 
					  CELL_SIZE, CELL_SIZE)
			pygame.draw.rect(screen, color, rect)

def updateGrid(grid: list[list], shape: Shape): 
	#set old falling piece position to black again
	if (shape.isNew == False): 
		for i in range(len(shape.piece)):
			for j in range(len(shape.piece[0])):
				grid[shape.x + i][shape.y - 1 + j] = 0 

	for i in range(len(shape.piece)):
		for j in range(len(shape.piece[0])):
			grid[shape.x + i][shape.y + j] = shape.piece[i][j]

	return grid

def userInput(grid: list[list], piece: Shape, event): 
	if event.type == pygame.KEYDOWN:	
		if event.key == pygame.K_LEFT:
			piece.canMoveLeft(grid)
		elif event.key == pygame.K_RIGHT:
			piece.canMoveRight(grid)
		elif event.key == pygame.K_DOWN:
			pass
		elif event.key == pygame.K_SPACE:
			# space bar rotates the piece
			pass

def main(): 
	# fixed FPS for now 
	FPS = 5
	grid = initialiseGrid()

	pygame.init() 
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Tetris")

	running = True
	clock = pygame.time.Clock()

	# init pointer to piece
	currentPiece = randomPiece()
	while running:
		for event in pygame.event.get():
			if event.type is not None:
				userInput(grid, currentPiece, event)
			if event.type == pygame.QUIT:
				running = False

		grid = updateGrid(grid, currentPiece)
		drawGrid(grid, screen, CELL_SIZE)

		# if cant move down init new random piece and change pointer to new random piece
		if (currentPiece.canMoveDown(grid) == False): 
			currentPiece = randomPiece()
		#else currentPiece.canMoveDown(grid):
			
	

		pygame.display.flip()

		clock.tick(FPS)
		time.sleep(0.05)

	pygame.quit()

if __name__ == "__main__":
	main()