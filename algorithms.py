import drawLayout

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


def merge_sort(draw_info, ascending = True): 
    lst = draw_info.lst

#     if len(lst) < 2:
#         return lst[:]
#     else:
#         middle = len(lst) // 2
#         left = merge_sort(lst[:middle], compare)
#         right = merge_sort(lst[middle:], compare)
#         lst = merge(left, right, compare)
#     return lst


# def merge(left, right, compare):
#     result = []
#     i = 0
#     j = 0
#     while (i < len(left) and j < len(right)):
#         if compare(left[i], right[j]):
#             result.append(left[i])
#             i = i + 1
#         else:
#             result.append(right[j])
#             j = j + 1
#     while (i < len(left)):
#         result.append(right[j])
#         j = j + 1
#     return result

    if len(lst) > 1:
        mid = len(lst) // 2 #creates 2 subarrays by dividing lst into 2
        array1 = lst[:mid]
        array2 = lst[mid:]

    #sort independently
    merge_sort(array1)
    merge_sort(array2)

    #initial values
    i = 0 #initial index of left array
    j = 0 #initial index of right array
    k = 0 #initial index of merged array

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            lst[k] = array1[i]
            i = i + 1
        else:
            lst[k] = array2[j]
            j = j + 1
        drawLayout.draw_list(draw_info, {i: draw_info.GREEN, i+1: draw_info.RED, j: draw_info.GREEN, j+1: draw_info.RED, k: draw_info.GREEN, k+1: draw_info.RED}, True)
        yield True
        k = k + 1


    while i < len(array1):
        lst[k] = array1[i]
        i = i + 1
        k = k + 1
        drawLayout.draw_list(draw_info, {i: draw_info.GREEN, i+1: draw_info.RED, k: draw_info.GREEN, k+1: draw_info.RED}, True)
        yield True
    while j < len(array2):
        lst[k] = array2[j]
        j = j + 1
        k = k + 1
        drawLayout.draw_list(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED, k: draw_info.GREEN, k+1: draw_info.RED}, True)
        yield True
    return lst



def quick_sort(draw_info, ascending = True): 
    lst = draw_info.lst

    if(len(lst) > 1):
        piv = int(len(lst)/2)
        val = lst[piv]
        left = [i for i in lst if i<val]
        mid = [i for i in lst if i==val]
        right = [i for i in lst if i>val]

        result = quick_sort(left) + mid + quick_sort(right)
        return result
    else:
        return lst


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
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
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
 