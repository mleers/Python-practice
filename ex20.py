def bin_finder(list, target):
	lower = 0
	upper = len(list)
	while lower < upper:
		x = lower + (upper - lower) // 2  
		temp_val = list[x]
		if target == temp_val:
			return x
		elif target > temp_val:
			if lower == x:
				break
			lower = x
		elif target < temp_val:
			upper = x

