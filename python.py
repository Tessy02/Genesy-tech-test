from collection import Counter

def nth_rarest_item(list,n) 
#count occurances of each integer
counts = Counter(list)

#sort the unique integers by their occurrences
sorted_items = sorted(counts.items(),
key = lambda x: x[1])

#find the nth rarest item
if n<=len(sorted_items):
    return sorted_items[n-1][0]
    else:
        return None 
        #return none if n exceeds the number of unique items