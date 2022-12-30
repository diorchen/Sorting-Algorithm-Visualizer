import pygame
import random
import drawLayout 
import algorithms
pygame.init()

def generate_starting_list(n, min_val, max_val): #generates random list given input requirements
	lst = []

	for _ in range(n):
		val = random.randint(min_val, max_val)
		lst.append(val)

	return lst

def main(): #main driver code that allows you to see window
	run = True
	clock = pygame.time.Clock() #regulates how quickly the loop runs

	n = 50 #arbitrary that can be changed later
	min_val = 0
	max_val = 100

	lst = generate_starting_list(n, min_val, max_val)
	draw_info = drawLayout.DrawInformation(800, 600, lst) #creates the window we are working in
	sorting = False
	ascending = True

	sorting_algorithm = algorithms.bubble_sort
	sorting_algo_name = "Bubble Sort"
	sorting_algorithm_generator = None

	while run: #loop that handles all occurring events during run
		clock.tick(3) # 20 FPS, maximum number of times this loop can run per second

		if sorting:
			try:
				next(sorting_algorithm_generator) #if sorting, try to call next method
			except StopIteration: #if doesn't work (likely generator done), then stop sort
				sorting = False
		else:
			drawLayout.draw(draw_info, sorting_algo_name, ascending)

		for event in pygame.event.get(): #returns a list of all events that have happened since the last loop, check the event 
			if event.type == pygame.QUIT: # clicking X in upper right corner to quit the game
				run = False

			if event.type != pygame.KEYDOWN:
				continue

			if event.key == pygame.K_r: #resets the run
				lst = generate_starting_list(n, min_val, max_val)
				draw_info.set_list(lst)
				sorting = False
			elif event.key == pygame.K_SPACE and sorting == False: #starts sorting
				sorting = True
				sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
			elif event.key == pygame.K_a and not sorting: #sorts in ascending order
				ascending = True
			elif event.key == pygame.K_d and not sorting: #sorts in descending order
				ascending = False
			elif event.key == pygame.K_i and not sorting: #insertion sort
				sorting_algorithm = algorithms.insertion_sort
				sorting_algo_name = "Insertion Sort"
			elif event.key == pygame.K_b and not sorting: #bubble sort
				sorting_algorithm = algorithms.bubble_sort
				sorting_algo_name = "Bubble Sort"
			elif event.key == pygame.K_s and not sorting: #selection sort
				sorting_algorithm = algorithms.selection_sort
				sorting_algo_name = "Selection Sort"
			elif event.key == pygame.K_m and not sorting: #merge sort
				sorting_algorithm = algorithms.merge_sort
				sorting_algo_name = "Merge Sort"
			elif event.key == pygame.K_q and not sorting: #quick sort
				sorting_algorithm = algorithms.quick_sort
				sorting_algo_name = "Quick Sort"
			elif event.key == pygame.K_h and not sorting: #heap sort
				sorting_algorithm = algorithms.heap_sort
				sorting_algo_name = "Heap Sort"


	pygame.quit()


if __name__ == "__main__": # makes sure we are running the module directly before we run the main function
	main()