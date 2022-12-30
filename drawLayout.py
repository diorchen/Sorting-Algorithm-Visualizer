import pygame
import math
pygame.init()

class DrawInformation:
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GREEN = 0, 255, 0
	RED = 255, 0, 0
	BACKGROUND_COLOR = WHITE

	GRADIENTS = [
		(128, 128, 128),
		(160, 160, 160),
		(192, 192, 192)
	]

	FONT = pygame.font.SysFont('timesnewroman', 25) #font for the labels
	LARGE_FONT = pygame.font.SysFont('timesnewroman', 35)

	SIDE_PAD = 100
	TOP_PAD = 150

	def __init__(self, width, height, lst): #initialization
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode((width, height)) #creates attribute for the window that can be easily accessed
		pygame.display.set_caption("Sorting Algorithm Visualization")
		self.set_list(lst)

	def set_list(self, lst): #sets attributes needed for the list
		self.lst = lst
		self.min_val = min(lst)
		self.max_val = max(lst)

		self.block_width = round((self.width - self.SIDE_PAD) / len(lst)) #width of bars adjust depending on the number of values in list
		self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val)) #creates height of bars by determining starting point of upper left corner
		self.start_x = self.SIDE_PAD // 2 # x-coordinate starting point for the blocks 


def draw(draw_info, algo_name, ascending): #sets up the display
	draw_info.window.fill(draw_info.BACKGROUND_COLOR) #background fill

	title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.BLACK)
	draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2 , 5))

	controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLACK) #renders the control text
	draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2 , 45)) #draws the text and aligns in the center

	sorting1 = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort | S - Selection Sort", 1, draw_info.BLACK) #renders sorting algorithm text
	draw_info.window.blit(sorting1, (draw_info.width/2 - sorting1.get_width()/2 , 75)) #draws text and aligns in the center

	sorting2 = draw_info.FONT.render("M - Merge Sort | Q - Quick Sort | H - Heap Sort", 1, draw_info.BLACK) #renders sorting algorithm text
	draw_info.window.blit(sorting2, (draw_info.width/2 - sorting2.get_width()/2 , 105))

	draw_list(draw_info)
	pygame.display.update() #redraws the frame everytime it updates


def draw_list(draw_info, color_positions={}, clear_bg=False): #draws the blocks in the list, color_positions = dictionary for color of active blocks
	lst = draw_info.lst

	if clear_bg: #clears the portion of the window that the blocks are placed in
		clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD) #establishes borders of the window
		pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect) #renders the clear

	for i, val in enumerate(lst):
		x = draw_info.start_x + i * draw_info.block_width #calculate x and y-coordinate for the top left corner of the rectangles
		y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

		color = draw_info.GRADIENTS[i % 3] #every 3, the gradient resets

		if i in color_positions:
			color = color_positions[i]  #manually overwrites the color of the block to the assigned color

		pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

	if clear_bg:
		pygame.display.update()