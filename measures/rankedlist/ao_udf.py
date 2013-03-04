import sys

l1 = set([])
l2 = set([])
overlap = {0: 0}
sum1 = 0.0
l1Counter = 0
l2Counter = 0
depth = 0

for line in sys.stdin:
    depth = depth + 1
    x , y = line.strip().split('\t')
    
    if x != None and len(x.strip()) == 0: x = None
    if y != None and len(y.strip()) == 0: y = None
    
    #increment number of elements in the two lists
    if x: l1Counter = l1Counter + 1
    if y: l2Counter = l2Counter + 1
   
    if x == y:
        overlap[depth] = overlap[depth-1] + 2
    else:
        v1 = 0
        v2 = 0
        if x in l2:
            l2.remove(x)
            v1 = 2
        else: l1.add(x)
        
        if y in l1:
            l1.remove(y)
            v2 = 2
        else: l2.add(y)
        overlap[depth] = overlap[depth-1] + v1 + v2
    sum1 = sum1 + float(overlap[depth])/(l1Counter + l2Counter)


print (sum1/depth)
 