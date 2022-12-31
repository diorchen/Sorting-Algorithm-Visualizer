import drawLayout
from random import randint

def insertion_sort(draw_info, ascending=True):
	lst = draw_info.lst

	for i in range(1, len(lst)):
		current = lst[i]

		while True:
			ascending_sort = i > 0 and lst[i - 1] > current and ascending
			descending_sort = i > 0 and lst[i - 1] < current and not ascending

			if not ascending_sort and not descending_sort:
				break

			lst[i] = lst[i - 1]
			i = i - 1
			lst[i] = current
			drawLayout.draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
			yield True #gives control back to main loop so we are able to pause, reset, etc.

	return lst

def bubble_sort(draw_info, ascending=True): #implements bubble sorting algorithm, default = ascending
	lst = draw_info.lst

	for i in range(len(lst) - 1):
		for j in range(len(lst) - 1 - i):
			num1 = lst[j]
			num2 = lst[j + 1]

			if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
				lst[j], lst[j + 1] = lst[j + 1], lst[j]
				drawLayout.draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True) #draws the list in the window and assigns the proper colors
				yield True #generator creates generator object 

	return lst

def selection_sort(draw_info, ascending = True):
    lst = draw_info.lst

    for i in range(len(lst)):
        min_i = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_i] and ascending == True:
                min_i = j
            elif lst[j] > lst[min_i] and ascending == False:
                min_i = j

        if min_i != 1:
            lst[i], lst[min_i] = lst[min_i], lst[i]
            drawLayout.draw_list(draw_info, {i: draw_info.GREEN, min_i: draw_info.RED}, True)
            yield True    
    return lst

def merge_sort(draw_info, ascending=True): #calls merge_sort_helper function to yield to display in the window
    lst = draw_info.lst
    yield from merge_sort_helper(draw_info, ascending, 0, len(lst))

def merge_sort_helper(draw_info, ascending, left, right): #merge function
    lst = draw_info.lst
    if left < right:
        mid = int((left+right)/2)
        yield from merge_sort_helper(draw_info, ascending, left, mid)
        yield from merge_sort_helper(draw_info, ascending, mid+1, right)
        for arr, newLeft, newRight in merge(lst, left, mid, right, ascending):
            draw_info.lst = lst
            drawLayout.draw_list(draw_info, {newLeft: draw_info.GREEN, newRight: draw_info.RED}, True) 
            yield arr, newLeft, newRight


def merge(lst, left, mid, right, ascending): #merge function
    L = lst[left:mid+1]
    R = lst[mid+1:right+1]
    i = 0
    j = 0
    k = left
    multiplier = 1 
    if not ascending:
        multiplier = -1
    while i < len(L) and j < len(R):
        
        if multiplier * L[i] < multiplier * R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1
        yield lst, left+i, mid+j
    
    while i < len(L):
        lst[k] = L[i]
        i += 1
        k += 1
        yield lst, left+i, mid+j

    while j < len(R):
        lst[k] = R[j]
        j += 1
        k += 1
        yield lst, left+i, mid+j



def quick_sort(draw_info, ascending = True): #calls quick_sort_helper function to yield display in window
    lst = draw_info.lst
    yield from quick_sort_helper(draw_info, 0, len(lst)-1, ascending)


def quick_sort_helper(draw_info, left, right, ascending): #quick sort function implementation
    lst = draw_info.lst
    multiplier = 1
    if not ascending:
        multiplier = -1

    if left >= right:
        return
    index = left
    random_index = randint(left, right)
    lst[right], lst[random_index] = lst[random_index], lst[right]
    
    for j in range(left, right):
        drawLayout.draw_list(draw_info, {j: draw_info.GREEN, index: draw_info.RED}, True) 
        yield lst, j, index
        if multiplier* lst[j] < multiplier * lst[right]:
            lst[j], lst[index] = lst[index], lst[j]
            index += 1
    lst[index], lst[right] = lst[right], lst[index]
    yield from quick_sort_helper(draw_info, index + 1, right, ascending)
    yield from quick_sort_helper(draw_info, left, index - 1, ascending)


def heap_sort(draw_info, ascending = True): 
    lst = draw_info.lst
    
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i, ascending)
        drawLayout.draw_list(draw_info, {}, True)
        yield True
    
    for i in range(n - 1, 0, -1):
        (lst[i], lst[0]) = (lst[0], lst[i])
        heapify(lst, i, 0, ascending)
        drawLayout.draw_list(draw_info, {i: draw_info.GREEN, 0: draw_info.RED}, True)
        yield True  

def heapify(arr, N, i, ascending):
    multiplier = 1
    if not ascending:
        multiplier = -1
    
    largest = i  # Initialize largest as root
    l = 2 * i + 1     
    r = 2 * i + 2     
 
    # See if left child of root exists and is
    # greater than root
    if l < N and multiplier * arr[largest] < multiplier * arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < N and multiplier * arr[largest] < multiplier * arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, N, largest, ascending)
 