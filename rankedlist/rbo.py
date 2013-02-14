#
# @author: Ritesh Agrawal
# @Date: 13 Feb 2013
# @Description: This is an implementation of rank biased overlap score 
# (Refererence: http://www.umiacs.umd.edu/~wew/papers/wmz10_tois.pdf). 
# This is a modified implementation of  https://github.com/maslinych/linis-scripts/blob/master/rbo_calc.py
# It is a linear implementation of the RBO and assumes there are no
# duplicates and doesn't handle for ties. 
#

def RBO(l1, l2, p = 0.98):
    """
        Calculates Ranked Biased Overlap (RBO) score. 
        l1 -- Ranked List 1
        l2 -- Ranked List 2
    """
    sl,ll = sorted([(len(l1), l1),(len(l2),l2)])
    s, S = sl
    l, L = ll
    if s == 0: return 0

    # Calculate the overlaps at ranks 1 through l 
    # (the longer of the two lists)
    ss = set([])
    ls = set([])
    x_d = {0: 0}
    sum1 = 0.0
    for i in range(l):
        x = L[i]
        y = S[i] if i < s else None
        d = i + 1
        if y != None and x == y: x_d[d] = x_d[d-1] + 1.0
        else: ls.add(x) 
        if y != None: ss.add(y)
        x_d[d] = x_d[d-1] + (1.0 if x in ss else 0.0) + (1.0 if y in ls else 0.0)     
        sum1 += x_d[d]/d * pow(p, d)
        
    sum2 = 0.0
    for i in range(l-s):
        d = s+i+1
        sum2 += x_d[d]*(d-s)/(d*s)*pow(p,d)

    sum3 = ((x_d[l]-x_d[s])/l+x_d[s]/s)*pow(p,l)

    # Equation 32
    rbo_ext = (1-p)/p*(sum1+sum2)+sum3
    return rbo_ext
    
    
if __name__ == "__main__":
    list1 = ['0','1','2','3','4','5']
    list2 = ['1','0','2','3','4','5']
    print RBO(list1,list2, p = 0.98)

    list1 = ['012']
    list2 = []
    print RBO(list1, list2, p = 0.98)
