
# My friend John and I are members of the "Fat to Fit Club (FFC)". 
#     John is worried because each month a list with the weights of members is 
#     published and each month he is the last on the list which means he is the heaviest.

# I am the one who establishes the list so I told him: 
#     "Don't worry any more, I will modify the order of the list". 
#     It was decided to attribute a "weight" to numbers. 
#     The weight of a number will be from now on the sum of its digits.

# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. 
#     Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

# Test.it("Basic tests")
# Test.assert_equals(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
# Test.assert_equals(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")


strng = '103 123 4444 99 2000'
strng = '11 11 2000 22 10003 123 1234000 44444444 9999' #should equal 
#       '11 11 2000 10003 22 123 1234000 44444444 9999'



def root(num):
    ln =[int(d) for d in str(num)]
    return sum(ln)

def order_weight(strng):
    A = sorted(strng.split())
    W = [ int(w) for w in A ]
    R = [ root(w) for w in W]
    R2 = sorted(R) 
    O = [R2.index(i) for i in R]
    W2 = [x for _,x in sorted(zip(O,W))]
    return ' '.join([ str(w) for w in W2 ])

order_weight(strng)




