#
# @author: Ritesh Agrawal
# @Date: 13 Feb 2013
# @Description: This is an implementation of average overlap measure for 
# comparing two score 
# (Refererence: http://www.umiacs.umd.edu/~wew/papers/wmz10_tois.pdf). 
# This is a modified implementation of  https://github.com/maslinych/linis-scripts/blob/master/rbo_calc.py
# It is a linear implementation of the RBO and assumes there are no
# duplicates and doesn't handle for ties. 
#

def score(l1, l2, depth = 10):
    """
        Calculates Average Overlap score. 
        l1 -- Ranked List 1
        l2 -- Ranked List 2
        depth -- depth
    """
    if l1 == None: l1 = []
    if l2 == None: l2 = []

    sl, ll = sorted([(len(l1), l1),(len(l2),l2)])
    s, S = sl  # s = length of smaller list, S = Smaller List
    l, L = ll  # l = length of longer list, L = Longer list
    #sanity check
    if s == 0: return 0
    depth = depth if depth < l else l
    
    # Calculate fraction of overlap from rank  at ranks 1 through depth
    # (the longer of the two lists)
    ss = set([])
    ls = set([])
    overlap = {0: 0}  # overlap holds number of common elements at depth d 
    sum1 = 0.0  

    for i in range(depth):
        # get elements from the two list
        x = L[i]
        y = S[i] if i < s else None
        depth = i+1
        # if the two elements are same, then we don't need
        # to them to the list and just increment the 
        if x == y: 
            overlap[depth] = overlap[i] + 2
        #else add items to the two list
        else:
            ls.add(x)
            if y != None: ss.add(y)
            overlap[depth] = overlap[i] + (2 if x in ss else 0) + (2 if y in ls else 0) 
        sum1 = sum1 + float(overlap[depth])/(len(S[0:depth]) + depth)

    return sum1/depth
    
    
if __name__ == "__main__":
    list1 = ['a','b','c','d','e']
    list2 = ['b','a','c','d','e']
    print score(list1,list2)

    list2 = ['a','b','c','e','d']
    print score(list1, list2)
