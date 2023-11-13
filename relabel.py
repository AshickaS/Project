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

def bulk_relabel(s1_list, s2):
    '''
    The function bulk_relabel() checks whether all the strings in s1_list have the same characters and return a list of relabelled strings in s1_list. 
    '''
    labels = 'abcdefghijklmnopqrstuvwxyz'
    results = []
    try:
        s1_sets = [set(s1) for s1 in s1_list]
        if not all(s == s1_sets[0] for s in s1_sets):
            raise Exception('All strings in s1_list must have the same set of characters.')
		
        values = dict()
        labels_list = sorted(s1_list[0])
        used = set()    
        for i in labels_list:
            j = i
            while j in s2 or j in used:
        	    j = labels[labels.index(j) + 1]
            used.add(j)
            values[i] = j
            
        for s1 in s1_list:
            result = ''
            for i in s1:
                result += values[i]
            result += s2
            results.append(result)
    except Exception as e:
        print(e)
    return results

