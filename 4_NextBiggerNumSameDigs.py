


# Create a function that takes a positive integer and returns the 
#     next bigger number that can be formed by rearranging its digits. For example:

# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071


from itertools import permutations

def next_num(n):
    ns = [d for d in n]    
    p = list(set([''.join(x) for x in list(permutations(ns)) if int(''.join(x)) >= int(n) ]))
    if len(p) == 1:
        return 'Z'
    return sorted(p)[1]

def last_n(n,l):
    if len(str(n)) > l:
        ln = len(str(n)) - l
        nn = next_num(str(n)[-l:])
        if nn != 'Z':
            return int(str(n)[:ln] + nn)
    return next_num(str(n))

def how_big(n, ns):   
    # If 4 or smaller, run directly:
    if len(ns) <= 4:
        return int(next_num(str(n))) 

    # if bigger than 4 then need to determine how far back to check
    if len(ns) > 4:
        l = 4
        while l <= len(ns):
            nsr = sorted(ns[-l:], reverse= True)
            if nsr != ns[-l:]:
                return int(last_n(n,l))
            l += 1

def next_bigger(n):
    ns = [int(d) for d in str(n)] 
    nsr = sorted(ns, reverse= True)
    if nsr == ns: #This solves for 9876543210 or 999999999
        return -1
    return how_big(n, ns)


n = 12598848484654321

n = 2665333

next_bigger(n)

dupl = sorted([''.join(x) for x in list(permutations(ns)) if x[0] >= f ])
set(dupl)


digits = list(str(n))
    for pos, d in reversed(tuple(enumerate(digits))):