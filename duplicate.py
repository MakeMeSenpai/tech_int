def dup(list):
	index = 0
	for n in list:
		If list[index] == n:
			return true
		else:
			index += 1
	return false

lists = [[12, 3, 8, 8, 4], [1, 5, 6, 9, 10, 10], [2, 3, 6, 4, 8]]
for list in lists:
dup(list)