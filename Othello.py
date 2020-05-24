# Imports
import sys, pygame
import os
import pygame.gfxdraw

# Colors 
WHITE = (255, 255, 255)
GREEN = (0,110,0)
GREY = (150,150,150)
BLACK = (0,0,0)

# Size of window
size = WIDTH, HEIGHT = 800, 600	

# Window
screen = pygame.display.set_mode(size)

# Global Variables
## 
mousePressReady = False
## Variable to store whos turn
blackTurn = False
## Variable to determine if game has ended
gameOver = False
## 8x8 board containing 64 cells
board = [[None for x in range(0,8)] for y in range(0,8)]


class OthelloCell():
	"""docstring for OthelloCell"""
	def __init__(self, i, j):
		super(OthelloCell, self).__init__()
		self.played = False
		self.x = i
		self.y = j
		self.black = True
	
	def drawCell(self):
		'''Draws the cell on the board, in its current state.'''
		# Green box
		pygame.gfxdraw.box(screen, (35+(self.x*61), 55+(self.y*61), 61, 61), GREEN)
		# Black rectangle
		pygame.draw.rect(screen, BLACK, (35+(self.x*61), 55+(self.y*61),61,61), 1)

	def playIt(self):
		'''Sets the value of played to true, to indicate that a piece has been placed on this cell.'''
		self.played = True

	def setBlack(self, b):
		'''Sets the piece to black (black true) or white (black false).'''
		self.black = b

	def getBlackStatus(self):
		'''Return the status of black; true for a black piece, false for a white piece.'''
		return self.black

	def hasBeenPlayed(self):
		'''Return the status of played, indicating whether or not there is a game piece on this cell.'''
		return self.played

def startBoard():
	'''Initial population of the board'''
	global blackTurn
	global mousePressReady
	blackTurn = True
	mousePressReady = True
	pygame.display.set_caption("Othello")
	for i in range(0,8):
		for j in range(0,8):
			board[i][j]=OthelloCell(i,j)
	board[3][3].playIt();
	board[3][3].setBlack(True);
	board[4][4].playIt();
	board[4][4].setBlack(True);
	board[4][3].playIt();
	board[4][3].setBlack(False);
	board[3][4].playIt();
	board[3][4].setBlack(False);

def drawBoard():
	'''Draws the board, in its current state, to the GUI.'''
	# Color the entire window grey
	pygame.gfxdraw.box(screen, (0,0,800,600),GREY)
	# Draw the board
	pygame.gfxdraw.box(screen, (30, 50, 500, 500), BLACK)
	# Add cells to the board
	for i in range(0,8):
		for j in range(0,8):
			# Call the method drawCell to add cells onto the board in GUI
			board[i][j].drawCell()

def drawScoresAndMessages(whiteCount, blackCount):
	'''A helper method for countScoreAnddrawScoreBoard. Draws the score 
	board and updates the scores after each play
	@param  whiteCount      The current count of the white pieces on the board.
	@param  blackCount      The current count of the black pieces on the board.'''
	# Initialize font
	pygame.font.init()
	# setting font and size
	myfont = pygame.font.SysFont('freesansbold.ttf', 80)
	# Setting the context of the text
	mytext = myfont.render('Score',True,BLACK)
	# Retreving the boundry for text
	textRect = mytext.get_rect()
	# Setting new location for text
	textRect.topleft = (590, 55)
	# Displaying text
	screen.blit(mytext, textRect)

	# Now repeat for white score and black score
	myfont = pygame.font.SysFont('freesansbold.ttf', 40)
	mytext = myfont.render(str(whiteCount),False,BLACK)
	textRect = mytext.get_rect()
	textRect.topleft = (590, 120)
	screen.blit(mytext, textRect)

	mytext = myfont.render(str(blackCount),False,BLACK)
	textRect = mytext.get_rect()
	textRect.topleft = (700, 120)
	screen.blit(mytext, textRect)

def countScore_DrawScoreBoard():
	'''Counts the white pieces on the board, and the black pieces on the board.
	Displays these numbers toward the top of the board, for the current state
	of the board.  Also prints whether it is "BLACK'S TURN" or "WHITE'S TURN"
	or "GAME OVER". '''
	whiteCount = 0
	blackCount = 0
	for x in range(0,8):
		for y in range(0,8):
			pass

	drawScoresAndMessages(whiteCount,blackCount)

def checkTurnAndGameOver():
	'''Checks to see if black can play.  Checks to see if white can play.
	If neither can play, the game is over.  If black can't go, then set
	blackTurn to false.  If white can't go, set blackTurn to true.
	@return - Returns true if the game is over, false otherwise.'''
	pass

def flipAllInThatDirection():
	'''A helper method for playAndFlipTiles.  Flips pieces in a given direction.  The
	 *  directions are as follows:
	 *  (1,1) is up and right
	 *  (1,0) is right
	 *  (1,-1) is down and right
	 *  (0,-1) is down
	 *  (-1,-1) is down and left
	 *  (-1,0) is left
	 *  (-1,1) is left and up
	 *  (0,1) is up
	 *  @param  xt      The horizontal coordinate value in the board.
	 *  @param  yt      The vertical coordinate value in the board.
	 *  @param  i       -1 is left, 0 is neutral, 1 is right,
	 *  @param  j       -1 is down, - is neutral, 1 is up.'''
	pass

def playAndFlipTiles():
	'''Places a game piece on the current cell for the current player.  Also flips the
	 *  appropriate neighboring game pieces, checking the 8 possible directions from the
	 *  current cell.'''
	pass

def directionValid():
	'''Checks to see if a valid move can be made at the indicated OthelloCell, in a 
	 *  particular direction (there are 8 possible directions). These are indicated by:
	 *  (1,1) is up and right
	 *  (1,0) is right
	 *  (1,-1) is down and right
	 *  (0,-1) is down
	 *  (-1,-1) is down and left
	 *  (-1,0) is left
	 *  (-1,1) is left and up
	 *  (0,1) is up
	 *  @param  xt      The horizontal coordinate value in the board.
	 *  @param  yt      The vertical coordinate value in the board.
	 *  @param  i       -1 is left, 0 is neutral, 1 is right,
	 *  @param  j       -1 is down, - is neutral, 1 is up.
	 *  @param  bTurn   Indicates the current player, true for black, false for white.
	 *  @return         Returns true if this direction has pieces to be flipped, false otherwise.'''
	pass

def isValidMove(xt,yt,bTurn):
	'''Checks to see if a valid move can be made at the indicated OthelloCell,
	 *  for the given player.
	 *  @param  xt      The horizontal coordinate value in the board.
	 *  @param  yt      The vertical coordinate value in the board.
	 *  @param  bTurn   Indicates the current player, true for black, false for white
	 *  @return         Returns true if a valid move can be made for this player at
	 *                  this position, false otherwise.'''
	pass

def makeChoice():
	'''Waits for the user to make a choice. The user can make a move
	placing a black piece or the white piece (depending on whose turn
	it is), or click on the "RESET" button to reset the game.'''
	
	global blackTurn 
	global mousePressReady

	moveChosen = False
	while(not(moveChosen)):
		if(mousePressReady and bool(pygame.mouse.get_pressed()[0])):
			mousePressReady = False
			x = pygame.mouse.get_pos()[0]
			y = pygame.mouse.get_pos()[1]
			# Determe if the click was outside the board
			if (x<35 or x>523 or y<55 or y>543):
				# Click wasnt valid so return
				return
			else:
				print(x,y)
			
			tempx = x
			tempy = y
			# Check if users move is valid
			if (isValidMove(tempx, tempy, blackTurn)):
				playAndFlipTiles()
				# Change the turn
				blackTurn = not(blackTurn)

		if(not(pygame.mouse.get_pressed()[0]) and not(mousePressReady)):
			mousePressReady = True
			return
		pygame.time.wait(30)
		moveChosen = True

def main():
	'''Runs an endless loop to play the game.  Even if the game is over, the
		loop is still ready for the user to press "RESET" to play again.'''
	run = True
	while(run):
		# Quit the game if the quit icon is pressed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		# Draws the board, in its current state, to the GUI.
		drawBoard()
		# Draw the scoreboard and update the score
		countScore_DrawScoreBoard()
		# Update the full display Surface to the screen
		pygame.display.flip()
		# pause the program for an amount of time
		pygame.time.wait(30)
		# Wait for user to make a move
		makeChoice()
		# Check whos turn it is and determine if the game is over
		gameOver = checkTurnAndGameOver()

if __name__ == '__main__':
	# Initialize pygame display
	pygame.display.init()
	# Setup the graphics for the board
	startBoard()
	# Run the game
	main()