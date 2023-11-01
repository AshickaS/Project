def relabel(s1, s2):
	'''
	The function relabel() takes as argument two strings s1, s2. It creates a sorted copy of s1 and relabel the letters to the next possible letter if the letter is either present in s2 or has already been assigned previously. The function returns the relabelled s1 concatenated to s2.
	'''
	labels = 'abcdefghijklmnopqrstuvwxyz'
	result = ''
	used = set()	
	values = dict()
	labels_list = sorted(s1)
	for i in labels_list:
		j = i
		while j in s2 or j in used:	
			j = labels[labels.index(j) + 1]
		used.add(j)
		values[i] = j
	for i in s1:
		result += values[i]
	result += s2
	return result